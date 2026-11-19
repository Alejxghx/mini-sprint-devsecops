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
