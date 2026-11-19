# Mini Sprint DevSecOps

Práctica de Ciclos de Desarrollo de Software Seguro con la API Flask suministrada por la cátedra. Datos ficticios, ejecución exclusivamente local en 127.0.0.1.

## Definition of Done

- Bandit sin hallazgos y pip-audit sin vulnerabilidades conocidas en las dependencias resueltas.
- Pruebas de autenticación y rechazo de inyección SQL aprobadas.
- Hook detect-secrets instalado y rechazo de credencial ficticia demostrado.
- Build Breaker de GitHub Actions en verde y cambios revisados mediante Pull Request antes de integrar. La revisión humana por otro integrante debe hacerla una persona; el check automático no la sustituye.

## Tablero ágil

Ver [TABLERO.md](TABLERO.md). Cada historia enlaza a su issue y se cierra cuando la corrección y sus verificaciones están listas.

## Evidencias

El historial del Pull Request conserva el escenario vulnerable y su remediación. Los informes locales y el SBOM se almacenan en `evidence/`. El pipeline genera además un SBOM descargable por ejecución.

## Ejecutar la versión corregida

Requiere Python 3.12 y Git. Crear un entorno virtual e instalar `requirements.txt`. Exportar `API_KEY`, `DEMO_USERNAME` y `DEMO_PASSWORD` con valores ficticios elegidos para la práctica, y ejecutar `python app.py`. La aplicación no carga `.env` automáticamente: exporte las variables en su terminal. La base corregida es `practica_segura.db` para no reutilizar contraseñas en texto plano del laboratorio original.

Instalar `pre-commit==4.7.0` y ejecutar `pre-commit install`. El hook local ejecuta detect-secrets 1.5.0 con verificación remota desactivada para no enviar las credenciales ficticias. La carpeta `evidence/` conserva resultados históricos y queda excluida del hook; el código de la aplicación sí se examina.

Validar con `python -m pytest -q`, `bandit -r app.py` y `pip-audit -r requirements.txt --strict`. Los endpoints siguen siendo `/api/health`, `/api/login` y `/api/profile`. Este laboratorio no incluye sesiones ni JWT ni se considera un servicio listo para producción.
