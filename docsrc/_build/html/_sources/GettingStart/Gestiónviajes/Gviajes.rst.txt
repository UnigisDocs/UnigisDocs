Gestión de Viajes
==================

.. figure:: Imagen19.png
   :align: left

Conceptos Básicos
------------------

.. container:: justified-text

    La gestión del viaje y transporte implica la administración, planeación, control y cierre de servicios de distribución. Se basa en objetivos y procesos bien definidos dentro de la logística empresarial, lo cual influye en los beneficios que una compañía puede obtener en esta área. Es crucial mantener un control efectivo en cada etapa del proceso. Por eso, muchas empresas optan por implementar soluciones TMS que gestionen integralmente flotas y transportes.

    En este contexto, es útil comprender los aspectos relacionados y principales de la planificación de rutas en UNIGIS TMS para administrar, conocer, analizar y utilizar la siguiente información:

    Ruta:

    En UNIGIS TMS, una ruta es un trayecto planificado y optimizado que un vehículo de transporte asignado recorrerá para realizar un viaje específico, pasando por paradas o entregas programadas.

    Viaje:

    El viaje se refiere a la ejecución del servicio planificado para el vehículo de transporte, desde un punto de origen hasta un destino específico. Su objetivo principal es realizar las entregas programadas, y contiene todos los datos relacionados con la ruta para garantizar una optimización exitosa del viaje.

    Parada:

    Una parada es un punto específico a lo largo de la ruta planificada donde el vehículo de transporte realiza una acción, como carga o descarga de productos, recolección de mercancías u otras tareas específicas. Las paradas son parte integral de la ruta establecida y son fundamentales para optimizar la eficiencia del proceso de entrega y cumplir con las promesas de entrega.

Entidades
---------

.. container:: justified-text

    Para planificar una solicitud de transporte, es necesario crear una estructura base, configurar catálogos y establecer la transacción de datos para una nueva orden de ruta. Se debe configurar las entidades relacionadas con los flujos de trabajo de jornadas, órdenes y rutas antes de iniciar la operación.

    Una vez establecido el pedido o solicitud de transporte, se pueden determinar la cantidad de órdenes necesarias. Estas órdenes están asociadas a una única jornada, operación y fechas debido a la naturaleza del pedido. En la planificación, no se asigna un vehículo específico, sino que se planifica con un tipo de vehículo disponible en un depósito correspondiente a una operación, considerando las características específicas de la ruta, jornada y orden para cumplir con el objetivo del domicilio de la orden.

.. figure:: entidades.png
   :align: center

Gestión de Viajes
------------------

.. container:: justified-text

    El módulo de gestión de viajes y paradas facilita la publicación de rutas a tus transportistas terceros previamente registrados. Estas rutas pueden ser aceptadas por los transportistas, asignando vehículos y conductores de manera eficiente, considerando la disponibilidad, habilidades y restricciones de cada recurso. El módulo de Tendering puede ayudar en esta asignación de manera automática o sugerir opciones óptimas, permitiendo conocer la rentabilidad del servicio en los viajes según su categoría.

.. image:: Imagen2.png
    :align: Center
    :width: 400px
    :height: 250px

Portal B2B (business-to-business)
----------------------------------

.. container:: justified-text

    El portal de transporte B2B, se promueve la colaboración entre diversos actores del sector con el objetivo de mejorar la eficiencia y la oferta de servicios. Para ello, se brindan herramientas e información a los servicios de transporte tercero, permitiéndoles ofertar viajes de acuerdo a sus capacidades y especialidades.

    Estos servicios de transporte externos pueden acceder a una plataforma donde visualizan los viajes ofertados, aquellos disponibles y los que ya están en curso. Una vez que se asigna un viaje, el conductor dispone de toda la información necesaria para llevar a cabo el transporte de manera fluida. Esto incluye detalles como las paradas del viaje, los ítems correspondientes a cada parada, así como la ruta a seguir. Todas estas configuraciones y permisos son proporcionados por el usuario del producto, garantizando un control total sobre el proceso.

.. image:: Imagen5.png
    :align: Center

.. container:: justified-text

    Las empresas de transporte o conductores pueden acceder al portal de transporte para visualizar la oferta en tiempo real de las rutas publicadas por el dador de carga. A su vez, el dador de carga puede visualizar la oferta para optimizar las rutas de transporte, basándose en evaluaciones (Tendering), control de rutas planificadas y optimizadas (Routing), y reducción de kilómetros y uso de vehículos. Esto se realiza mediante comunicación en tiempo real con empresas transportistas, ya sea que parte de la flota o la totalidad se encuentre tercerizada a través del portal del transporte.

.. container:: justified-text

    Al seleccionar una empresa de transporte, se permite gestionar los viajes. Como transportista, puedes ver la oferta, que incluye información importante sobre la ruta y la carga del vehículo, así como los viajes ya ofertados por el conductor. Además, puedes agregar observaciones a la oferta y aceptarla o rechazarla según los parámetros configurados. 

.. image:: Imagenb2b.png
    :align: center

.. container:: justified-text

    Una vez aceptada la oferta, el dador de carga puede acceder a información importante, como la documentación de la placa, del conductor y otros registros adicionales. El registro del arribo del camión al depósito de salida, la validación de accesos y la verificación del vehículo permiten validar los documentos necesarios para el arribo y confirmación del viaje y transporte. Esto garantiza el cumplimiento normativo y reduce el riesgo de problemas legales.
    
    Maximizar la eficiencia del espacio de carga y reducir los costos asociados puede lograrse mediante la optimización de las cargas, considerando la capacidad y las características específicas de los vehículos.

Yard Management
-----------------

.. container:: justified-text
    
    Dentro del módulo de Yard, se lleva a cabo una gestión integral de los muelles y depósitos de manera visual, aprovechando todas las características disponibles. Cada muelle cuenta con su propio calendario que muestra ocupaciones y reservas generadas de forma automatizada, facilitando una visión clara de la disponibilidad. Además, se ofrece una página inteligente para cada muelle, proporcionando detalles cruciales.

    Para los depósitos, se dispone de una visualización completa de sus características y disponibilidad, incluyendo geocercas individuales, y se muestra información detallada sobre los vehículos alojados en cada uno.

.. image:: yardimagen.png
    :align: center

.. container:: justified-text

    Cuando se selecciona un vehículo, se accede a toda la información relevante, como la del conductor, viajes asignados, carga, ítems y otros datos importantes. También se ofrecen detalles sobre las salidas, fechas de entrada y salidas, facilitando una navegación clara y precisa.

    La gestión de los muelles puede realizarse de manera manual o automática. En el primer caso, se permite la gestión por entradas o salidas, búsqueda por clientes, visualización de disponibilidad por fechas, optimización de asignaciones por viajes próximos, y visualización de advertencias o riesgos. Se proporciona información crucial sobre el conductor y los permisos necesarios para las operaciones en el depósito, entre otras funciones.

    En el proceso automático, se incluye la planeación de rutas, donde las solicitudes pueden ser confirmadas o ignoradas según la gestión requerida. Cada opción se integra en un workflow configurado, lo que permite cambios automáticos de estado según las acciones realizadas dentro del yard, manteniendo así un flujo de trabajo actualizado en todo momento. Por ejemplo, cambios de estado pueden ocurrir al momento de entrada al depósito, descarga, salida del vehículo, manejo de documentación, entre otros procesos.

.. image:: Imagen6.png
    :align: Center

.. container:: justified-text

    Una vez el transporte sale del deposito se puede realizar un monitoreo detallado de las asignaciones que han sido ruteadas en función del inventario predefinido dentro del módulo de Tracking. Esta funcionalidad permite una supervisión precisa y en tiempo real de las operaciones en curso, facilitando la toma de decisiones y la gestión eficiente de los recursos disponibles.

Workflows
----------
.. container:: justified-text

    Cada entidad en el producto UNIGIS TMS dispone de sus flujos de trabajo, los cuales pueden ser implementados para gestionar tareas recurrentes, como la confirmación de entregas, la actualización de información y la comunicación con los conductores. Esto resulta en una reducción de la carga administrativa y una mejora en la eficiencia operativa.

Automatización de Procesos
---------------------------

.. container:: justified-text
    
    La entidad tiene como objetivo la configuración de acciones o transiciones para la creación de procesos automatizados. Estas acciones o transiciones pueden configurarse antes o después de un cambio de estado, o cuando se elimina un pedido, de manera distribuida, sincrónica o temporal. Esto permite configurar y adaptar UNIGIS TMS a cualquier tipo de operación, utilizando un catálogo de métodos establecidos o personalizados, y especificando cómo se ejecutan en cada operación o tipo de jornada.

    Por ejemplo, cuando una entidad de tipo "Pedido" cambia de estado de "Ingresado" a "Aprobado", el método que se ejecuta es el de crear una orden a partir de ese pedido. La entidad de orden realiza el proceso de planificación correspondiente. De esta manera, cuando la entidad de viaje toma esa transición, cambia su estado a "Confirmado" para dar inicio al arribo del vehículo al depósito. Estas acciones pueden realizarse fuera de la transición o de manera temporal, indicada por un comando crontab. Además, se permiten validaciones y condiciones para garantizar que el proceso se cumpla entre entidades.

UNIGIS X DELIVERIES
--------------------

.. container:: justified-text

    UNIGIS X DELIVERIES proporciona capacidades de seguimiento en tiempo real dentro de UNIGIS TMS para monitorear la ubicación y el progreso de los vehículos durante los viajes mediante flujos de trabajo configurados por estados. Esto facilita la toma de decisiones rápidas en caso de desviaciones o problemas durante el viaje.

    La aplicación móvil muestra un enlace asignado para el viaje del conductor, donde puede visualizar los viajes disponibles del día y la información general de la jornada, así como detalles de las paradas, tanto de servicio como de control o mantenimiento, todo configurable según las necesidades del negocio.

    La aplicación móvil también cuenta con un QR CARD configurable para cada interacción que desee aplicar. Por ejemplo, para control de carga, entradas y salidas de vehículos, inicio de jornadas, documentación, estados de flujo de trabajo, firmas, entre otras interacciones. Los permisos determinan qué acciones puede realizar el usuario en la gestión de viajes.

.. image:: Imagen3.png
    :align: Center
    :width: 250px
    :height: 400px

.. container:: justified-text

    Una vez que el conductor acepta la jornada, la aplicación proporciona detalles sobre las paradas en su ruta. Puede usar la función de navegación integrada con Waze o Google Maps para dirigirse a la próxima parada, consultar los productos a entregar y comunicarse con el cliente en caso necesario.

    Durante el viaje, se pueden realizar diversas acciones, como mensajería en tiempo real, llamadas a la torre de control y cambio de estados de recursos, entre otras.

    Para la entrega y confirmación, una vez que el conductor llega a la dirección de entrega, completa la entrega y puede marcarla como finalizada en la aplicación. Esto notifica a la plataforma y al cliente que el pedido ha sido entregado con éxito. En caso de una entrega parcial, el conductor puede seleccionar el estado correspondiente y proporcionar una breve descripción con evidencia del motivo.

    UNIGIS X DELIVERIES es una aplicación configurable para la gestión y monitoreo de viajes que se adapta a cualquier tipo de entrega. Integra flujos de trabajo configurados y se ajusta a los permisos y seguridad de cada usuario. En ausencia de conexión a internet, guarda los datos offline hasta el próximo punto de conexión, incluyendo evidencias, encuestas y códigos QR con opciones configurables.

.. image:: Imagen26.png
    :align: center
    :width: 300px
    :height: 400px

 