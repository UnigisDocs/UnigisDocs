Metodología de Implementación
=============================
.. container:: justified-text
    
 El proceso del producto se compone por tres metodologías que se aplican a un tercio de la capacidad del equipo, ¿Qué significa a un tercio de capacidad? se refiere a que al inicio de la planeación el equipo toma en cuenta las actividades que se planean al inicio del periodo, las actividades de del día a día y reserva, y actividades que se planean trimestralmente esto entraría dentro del objetivo del producto. 
    
 Las metodologías que se aplican a lo largo del proceso de trabajo son las siguientes:

 +--------------+-------------+-------------+
 |     SCRUM    |    KANBAN   |  SSM SAFe4  |
 +==============+=============+=============+
 |              |             |             |
 +--------------+-------------+-------------+

**Scrum adaptado**

.. container:: justified-text

    El inicio del Sprint se selecciona el avance de trabajo correspondiente al plan de producto que se desea entregar en la duración del periodo, la duración es de dos semanas con releases semanales, es decir, la finalización del plan de trabajo está compuesta por dos releases (versiones) dichas versiones son de tipo BETA que se compilan a una versión final, esto permite al equipo atender de manera ágil los defectos del producto. 
    
    Se realizan Dailys Meetings todos los días a las 9:30 am con una duración promedio de 30 minutos, dentro de los Dailys se presentan las siguientes preguntas por cada miembro del scrum team.

    - ¿Qué hice ayer?
    - ¿Qué voy a hacer hoy?
    - ¿Identifique algún bloqueo?
    - ¿Qué puedo aportar? (Adaptación UNIGIS desde modelo “we say we listen”).

    Dentro de los Dailys Meeting no se discuten temas por fuera de la agenda, no es un reporte de avances, los líderes responden de la misma manera.

**Kanban: agile al agile**

.. container:: justified-text

    La implementación de Kanban dentro de la metodología UNIGIS nos ayuda con la planeación dinámica día a día, es decir, esto permite una mejor colaboración con la gestión visual de tareas. Dentro de las tareas que pueden existir en el Backlog del Kanban puede haber incidencias urgentes (soportes nivel 3), defectos detectados por QA y respuestas ágiles a los cambios de alcance o nuevos requerimientos que se encuentran fuera de la planeación del sprint. 
    
    La gestión diaria de las tareas se realiza por medio de Jira software en donde se encuentran todos los proyectos vigentes que intervienen en el proceso de desarrollo esto permite identificar de manera útil las tareas que tiene el equipo para entregar el trabajo de manera ágil y sobre todo controlada.

.. table:: kanban

   +--------------+-------------+-------------+
   |     TO DO    | IN PROGRESS |     DONE    |
   +==============+=============+=============+
   |              |             |             |
   +--------------+-------------+-------------+

**Safe 4 Scrum Master 4 (SSM)**

.. container:: justified-text

    Scaled Agile Framework® (SAFe®) es un ambiente de trabajo que sigue patrones y flujo de trabajo los cuales funcionan para implementar prácticas ágiles a un nivel de escalamiento empresarial. El marco constituye un cúmulo de conocimientos que incluye instrucciones estructuradas sobre las funciones y responsabilidades, la forma de planificar y gestionar el trabajo, los valores que hay que defender. Es decir, dentro de UNIGIS se promueve la coherencia, la colaboración y la gestión a través de un gran número de equipos agiles, pero todos siguiendo el mismo objetivo del producto.
    
    La duración de este método de trabajo tiene una duración de 3 meses y tiene como resultado una versión mayor dentro del producto. 

.. image:: Metodologíalight.png
    :align: center
    :class: only-light

.. image:: Metodologíablack.png
    :align: center
    :class: only-dark

Versiones
----------

.. container:: justified-text

    La numeración de las versiones de los incrementos de software nos permite expresar de forma normalizada las modificaciones existentes entre las distintas versiones, indicando los cambios que se han producido entre una versión y la siguiente.

    Dentro de la metodología de trabajo, las publicaciones se realizan de dos maneras:

    1. LTS (Long Term Support)

    Una LTS o una implementación estándar es aquella que se implementa en producción para los clientes, con una publicación cada 3 meses y un soporte de optimización durante 12 meses. Esto significa que durante un año, se tienen cuatro versiones que se optimizan continuamente.
    
    Esto nos permite disponer con:

    - Versiones estables.
    - No se desarrollan nuevo features standares durante esa versión, solo se atienden bug-fixing.
    - Permite desarrollos sobre customs, se atienden las necesidades de acuerdo con el cliente, pero sin cambiar el producto estándar.
    - Extensas pruebas de calidad por el área de QA Test.
    - El esquema de soporte incluye liberaciones cada 2 semanas en modo Branch, esto permite atender de manera adecuada los errores que la versión presenten sin regresiones. 

.. table:: Nomenclatura LTS

   +---------------+--------------+---------------+--------------+
   | Versión Mayor | Versión LTS  |Interacción LTS|    Hot Fix   |
   +===============+==============+===============+==============+
   |               |              |               |              |
   +---------------+--------------+---------------+--------------+

.. container:: justified-text

 *Versión Mayor*. La versión mayor o principal en la que se encuentra el producto, este representa la versión más representativa y es actualizada cuando presenta cambio no retro compatibles, es decir, cuando se cambia la funcionalidad del software o ya no es compatible con funcionalidades anteriores.

 *Versión LTS*. Indica el número de LTS que se encuentra, es decir, son medianas funcionalidades o nuevas compatibles con la versión mayor. Esta solo será en múltiplos de 10. 

 *Interacción LTS*. Indica que hubo una liberación de bug fixing sobre la misma versión, es decir, la versión ya cuenta con una actualización de errores o nuevas características, esto sin modificar la funcionalidad existente. 

 *Hot Fix*. Se hace referencia a hot fix cuando hablamos a arreglos de urgencia o parche rápido, generalmente se usa este funcionamiento para arreglos de urgencia que no pueden esperar un ciclo de bug fixing y debe ser resuelto lo antes posible. Para el desarrollador, un hotfix implica que el cambio ha sido creado rápidamente y fuera de los procesos normales de desarrollo y pruebas.

 Por ejemplo: 10.230.02.0-LTS 

 Se entiende la versión principal recibio una actualización importante de versión LTS.  

 +---------------+--------------+---------------+--------------+
 | Versión Mayor | Versión LTS  |Interacción LTS|    Hot Fix   |
 +===============+==============+===============+==============+
 |      10       |     230      |      00       |      0       |
 +---------------+--------------+---------------+--------------+

 Se entiende la versión principal y la versión LTS recibio una actualización y correccioón de funcionalidades sobre la misma versión.

 +---------------+--------------+---------------+--------------+
 | Versión Mayor | Versión LTS  |Interacción LTS|    Hot Fix   |
 +===============+==============+===============+==============+
 |      10       |     230      |      01       |      0       |
 +---------------+--------------+---------------+--------------+

 2. **Desarrollo: Beta**
 
 Una versión de tipo Beta se refiere a versiones de prueba o versión preliminar del producto, incluyen todos los avances que tiene el producto semanalmente, se integran: ciclos de QA smoke test y unit test automatizados para detectar regresiones sobre las características principales y Bug fixing, estas versiones se realizan de manera ágil. Las versiones Beta pueden ir a producción sin esperar la próxima versión LTS solo sí se cumple con todas las pruebas completas en el ambiente de cada cliente.

.. table:: Nomenclatura BETA

   +---------------+---------------+---------------+--------------+
   | Versión Mayor | Versión Menor |  Hot Feature  |    Hot Fix   |
   +===============+===============+===============+==============+
   |               |               |               |              |
   +---------------+---------------+---------------+--------------+

.. container:: justified-text

 *Versión Mayor*. La versión mayor o principal en la que se encuentra el producto, este representa la versión más representativa y es actualizada cuando presenta cambio no retro compatibles, es decir, cuando se cambia la funcionalidad del software o ya no es compatible con funcionalidades anteriores.

 *Versión menor*. A diferencia de las versiones LTS esta se Indica con números incrementables, es decir, que se está actualizando. Esta será un consecutivo de la LTS en la que se está atendiendo semanalmente hasta llegar a la nueva LTS.

 *Hot Feature*. Indica que hubo una liberación intermedia de bug fixing no puede esperar el ciclo del sprint. Se entiende como Hot Feature a una característica o solución urgentes.

 *Hot Fix*. Se reserva para arreglos de urgencia que no pueden esperar un ciclo de bug fixing y debe ser resuelto lo antes posible.

 Por ejemplo: 10.221.00.0-LTS 

 Se entiende la versión mayor recibio una actualización beta dentro de la misma LTS.

 +---------------+---------------+---------------+--------------+
 | Versión Mayor | Versión Menor |  Hot Feature  |    Hot Fix   |
 +===============+===============+===============+==============+
 |      10       |     231       |       0       |      0       |
 +---------------+---------------+---------------+--------------+

 +---------------+---------------+---------------+--------------+
 | Versión Mayor | Versión Menor |  Hot Feature  |    Hot Fix   |
 +===============+===============+===============+==============+
 |      10       |     232       |      0        |      0       |
 +---------------+---------------+---------------+--------------+

 
Soporte
--------

.. container:: justified-text

 **Visión**

 Lograr un servicio de Soporte Técnico a los clientes que se asegure el uso y la adopción de UNIGIS como parte critica de sus procesos de negocios aportando los beneficios esperados. Generar usuarios fieles de UNIGIS TMS.
 Objetivos del Servicio

 **Pilares fundamentales**

 - Colaboración y Sinergia: Trabajo en equipo en todas las áreas internas para dar la mejor atención y la más rápida respuesta a las consulta y problemas a los clientes con el uso de UNIGIS.

 - Estandarizar Procesos: Unificar procesos y criterios para la atención y apoyo a los clientes UNIGIS brindando un servicio homogéneo con calidad y escalable en toda la región y países que se requiera.

 - Base de Conocimiento: Con la información UNIGIS disponible, las consultas y respuestas a los clientes crear una base de conocimientos (KB) que permita el auto consulta y soporte, generar mayor autonomía en el equipo de soporte y servicios, facilitar la capacitación interna y externa. centralizar y generar conocimiento.

 - Medirnos SLA / SLO: Compromiso con el servicio al cliente, asegurando los tiempos de respuesta de resolución.

 - Soporte Proactivo (24x7x365): Implementar un equipo regional de soporte para amplia la franja horaria de atención a clientes. Detección temprana preventiva de errores y riesgos con el monitoreo activa 7/24 y alertas en el ambiente de UNIGIS CLOUD y on premise. Guardias pasivos con escalamientos para soporte fuera de horario.

 **Niveles de Soporte**

 El nivel 1 es donde el equipo de soporte interviene por primera vez. Quienes trabajan en este nivel muchas veces no tienen conocimientos profundos sobre el producto o servicio que ofrecen, en cambio, saben resolver problemas básicos buscando información dentro de una base de datos. Es importante que este personal tenga cualidades como facilidad de palabra, paciencia, empatía y capacidad de comprender el problema del cliente, incluso si la explicación no es muy clara. Otra característica clave es la capacidad para determinar cuándo escalar la situación al siguiente nivel de atención. Las tareas del soporte básico varían según el producto, entre ellas:

 - Crear de tickets.
 - Restablecer de contraseña.
 - Revisar el rendimiento de la red.
 - Ayudar a los usuarios en el uso de software y hardware.

 El nivel 2 atiende problemas más complejos, por lo que su conocimiento de la parte mecánica, las herramientas y el software que componen el producto es mayor. Generalmente, se deriva a este personal los problemas que no pudieron resolverse en el primer nivel de atención. Estas son algunas de sus funciones:

 - Revisar los tickets no resueltos en el nivel 1.
 - Identificar las soluciones que ya se probaron.
 - Evaluar el problema.
 - Hablar con el cliente para conocer más detalles del problema.
 - Proponer nuevas soluciones.
 - Derivar al siguiente nivel si estas soluciones no funcionan.

 
 El nivel 3 se conforma por profesionales que, además de conocer a fondo los productos y servicios, también tienen profundos conocimientos técnicos. Generalmente se encargan de revisar a fondo redes, códigos y estructuras y hacen reparaciones clave para la integridad de los sistemas. Algunas de sus principales funciones son las siguientes:

 - Analizar problemas de código, arquitectura o hardware.
 - Revisar sistemas, dar mantenimiento y hacer reparaciones.
 - Atender los tickets no resueltos del nivel 1 y 2.

 **Jira Service Desk**
 
 Acceso al servicio de soporte mediante un formulario de Alta de cliente al servicio UNIGIS Service Desk.

 Formulario donde se completan los datos del cliente implementando de producción que accede al servicio de UNIGIS Service Desk. Se establece un usuario y una contraseña genérica para acceder al sistema UNIGIS SD y se solicita que se el interlocutor / key user quien centraliza, usa y registra las solicitudes. El cliente acepta (firma) las condiciones de uso del servicio, esencialmente acepta el SLA de UNIGIS. Si la cliente esta on premise debe aceptar un acceso remoto permanente para poder dar soporte y cumplir con el SLA. Este documente está pendiente de definición con la dirección.

.. _a link: https://support.unigis.com/

.. container:: justified-text
 
 Acceso al servicio UNIGIS Service Desk
 El equipo de servicio UNIGIS al completar un proyecto que pasa al servicio UNIGIS Service Desk, entrega la documentación completa del cliente para pasar a producción y acceder al servicio, entre ellas módulos contratados y cantidad de licencias, flujos definidos, integraciones, key users de la cuenta y contactos. Si el cliente es on premise se debe indicar los datos de conexión. Toda esta documentación necesaria para poder brindar un soporte técnico adecuada se define en conjunto con los equipos de servicio y producto/desarrollo de UNIGIS.

 Acceso al servicio UNIGIS Service Desk

 El equipo de servicio UNIGIS al completar un proyecto que pasa al servicio UNIGIS Service Desk, entrega la documentación completa del cliente para pasar a producción y acceder al servicio, entre ellas módulos contratados y cantidad de licencias, flujos definidos, integraciones, key users de la cuenta y contactos. Si el cliente es on premise se debe indicar los datos de conexión. Toda esta documentación necesaria para poder brindar un soporte técnico adecuada se define en conjunto con los equipos de servicio y producto/desarrollo de UNIGIS.

 - Es una herramienta personalizable.

 - Soporta administración de cambios y problemas.

 - Integración nativa con Jira Software y Confluence.

 - Soporta multi idiomas.

 - Admite el uso de plugins para incorporar nuevas funcionalidades.
 
 Al iniciar sesión dentro de jira service desk el usuario puede visualizar la siguiente pantalla en donde se encuentra dos tipos de solicitudes:

.. image:: jirasd.png
    :align: center


Consulta de Soporte
    Para el formato de solicitud de consulta de soporte se realiza cuando el usuario presenta alguna duda o consulta sobre el funcionamiento de UNIGIS.

.. image:: Consulta.png
    :align: center

Consultas generales acerca del funcionamiento del sistema o temas relacionados con el uso de este. Incluye todos los temas que no requiera una modificación directa sobre los productos UNIGIS.

Proceso:

.. image:: Consultalight.png
    :align: center
    :class: only-light

.. image:: Consultablack.png
    :align: center
    :class: only-dark

Reportar problema
    Para el formato de reporte de problema se realiza cuando el usuario presenta algún problema con el producto y debe de capturar todos los datos para su resolución. 

.. image:: reporte.png
    :align: center

Reporte de errores detectados en UNIGIS. Alguna funcionalidad incluida no cumple correctamente con su propósito y se requiere corrección, es cuando se realiza el levantamiento de una incidencia para su análisis y seguimiento.

Proceso:
 
.. image:: Problemalight.png
    :align: center
    :class: only-light

.. image:: Problemablack.png
    :align: center
    :class: only-dark

Solicitudes
    Dentro de Jira Service Desk el usuario puede ver el listado de sus solicitudes y el estado en la que se encuentran para su gestión.

.. image:: solicitud.png
    :align: center

Cambios programados requeridos por una nueva funcionalidad, ajustes o resolución de un problema UNIGIS. Los cambios pueden ser requeridos por el consultor o líder de proyecto, pero no por el cliente, el cambio a diferencia del problema pasa por un esquema de aprobaciones. Ejemplo: Actualizaciones del sistema.

Proceso: 

.. image:: Cambioslight.png
    :align: center
    :class: only-light

.. image:: Cambiosblack.png
    :align: center
    :class: only-dark

SLA Y SLO
----------
.. container:: justified-text
    
    Como objetivo inicial los tiempos del SLO son sensiblemente menores a los definidos en el SLA, estos son 50% menor aproximadamente, teniendo como meta el compromiso con el servicio y el 100% de cumplimiento de SLA.

    - SLA 

    Impacto. Sin disponibilidad de la plataforma UNIGIS (Máximo) 
    
    – Operación afectada severamente (Alto) 
   
    – La solución UNIGIS está funcionando con impedimento (Medio) 
    
    – No afecta la operación en producción (Bajo).
    
    Categoría de cliente. Definición comercial.
    Tipo de solicitud. La solicitud recibida está vinculada a la resolución de un problema o es una consulta. 
    
    Problema > Consulta
    
    Tiempo de respuesta. Es el tiempo que transcurre entre la recepción de la solicitud y la asignación al especialista para comenzar con el tratamiento de esta y la respectiva notificación al cliente.

    Tiempo de Resolución. Es el tiempo entre que se recibe la solicitud y se diagnostica y el especialista da por resuelta la solicitud de servicio.


+--------------------+-----------+--------------------+---------------------+--------------------+
| TIPO DE INCIDENCIA | PRIORIDAD |     DESCRIPCIÓN    | TIEMPO DE RESPUESTA | TIEMPO DE SOLUCIÓN |
+====================+===========+====================+=====================+====================+
| Soporte General    |   Máxima  | Sin disponibilidad |      1-2 horas      |      2-4 horas     |
+--------------------+-----------+--------------------+---------------------+--------------------+
| Soporte General    |   Alta    | Afecta la operación|      2-4 horas      |      4-8 horas     |
+--------------------+-----------+--------------------+---------------------+--------------------+
| Soporte General    |   Media   | Errores menores    |      4-8 horas      |      8-16 horas    |
+--------------------+-----------+--------------------+---------------------+--------------------+
| Soporte General    |   Baja    | No afecta operación|      8-12 horas     |      16-36 horas   |
+--------------------+-----------+--------------------+---------------------+--------------------+

.. container:: justified-text
    
    - SLO
    
    Tiempo de respuesta. Es el tiempo que transcurre entre la recepción de la solicitud y la asignación al especialista para comenzar con el tratamiento de esta y la respectiva notificación al cliente.
    
    Tiempo de Resolución. Es el tiempo entre que se recibe la solicitud y se diagnostica y el especialista da por resuelta la solicitud de servicio.

.. image:: slaslo.png
   :align: center
   :width: 400px
   :height: 320px


+---------------+---------------------+------------------------+
|      SLO      | TIEMPO DE RESPUESTA |  TIEMPO DE RESOLUCIÓN  |
+===============+=====================+========================+
|  Bloqueante   |     30 minutos      |         1 hora         |
+---------------+---------------------+------------------------+
|   Muy alto    |       1 hora        |         2 horas        |
+---------------+---------------------+------------------------+
|    Alto       |       2 horas       |         4 horas        |
+---------------+---------------------+------------------------+
|    Medio      |       4 horas       |         8 horas        |
+---------------+---------------------+------------------------+
|     Bajo      |       4 horas       |         16 horas       |
+---------------+---------------------+------------------------+
|   Muy bajo    |       4 horas       |         24 horas       |
+---------------+---------------------+------------------------+
| Sin impacto   |       8 horas       |         36 horas       |
+---------------+---------------------+------------------------+
