Guion de exposición de cinco minutos

0:00 a 0:40  Presentación
Buenos días. Soy Robert Garcia y voy a presentar el mini sprint DevSecOps realizado con una API Flask. El objetivo fue revisar una aplicación con fallos de seguridad, organizar las correcciones y comprobar que los controles automáticos detectaran los problemas antes de integrar los cambios. La práctica se ejecutó localmente con datos ficticios.

0:40 a 1:40  Hallazgos
La aplicación recibe peticiones HTTP mediante Flask y guarda usuarios en una base SQLite. Tiene tres endpoints: health para comprobar el servicio, login para autenticar y profile para consultar un perfil con una clave. En la lectura del código encontré SQL concatenado, una clave escrita directamente en el programa y contraseñas guardadas sin hash. La prueba más clara fue el login: una entrada SQL manipulada permitió acceder con una contraseña incorrecta. Bandit señaló la consulta y pip-audit registró 54 avisos en cinco paquetes. Al eliminar repeticiones quedaron 28 combinaciones de paquete y CVE, que constan en la tabla del informe.

1:40 a 2:30  Organización y correcciones
Mostrar el tablero de GitHub Projects durante diez segundos.
Organicé cuatro historias: corregir la autenticación, retirar secretos, actualizar dependencias y automatizar los controles. Para cerrar una historia exigí análisis de seguridad y pruebas aprobadas. Cambié la consulta por una parametrizada, protegí las contraseñas con hash scrypt y pasé la clave a variables de entorno. También actualicé las dependencias y generé el inventario SBOM en JSON con CycloneDX.

2:30 a 4:15  Demostración
Abrir primero la ejecución fallida y después la aprobada. Dedicar unos treinta segundos a cada pantalla.
Aquí se observa el antes: Bandit y pip-audit fallaron, por lo que el Build Breaker también quedó en rojo. La rama principal exige este control para integrar cambios. Después de las correcciones, los cuatro controles terminaron en verde. Bandit no encontró hallazgos, pip-audit no detectó vulnerabilidades conocidas y pasaron las 14 pruebas funcionales. La inyección SQL ahora recibe 401 y las credenciales válidas conservan la respuesta 200.
Mostrar la captura del rechazo del commit durante quince segundos.
Además instalé pre-commit con detect-secrets. Al intentar confirmar una credencial ficticia, el hook rechazó el commit antes de que el archivo entrara al repositorio. Esto permite detectar un error en el equipo local y después repetir otros controles en GitHub Actions.

4:15 a 5:00  Lecciones y cierre
La principal lección fue incorporar la seguridad durante el desarrollo. Los análisis automáticos ayudan, pero también hacen falta lectura del código y pruebas de comportamiento. Por ejemplo, el bypass de autenticación se comprobó con una petición real, además del aviso de Bandit. El reto fue corregir los riesgos sin romper el acceso válido y dejar evidencia del antes y el después. El check verde es una aprobación automática; la revisión humana del Pull Request sigue siendo un paso separado. Con estos controles, la seguridad forma parte del trabajo diario del desarrollo.
