# Evidencias de ejecución

Los JSON y TXT conservan las salidas de las herramientas. `capturas/` contiene capturas reales de Playwright tomadas sobre una terminal web local que ejecutó los comandos, sin reemplazar ni dibujar sus resultados. Las consultas a GitHub se hicieron con la herramienta oficial `gh`. El tablero se abrió con un visor local de `TABLERO.md`; no es una captura de GitHub Projects.

El rechazo del commit muestra código 1 del hook. El script verificador devuelve 0 cuando comprueba correctamente el rechazo. Los avisos repetidos de pip-audit se agrupan por paquete y CVE en `MITIGACIONES.md`, conservando el JSON sin modificar.

`demo_api.py` ejecuta la versión corregida con el cliente de pruebas real de Flask y una base efímera. Ejecutar desde la raíz con `python evidence/demo_api.py`.
