# Tablero del mini sprint

Objetivo: corregir los riesgos de la API heredada y verificar los controles DevSecOps.

| Historia | Prioridad | Estado | Criterio de aceptación |
| --- | --- | --- | --- |
| SEC 01 Parametrizar autenticación | Alta | Pendiente | La inyección SQL se rechaza con 401 y el acceso válido funciona |
| SEC 02 Retirar secretos del código | Alta | Pendiente | Clave desde entorno y contraseñas protegidas con hash |
| SEC 03 Actualizar dependencias | Alta | Pendiente | pip-audit sin vulnerabilidades conocidas |
| SEC 04 Automatizar controles | Alta | En curso | Hook rechaza secreto y CI muestra fallo antes y éxito después |
