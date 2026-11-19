"""API de laboratorio corregida. Ejecutar únicamente en localhost."""
import os
import secrets
import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        DATABASE=str(Path(__file__).with_name("practica_segura.db")),
        API_KEY=os.environ.get("API_KEY"),
        MAX_CONTENT_LENGTH=16384,
    )
    if test_config:
        app.config.update(test_config)
    if not app.config["API_KEY"]:
        raise RuntimeError("Defina API_KEY en el entorno antes de iniciar la API")

    @app.get("/api/health")
    def health():
        return jsonify(status="ok", service="API de práctica")

    @app.get("/api/profile")
    def profile():
        supplied = request.headers.get("X-API-Key", "")
        if not secrets.compare_digest(
            supplied.encode("utf-8"), app.config["API_KEY"].encode("utf-8")
        ):
            return jsonify(error="No autorizado"), 401
        return jsonify(user="admin", message="Acceso de demostración")

    @app.post("/api/login")
    def login():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify(error="Se requiere un objeto JSON"), 400
        username, password = data.get("username"), data.get("password")
        if (
            not isinstance(username, str) or not isinstance(password, str)
            or not username or not password
            or len(username) > 100 or len(password) > 256
        ):
            return jsonify(error="Credenciales con formato inválido"), 400
        with sqlite3.connect(app.config["DATABASE"]) as conn:
            row = conn.execute(
                "SELECT id, username, password_hash FROM users WHERE username = ?",
                (username,),
            ).fetchone()
        if row and check_password_hash(row[2], password):
            return jsonify(message="Login correcto", user={"id": row[0], "username": row[1]})
        return jsonify(error="Credenciales inválidas"), 401

    return app


def init_db(app, username, password):
    """Crea usuario de laboratorio con hash scrypt, sin guardar texto plano."""
    if not username or not password:
        raise RuntimeError("Defina DEMO_USERNAME y DEMO_PASSWORD en el entorno")
    with sqlite3.connect(app.config["DATABASE"]) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users "
            "(id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT NOT NULL)"
        )
        conn.execute(
            "INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )


if __name__ == "__main__":
    app = create_app()
    init_db(app, os.environ.get("DEMO_USERNAME"), os.environ.get("DEMO_PASSWORD"))
    app.run(host="127.0.0.1", port=5000, debug=False)
