"""Repite la prueba de la versión corregida usando datos efímeros."""
import secrets
import tempfile
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import create_app, init_db
with tempfile.TemporaryDirectory() as d:
    key, password = secrets.token_urlsafe(24), secrets.token_urlsafe(20)
    app = create_app({'DATABASE': str(Path(d) / 'demo.db'), 'API_KEY': key})
    init_db(app, 'admin', password)
    c = app.test_client()
    for label, body in [
        ('Contraseña incorrecta', {'username': 'admin', 'password': secrets.token_urlsafe(12)}),
        ('Inyección SQL', {'username': "' OR 1=1 -- ", 'password': secrets.token_urlsafe(12)}),
        ('Credencial válida', {'username': 'admin', 'password': password}),
    ]:
        r = c.post('/api/login', json=body)
        print(label, '=> HTTP', r.status_code)
    print('Perfil sin clave => HTTP', c.get('/api/profile').status_code)
    print('Perfil con clave => HTTP', c.get('/api/profile', headers={'X-API-Key': key}).status_code)
