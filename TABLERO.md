# Tablero del mini sprint

[Tablero real en GitHub Projects](https://github.com/users/Alejxghx/projects/2/views/2)

Objetivo: corregir los riesgos de la API heredada y verificar los controles DevSecOps.

| Historia | Prioridad | Estado | Criterio de aceptación |
| --- | --- | --- | --- |
| [SEC 01](https://github.com/Alejxghx/mini-sprint-devsecops/issues/2) Parametrizar autenticación | Alta | Hecho | La inyección SQL se rechaza con 401 y el acceso válido funciona |
| [SEC 02](https://github.com/Alejxghx/mini-sprint-devsecops/issues/3) Retirar secretos del código | Alta | Hecho | Clave desde entorno y contraseñas protegidas con hash |
| [SEC 03](https://github.com/Alejxghx/mini-sprint-devsecops/issues/4) Actualizar dependencias | Alta | Hecho | pip-audit sin vulnerabilidades conocidas |
| [SEC 04](https://github.com/Alejxghx/mini-sprint-devsecops/issues/5) Automatizar controles | Alta | Hecho | Hook rechaza secreto y CI muestra fallo antes y éxito después |

## Sprint review

Verificación local: 14 pruebas aprobadas, Bandit sin hallazgos, auditoría sin vulnerabilidades conocidas y rechazo real de una credencial ficticia por pre-commit.

- [CI original fallido](https://github.com/Alejxghx/mini-sprint-devsecops/actions/runs/44523926944)
- [CI corregido aprobado](https://github.com/Alejxghx/mini-sprint-devsecops/actions/runs/44526560811)
- [Pull Request de remediación](https://github.com/Alejxghx/mini-sprint-devsecops/pull/1)

La aprobación automática se verificó; la revisión humana del PR y la exposición en clase son pasos posteriores.
