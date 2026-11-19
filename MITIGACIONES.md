# Decisiones de mitigación

Auditoría original: 54 registros. La tabla agrupa identificadores CVE repetidos: 28 pares paquete y aviso. El informe JSON conserva la salida original completa. La presencia de una dependencia vulnerable no demuestra que cada vector se pueda explotar en esta API.

| Paquete original | CVE o aviso | Versiones de corrección indicadas por la auditoría | Decisión aplicada |
| --- | --- | --- | --- |
| flask 2.2.2 | CVE-2023-30861 | 2.2.5,2.3.2 | Actualizar a 3.1.3 y volver a auditar |
| flask 2.2.2 | CVE-2026-27205 | 3.1.3 | Actualizar a 3.1.3 y volver a auditar |
| werkzeug 2.2.2 | CVE-2023-23934 | 2.2.3 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2023-25577 | 2.2.3 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2023-46136 | 2.3.8,3.0.1 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2024-34069 | 3.0.3 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2024-49766 | 3.0.6 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2024-49767 | 3.0.6 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2025-66221 | 3.1.4 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2026-21860 | 3.1.5 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2026-27199 | 3.1.6 | Actualizar a 3.1.9 y volver a auditar |
| werkzeug 2.2.2 | CVE-2026-102598 | 3.1.9 | Actualizar a 3.1.9 y volver a auditar |
| requests 2.20.0 | CVE-2023-32681 | 2.31.0 | Actualizar a 2.34.2 y volver a auditar |
| requests 2.20.0 | CVE-2024-35195 | 2.32.0 | Actualizar a 2.34.2 y volver a auditar |
| requests 2.20.0 | CVE-2024-47081 | 2.32.4 | Actualizar a 2.34.2 y volver a auditar |
| requests 2.20.0 | CVE-2026-25645 | 2.33.0 | Actualizar a 2.34.2 y volver a auditar |
| idna 2.7 | CVE-2024-3651 | 3.7 | Actualizar a 3.20 y volver a auditar |
| idna 2.7 | CVE-2026-45409 | 3.15 | Actualizar a 3.20 y volver a auditar |
| urllib3 1.24.3 | CVE-2020-26137 | 1.25.9 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2024-37891 | 1.26.19,2.2.2 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2023-43804 | 1.26.17,2.0.6 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2023-45803 | 1.26.18,2.0.7 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2025-50181 | 2.5.0 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2025-66418 | 2.6.0 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2025-66471 | 2.6.0 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2026-21441 | 2.6.3 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2026-44431 | 2.7.0 | Actualizar a 2.8.0 y volver a auditar |
| urllib3 1.24.3 | CVE-2026-97689 | 2.8.0 | Actualizar a 2.8.0 y volver a auditar |

La versión final resuelve 12 paquetes fijados y la auditoría no detecta vulnerabilidades conocidas en ellos. Para secretos y SQL se aplicaron variables de entorno, hash scrypt, consultas parametrizadas y validación de entradas.
