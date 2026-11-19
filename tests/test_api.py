import secrets
import sqlite3

import pytest

from app import create_app, init_db


@pytest.fixture()
def lab(tmp_path):
    key, password = secrets.token_urlsafe(24), secrets.token_urlsafe(20)
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "test.db"), "API_KEY": key})
    init_db(app, "admin", password)
    return app, app.test_client(), key, password


def test_health(lab):
    assert lab[1].get('/api/health').status_code == 200


def test_valid_login(lab):
    assert lab[1].post('/api/login', json={"username": "admin", "password": lab[3]}).status_code == 200


def test_invalid_login(lab):
    assert lab[1].post('/api/login', json={"username": "admin", "password": secrets.token_urlsafe(12)}).status_code == 401


@pytest.mark.parametrize('field', ['username', 'password'])
def test_sql_injection_is_rejected(lab, field):
    body = {"username": "admin", "password": secrets.token_urlsafe(12)}
    body[field] = "' OR 1=1 -- "
    assert lab[1].post('/api/login', json=body).status_code == 401


@pytest.mark.parametrize('body', [None, [], "texto", {}, {"username": 12, "password": []}, {"username": "a" * 101, "password": "a"}])
def test_malformed_body(lab, body):
    assert lab[1].post('/api/login', json=body).status_code == 400


def test_profile_authorization(lab):
    client = lab[1]
    assert client.get('/api/profile').status_code == 401
    assert client.get('/api/profile', headers={"X-API-Key": "incorrecta"}).status_code == 401
    assert client.get('/api/profile', headers={"X-API-Key": lab[2]}).status_code == 200


def test_password_is_hashed(lab):
    with sqlite3.connect(lab[0].config['DATABASE']) as conn:
        stored = conn.execute('SELECT password_hash FROM users').fetchone()[0]
    assert stored != lab[3]
    assert stored.startswith('scrypt:')


def test_missing_api_key(monkeypatch):
    monkeypatch.delenv('API_KEY', raising=False)
    with pytest.raises(RuntimeError, match='API_KEY'):
        create_app()
