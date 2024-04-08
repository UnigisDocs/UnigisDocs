Circuito Operativo 
==================
.. container:: justified-text

  UNIGIS TMS ofrece una amplia gama de circuitos operativos que se adaptan a las necesidades y el tipo de negocio de cada usuario. Estos circuitos pueden variar desde simples rutas punto a punto hasta circuitos operativos más complejos. En UNIGIS TMS, cada circuito es completamente configurable, lo que permite a los usuarios ajustarlos según sus requisitos específicos.

  Un circuito operativo describe un flujo de operaciones punto a punto desde la entrada de datos hasta la entrega final. Aquí se proporciona un ejemplo muy estándar abarcando partes principales de la solución UNIGIS TMS:

.. image:: cop.png
    :align: center

|assignment_light| |assignment_dark| Administración de Pedidos y Órdenes
------------------------------------------------------------------------
.. raw:: html

   <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Symbols+Outlined">

.. |assignment_light| raw:: html

    <span class="material-symbols-outlined">
    assignment
    </span>

.. |assignment_dark| raw:: html
    
    <span class="material-symbols-outlined dark-mode-icon" style="display: none;">
    assignment
   </span>

.. raw:: html

   <script>
     if (document.documentElement.classList.contains('theme-dark')) {
       document.querySelector('.light-mode-icon').style.display = 'none';
       document.querySelector('.dark-mode-icon').style.display = 'inline';
     } else {
       document.querySelector('.light-mode-icon').style.display = 'inline';
       document.querySelector('.dark-mode-icon').style.display = 'none';
     }
   </script>

.. container:: justified-text

  Dentro de UNIGIS TMS cuenta con una herramienta para la gestión de pedidos, automatiza todo el proceso de gestión de pedidos. Permite gestionar la información de inventario, depósitos, ventas y clientes en un solo lugar, para que puedas acceder fácilmente a todos estos datos desde cualquier lugar y en cualquier momento.

  Order Management tiene la capacidad de integrar y gestionar todos los pedidos de venta de diferentes portales colaborativos (ERP, CRM, WMS, entre otros) que utiliza una empresa para delivery y pedidos. Los administra en un sistema centralizado que permite ajustar las fechas de entrega comprometidas, realizar particiones y consolidaciones, geo codificar y normalizar las direcciones, hasta generar las órdenes de entrega, trabajo o servicio, que requiere la logística de distribución

.. image:: Imagen7.png
    :align: center

|location_on_light| |location_on_dark| Planeación y Transporte (Routing)
------------------------------------------------------------------------

.. |location_on_light| raw:: html

    <span class="material-symbols-outlined">
    location_on
    </span>

.. |location_on_dark| raw:: html
    
    <span class="material-symbols-outlined dark-mode-icon" style="display: none;">
    location_on
   </span>

.. container:: justified-text

  Dentro de UNIGIS TMS se encuentra el módulo “Routing”, una herramienta de planeación de rutas de forma automática o manual y todo lo correspondiente para la aprobación de un pedido dentro de una jornada establecida de recolección y entregas.

  Dentro del módulo de “Routing” se configura por jornadas de recolección/entrega, dentro de un día se pueden tener varias jornadas, se entienden como tipo de jornadas de planeación. Se puede visualizar datos importantes de la jornada, como el número de órdenes y los clientes correspondientes que contienen para planificar la ruta, de igual manera nos permite crear una nueva jornada.

  Cuenta con la funcionalidad de por cada jornada el usuario pueda planificar rutas de entrega/recolección.  
  Se visualiza la opción “Planeación” con la jornada previamente seleccionada.

  Dentro de la planificación se pueden visualizar datos importantes como direcciones de la orden, vehículos, horarios, etc. para la geo codificación de la ruta.

.. image:: Imagen8.png
    :align: center

|desktop_windows_light| |desktop_windows_dark| Tendering
---------------------------------------------------------

.. |desktop_windows_light| raw:: html

    <span class="material-symbols-outlined">
    desktop_windows
    </span>

.. |desktop_windows_dark| raw:: html
    
    <span class="material-symbols-outlined dark-mode-icon" style="display: none;">
    desktop_windows
   </span>

.. container:: justified-text

  UNIGIS TMS contiene un portal del transporte que permite publicar a tus transportistas terceros previamente registrados las rutas que deseas cubrir para que acepten la oferta y asignen el vehículo que necesitas. Permite conocer la mejor rentabilidad de servicio en los viajes según su categoría. 

  Las empresas de transporte o conductores pueden acceder al portal de transporte y visualizar la oferta en tiempo real de las rutas publicadas por el dador de carga, este a su vez puede visualizar la oferta para la optimización de las rutas de transporte, en base a evaluaciones (tender) control de rutas planificadas y optimizadas (routing) y reducción de kilómetros y uso de vehículos con comunicación en tiempo real con empresas transportistas si parte de la flota o el total se encuentra tercerizado a través del portal del transporte.

.. container:: justified-text

  Al seleccionar una empresa de transporte permite gestionar los viajes, como transportista permite ver la oferta como información importante de la ruta y carga del vehículo, los viajes ya ofertados por el conductor, agregar observaciones de la oferta, rechazar o aceptar la oferta del viaje según parámetros configurados.

  Al aceptar la oferta, el dador de carga puede visualizar información importante como documentación de la placa, conductor y registros adicionales. Registrar el arribo del camión al deposito de salida, validar accesos y verificación del vehículo para la confirmación del viaje.

.. image:: Imagen9.png
    :align: center

|garage_home_light| |garage_home_dark| Yard Management
-------------------------------------------------------

.. |garage_home_light| raw:: html

    <span class="material-symbols-outlined">
    garage_home
    </span>

.. |garage_home_dark| raw:: html
    
    <span class="material-symbols-outlined dark-mode-icon" style="display: none;">
    garage_home
   </span>

.. container:: justified-text

  Dentro de Home de UNIGIS TMS se muestra el módulo “Yard Management” ubicado en el menú lateral. Con el módulo “Yard Management” permite administrar la ocupación de los muelles, el usuario podrá asignar viajes en determinados estados a las cortinas disponibles y las cuales se visualizarán gráficamente a través de colores. Adicionalmente es posible configurar estados como ocupada, disponible, en mantenimiento y según el estado permitirá asignar un viaje a una cortina o no. También administra alertas para los casos en que el vehículo supera el tiempo de carga establecido, las notificaciones se pueden visualizar en UNIGIS o se pueden enviar por correo electrónico.

  Mientras el vehículo se encuentra en viaje activo el área de torre en control, le darán seguimiento al viaje mediante:
  - Visualización personalizada por transporte, por viaje o una vista general de la jornada actual.
  - Permite consultar el estado de la conexión, el detalle del tiempo transcurrido y las ultimas actualizaciones de los viajes.
  - Consultar Información general, por ejemplo, tiempos de planificación contra el tiempo real, detalles del vehículo, velocidad, detalle de los productos a entregar, información del viaje, paradas y alarmas.
  - Los clústeres representan un grupo de vehículo o paradas. Estos se pueden habilitar o deshabilitar para ver el detalle de sus estados por grupo.
  - Puede controla en tiempo real la ejecución de las entregas visualizando los estados de las paradas del viaje.
  - Configuración de notificaciones automáticas por medio de WhattApp, SMS o correo electrónico con el detalle que se requiera compartir dependiendo del estado del pedido.
  - Entre otras.

.. image:: Imagen10.png
    :align: center

|local_light| |local_dark| Smart Tracking (Monitoreo Logístico)
---------------------------------------------------------------

.. raw:: html

   <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

.. |local_light| raw:: html

    <span class="material-icons">
    local_shipping
    </span>

.. |local_dark| raw:: html
    
    <span class="material-icons dark-mode-icon" style="display: none;">
    local_shipping
    </span>

.. container:: justified-text

  En la pantalla inicial de UNIGIS TMS se muestra el módulo “Tracking” ubicado en el menú lateral. El módulo “Tracking” es una herramienta para realizar el monitoreo logístico prevista del plan de distribución y la entrega de productos en tiempo real, se integra con todos los dispositivos móviles y GPS instalados en sus propios vehículos o con servicios de transportes tercerizada. Valida en tiempo real que se cumplan las rutas planeadas, los horarios de visitas y las entregas finales. Permite la configuración de alertas personalizadas y mensajes en el momento que ocurren para la toma de decisiones.

.. image:: Imagen11.png
    :align: center

|phonelink_ring_light| |phonelink_ring_dark| Confirmación de Entregas (POD) y Movilidad
---------------------------------------------------------------------------------------

.. |phonelink_ring_light| raw:: html

    <span class="material-symbols-outlined">
    phonelink_ring
    </span>

.. |phonelink_ring_dark| raw:: html
    
    <span class="material-symbols-outlined dark-mode-icon" style="display: none;">
    phonelink_ring
   </span>

.. container:: justified-text

  UNIGIS ofrece un conjunto de aplicaciones móviles para colaborar en la gestión de la distribución y ofrecer un mejor servicio a los clientes. La aplicación de confirmación de entregas (POD) permite informar en tiempo real si la entrega es efectiva junto con las evidencias de la firma electrónica, scan de productos y documentos, fotos, encuestas de satisfacción, contactless, entre otros beneficios. Ofrece al operador la mejor ruta de llegada a destino considerando el tránsito de la ciudad en cada momento.

.. image:: Imagen25.png
    :align: center

|request_quote_light| |request_quote_dark| Finalización y Tarifación de viajes
------------------------------------------------------------------------------

.. |request_quote_light| raw:: html

    <span class="material-symbols-outlined">
    request_quote
    </span>

.. |request_quote_dark| raw:: html
    
    <span class="material-symbols-outlined dark-mode-icon" style="display: none;">
    request_quote
   </span>

.. container:: justified-text

  UNIGIS TMS cuenta con un módulo “Tarifas” para la finalización y liquidación de sus viajes, puede tarifar desde el inicio del o hasta la entrega final de los productos al cliente, incluyendo la liquidación del transporte con sus tarifas y costos, documentos oficiales, tipos de ventas, customización de tarifas y todos los procesos operativos necesarios. Ofrece visibilidad y trazabilidad end-to-end del estado de los pedidos, viajes y entregas, desde la planeación inicial y hasta la ejecución final junto con todas las evidencias que ocurren durante el proceso. Opera en forma conjunta con los diferentes portales colaborativos (ERP, CRM, WMS, otro) Permite crear fácilmente los reportes, estadísticas e indicadores estratégicos del negocio se requiere.

  Al momento de la finalización de la parada o el viaje permite al monitoreo dejar de visualizarlo dentro del mapa como activo, es cuando entra la rendición del viaje. Al finalizar el viaje el usuario puede customizar los estados y alertas que aplicara para la llegada o rendición de viaje, presentar remitos de conformidad, hojas de viaje, sellos, incidencias económicas y gestión de productos no entregados, en caso de que no finalizar un viaje correctamente el sistema cuenta con estados para visualizar el viaje a parcialmente rendido para el seguimiento de este.

  El sistema genera para cada empresa de transporte cada liquidación de costo en estado inicial. Será posible hacer ajustes por incidencias.

.. image:: Imagen12.png
    :align: center

.. raw:: html

   <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Symbols+Outlined">
