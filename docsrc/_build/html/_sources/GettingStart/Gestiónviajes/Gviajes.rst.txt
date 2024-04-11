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

Workflows
----------
.. container:: justified-text

    Cada entidad en el producto UNIGIS TMS dispone de sus flujos de trabajo, los cuales pueden ser implementados para gestionar tareas recurrentes, como la confirmación de entregas, la actualización de información y la comunicación con los conductores. Esto resulta en una reducción de la carga administrativa y una mejora en la eficiencia operativa.

Automatización de Procesos
---------------------------

.. container:: justified-text
    
    La entidad tiene como objetivo la configuración de acciones o transiciones para la creación de procesos automatizados. Estas acciones o transiciones pueden configurarse antes o después de un cambio de estado, o cuando se elimina un pedido, de manera distribuida, sincrónica o temporal. Esto permite configurar y adaptar UNIGIS TMS a cualquier tipo de operación, utilizando un catálogo de métodos establecidos o personalizados, y especificando cómo se ejecutan en cada operación o tipo de jornada.

    Por ejemplo, cuando una entidad de tipo "Pedido" cambia de estado de "Ingresado" a "Aprobado", el método que se ejecuta es el de crear una orden a partir de ese pedido. La entidad de orden realiza el proceso de planificación correspondiente. De esta manera, cuando la entidad de viaje toma esa transición, cambia su estado a "Confirmado" para dar inicio al arribo del vehículo al depósito. Estas acciones pueden realizarse fuera de la transición o de manera temporal, indicada por un comando crontab. Además, se permiten validaciones y condiciones para garantizar que el proceso se cumpla entre entidades.

 