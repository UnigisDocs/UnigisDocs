Smart Planning
==============================

Descripción 
--------------

.. container:: justified-text

    El siguiente documento tiene como objetivo proporcionar información técnica, describir la funcionalidad paso a paso, así como ofrecer una descripción detallada y organizada. Esta guía está diseñada para ser comprensible en todos los niveles y tener la información disponible para su uso en cualquier momento que pueda ser de utilidad.

Permisos
---------

Crear Usuario
~~~~~~~~~~~~~~~~~~~~~

.. container:: justified-text

    Para acceder al módulo de Routing, el administrador debe dirigirse a :kbd:`AdministracióndelSistema` --> :kbd:`Seguridad` --> :kbd:`Usuarios`.

    Al ingresar, se debe visualizar un listado de usuarios registrados. Para agregar un nuevo usuario, es necesario hacer clic en el botón Crear :kbd:`+` y completar los campos respectivos.

.. image:: Usuario.png
   :align: center
   :width: 480px
   :height: 520px

Permisos de Grupo
~~~~~~~~~~~~~~~~~~~~~

.. container:: justified-text
    
    Lo siguiente es que el usuario cuente con los permisos necesarios esto se realiza dentro de :kbd:`AdministracióndelSistema` --> :kbd:`Seguridad` --> :kbd:`Grupos`.

    Al ingresar, debe visualizar un listado de los grupos con los que se cuenta actualmente. Para conceder permisos al usuario registrado previamente, debe hacer clic en el botón "Crear" :kbd:`+` y seleccionar la pestaña de Usuarios.

.. image:: Grupo.png
   :align: center
   :width: 480px
   :height: 520px

Funcionalidad
---------------

.. container:: justified-text

    Como usuario del módulo de Routing en el TMS de UNIGIS, primero debe iniciar sesión con el usuario y la contraseña registrados en el administrador de sistema. Una vez dentro, puede acceder al módulo de Routing.

.. container:: justified-text

    Dentro del módulo, encontrará las secciones de Jornadas, Planeación y Catálogos. Para realizar ajustes clave para su empresa, es necesario ingresar a una jornada. Esto se puede hacer dando doble clic en una jornada del listado o haciendo clic en el botón :kbd:`Planificar`.

    Una vez dentro de una jornada, verá datos relacionados con Rutas, Órdenes, Consolidados y Consultas. Si desea una configuración personalizada, puede hacer clic en el botón :kbd:`ajustes` ubicado en la parte inferior izquierda.

.. image:: config.png
   :align: center

Configuración de Datos Generales 
----------------------------------

``General``
-------------

Modo de Ruteo
~~~~~~~~~~~~~~~

Indica el modo en que se realizará el ruteo, puede ser:

- Ruteo por Ordenes: Ruteará Ordenes de manera individual.
- Ruteo por Consolidados: Rutea una agrupación de Ordenes Parada. Este modo requiere ejecutar previamente el proceso de "Consolidación de Ordenes".

Restricción Ambiental
~~~~~~~~~~~~~~~~~~~~~~~

Restringe configuraciones de ruteo por Normativas Ambientales, puede ser:

- Default: No aplica restricciones ambientales.
- Normativa Europea: Contempla los tiempos de conducción y descansos en las rutas según la Normativa Europea (Reglamento (CE) N.º 561/2006).

Opciones
~~~~~~~~~~

.. container:: justified-text

    Visualización de Trayectos: Es el modo en que se visualizan los trayectos generados, puede ser:
    
    - Sin Líneas: No Muestra trayectos.
    
    - Por Calles: Muestra los trayectos según la red de viales.
    
    - Lineal: Muestra los trayectos de forma directa.
  
    Cálculo de Distancias: Modo en que se calculan las distancias de las rutas, puede ser:
  
    - Por Calles: Distancia entre Ordenes contemplando la red de viales.
  
    - Lineal: Durante la construcción y optimización de rutas, se consideran distancias lineales entre Ordenes.
  
    - Máxima Precisión: Calcula las distancias entre Ordenes por calles con mínimo error.
  
    - Lineal - Manhattan: El cálculo de distancia se compone de la suma de las diferencias absolutas de las coordenadas entre dos puntos. 

    Mapa Optimizado: Opción para que en mapa se muestre solo el detalle necesario, optimizando tiempos de carga en la renderización de los mapas a utilizar. Los trayectos de las rutas se visualizarán solo al abrir el detalle de cada ruta, mostrándose inicialmente solo los puntos de ubicación de las Ordenes.

    Contemplar Hora Actual: Para creaciones de ruta que se están planificando en el mismo día de la Jornada, la hora de inicio de estas será superior a la hora actual de ruteo. Tener en cuenta que el horario de inicio se fija al momento de rutear, para extenderlo utilizar "Diferencia temporal".

    Diferencia Temporal: Indica cuantos minutos posteriores a la "Contemplación de Hora actual" podrán inicializar las rutas nuevas.

Depositos
~~~~~~~~~~~

.. container:: justified-text

    Automáticos: Para el ruteo se utiliza como Depósitos de Salida y Llegada los configurados en las Ordenes (entidad Orden, campos DepositoSalidaIN y DepositoLlegadaIN) y no el informado en el ruteo automático (Zona). De esta manera nunca se "mezclarán" Ordenes con distintos Deposito de Salida o Llegada en una misma ruta.

.. note::
    
    Tener en cuenta que, de no encontrarse seleccionado, el ruteo utilizará como Depósitos de Salida y Llegada el informado en el ruteo automático (Zona).

.. container:: justified-text

    Omitir el uso de Muelles: Ejecuta el ruteo sin considerar Muelles de Carga.

    No dibujar salida ni llegada: No dibuja en el mapa los trayectos desde el Depósito de Salida a la primer Orden ni del de la última al Depósito de Llegada. Sin embargo, los tiempos y distancias correspondientes si son considerados.

    Omitir el Uso de Muelles de Llegada: Ejecuta el ruteo sin considerar Muelles de Descarga.

    Ignorar Actividades de Muelles: No toma en cuenta las ocupaciones previas (viajes, rutas o actividades) de los Muelles al generar un nuevo ruteo automático.

    Tiempos Precalculados:Se contempla durante el ruteo los tiempos precargados en minutos de los registros manuales seteados en la entidad DistanciaRelacion. Dichos tiempos de ruta preestablecidos son únicamente entre Depósito de Salida y las Ordenes, pudiendo ser configurados según Operación, TipoPedido y CategoríaPedido (utilizándose el que mejor machee considerando estos tres campos, en caso de existir más de uno).

    Ignorar los Turnos de los Depósitovs: No se toma en cuenta la Capacidad Operativa de los Depósitos al momento de rutear. Es decir, las ventanas horarias que poseen los Depósitos para operar, en función del día y la franja horaria disponible.

    Concatenar Depósitos: Priorizar el ruteo de Ordenes por dos oleadas, primeramente, se ruteará bajo la condición Depósitos Automáticos.
    
    Luego, al quedar Ordenes sin rutear que pertenecen a distintos Depósitos, el algoritmo anula la condición de Depósito Automático y permite rutear las Ordenes remanentes en conjunto. Para que el mismo se encuentre habilitado debe encontrarse seteado el check "Depósitos Automáticos".

Vehículos
~~~~~~~~~~

.. container:: justified-text

    Origen: Indica el origen de los datos asociados Tipo de Vehículo, puede ser:

    - Default: Utiliza los datos del Tipo de Vehículo.
    
    - Operación: Modifica los datos de los Tipos de Vehículo para una Operación en particular (Entidad OperacionTipoVehiculo).
   
    - Zonas: Modifica los datos de los Tipos de Vehículo para una Zona en particular (Entidad ZonaTipoVehiculo).

.. note::

   Tener en cuenta que el Producto siempre rutea por Tipo de Vehículo.

.. container:: justified-text

    Asiganación Automática: Asigna, luego de realizar el ruteo, un Vehículo a la ruta según el Tipo de Vehículo utilizado. Se considera únicamente los Vehículos asociados a la Operación (entidad VehiculoDisponible).

    Utilizar Flotas por Jornada: Permite utilizar una lista específica de Vehículos disponibles para trabajar en la jornada (estado Activo), seleccionándolos a partir de la “Lista de vehículos”. Tener en cuenta que el ruteo solo considera dicha cantidad de vehículos. A su vez permite actualizar la cantidad de Vehículos mediante el Método “Actualizar Vehículos”.

    Lista de Vehículos: Permite mostrar el detalle total de Vehículos disponibles, pudiendo seleccionar aquellos con los que se desea trabajar en la Jornada.

    Mímimos de Tipo: Permite que se contemplen las mínimas capacidades operativas en los Tipos de Vehículo (Volumen, Peso, Pallets y Bultos).

    Tiempos de Inactivadad: Indica que se respete la parada de descanso.

    Respetar Actividades: Rutea con los Vehículos disponibles respetando la agenda o disponibilidad real (viajes, ruta o actividades).

    Usar Ventana Horaria: Respeta el Inicio Horario y Fin Horario del Tipo de Vehículo al momento de rutear.

    Máximos Según Grupos: Setea la cantidad de vehículos a utilizar en función de las demandas máx

    Utilizar flotas de Operación: Permite utilizar una lista específica de Vehículos disponibles para trabajar en operación seleccionándolos en la “Lista de vehículos”.

    Lista de Vehículos: Si se utiliza Flotas por operación, esta funcionalidad permite tener disponible Vehículos.

Ordenes
~~~~~~~~~~~~~~

.. container:: justified-text

    Carga Exclusiva: Permite que las Ordenes (o un Consolidado) sean ruteados de manera única en la Ruta, es decir que el Vehículo solo se utiliza para transportar esta carga. Deben tener seteado el campo "Carga Exclusiva".

    Segunda Ventana Horario: Permite utilizar para el ruteo ambas Ventanas Horarias seteadas en las Ordenes (InicioHorario1 / FinHorario1 y InicioHorario2 / FinHorario2).

    Prioridad Absoluta: Prioridad de rutear dicha Orden frente a las otras de menor prioridad en la misma Jornada. No garantiza su ruteo.

    Prioridad: Prioridad relativa de secuencia entre Ordenes dentro de la misma ruta, buscando jerarquizar el orden de las Ordenes en la Ruta. El valor 1 indica la Prioridad mayor, mientras que el 999 la menor.

    Grupo Rutas: Garantiza formar rutas con Ordenes de un mismo Grupo. Se setea en Grupo de Rutas informado en la Orden.

    Grupo Rutas Inclusivo: Ídem Grupo Rutas con la particularidad que los que posean valor 0 pueden agregarse en cualquier otro Grupo.

    Última Visita: Fuerza que las Ordenes que posean el campo activo "Ultima Visita" se asignen en la última posición de la Ruta. En caso de que existan más de una Orden con dicho seteo, las mismas se rutearán en rutas distintas a menos que se encuentren en un mismo Consolidado.

    Agrupación en Ruta: Busca realizar una Consolidación de manera dinámica mientras se rutea, consolidando Ordenes que se encuentran en el mismo Domicilio-Orden quedando así visitados a la misma hora.

    Ignorar Tipo de Entrega: No se considera el Tipo de la Orden al generar las rutas. Todas se consideran como Ordenes Tipo "Entregas".

    Comtemplar Pólizas: Habilita el control de Pólizas de seguros al momento de rutear, tal que se sumarice el valor transportado, a partir de los Valores Declarados en las Ordenes, siendo el Rlímite el permitido en la/s Pólizas (del cliente Dador de la orden) de la Ruta.

.. note::

    Se valida que no se supere el valor máximo a transportar por cada Póliza, por lo que cada Cliente deberá tener una Póliza asignada al momento de utilizar la funcionalidad. Finalmente, una Ruta puede tener N Pólizas, siempre y cuando no se supere el "TopLimite" de la misma.

.. container:: justified-text

    Máximas en Ruta: Limita la saturación de la Ruta por la capacidad máxima informada en la Orden (Bultos máximos en Ruta, Pallets máximos en Ruta, Peso máximos en Ruta, Volumen máximos en Ruta).

    Contemplar Cuentas: Permite modificar el comportamiento de la validación de las Pólizas. Al momento de generar las rutas se valida el valor de la Póliza asignada a una determinada Cuenta y no por Cliente. Para ello se requiere que en la Póliza se encuentre la Cuenta a la cual pertenece y se aplicará aquella Póliza que contenga la misma cuenta que tenga la Orden.

    Utilizar Depósitos PickUps: Una vez realizada la importación de datos a través de la Jornada y previo al ruteo, el sistema automáticamente genera (según lo indicado en el IdDeposito del Pedido o sus PedidoItems) la creación de las nuevas Ordenes (Depósitos Pickups o Auxiliares Auto creadas) a las que debe concurrir para realizar la entrega. Dichas “Ordenes” son ficticias y se generan de manera automática, asegurándose la recolección en cada Depósito, para luego realizar la Entrega de estos.

    Respetar Vehículo Pre Asignado: Agrupa las Ordenes con la pareja Conductor/Vehículo preasignado en el Pedido, haciendo con ellos una ruta forzando a su creación.

``Consolidación``
------------------

.. image:: consolidados.png
   :align: center

Opciones
~~~~~~~~~~~~~

.. container:: justified-text

    Ventana Horaria: Busca definir la ventana horaria que será utilizada en el Consolidado, puede ser:
    
    - Ventana Más Amplia: Utiliza como ventana horaria del Consolidado, la ventana horaria más amplia de las Órdenes que posee.
    
    - Ventana Más Restrictiva: Utiliza como ventana horaria del Consolidado, la ventana horaria menos amplia de las Órdenes que posee.

    Tiempo De Espera: Define el Tiempo de Espera que será utilizado el Consolidado (Ordenes Parada), puede ser:
   
    - Sumar Tiempos De Espera: El Tiempo de Espera del Consolidado es igual a la suma los Tiempos de Espera de cada Orden que contiene. 
    
    - Promediar Tiempos De Espera: El Tiempo de Espera del Consolidado es igual al promedio de los Tiempos de Espera de las Ordenes que se contienen. 
    
    - Máximo Tiempo De Espera: El Tiempo de Espera del Consolidado es igual al mayor Tiempo de Espera de la Orden que contienen.

    Dividir Tiempo De Espera En Ordenes: Distribuye el resultado del promedio en los Tiempos de Espera de las Ordenes que contiene, con el fin de ajustar el tiempo de estadía del Vehículo en dicho Domicilio-Orden.

    Valor 1: Primer Variable de Saturación para la Generación del Consolidado (Peso, Volumen, Bultos, Pallets, Adicional1 o Adicional2).

    Máximo Valor 1: Es el Valor Máximo que Soporta el Consolidado para la Primer Variable de Saturación Informada.

    Valor 2: Segunda Variable de Saturación para la Generación del Consolidado (Peso, Volumen, Bultos, Pallets, Adicional1 o Adicional2).

    Máximo Valor 2: Es el Valor Máximo que Soporta el Consolidado para la Segunda Variable de Saturación Informada.

    Reglas De Generación: Determina la Regla de Cercanía entre las Ordenes para su consolidación, puede ser:

    - Ubicación Exacta: Se agrupan todas las Órdenes que poseen las mismas coordenadas geográficas (Radio de error: 5 metros ).
    
    - Esquina: Se realiza la consolidación de todas las Órdenes que se encuentren en un radio definido por Distancia máxima (en metros) siendo el punto de llegada un VERTICE GEOGRÁFICO (Esquina).
    
    - Cercanía: Se realiza la consolidación de todas las Órdenes que se encuentren en un radio definido por Distancia máxima (en metros), siendo el punto de llegada en CUALQUIER ESPACIO Geografía.

    Distancia Máxima (MTS): Distancia Máxima en Metros (Radio) para las reglas “ESQUINA” y “CERCANIA” que se evalúa para consolidar Órdenes cercanas entre sí, según sus coordenadas.

    Cantidad Máxima Parada: Cantidad máxima de Ordenes que pueden ser agrupados en un mismo Consolidado.

    Grupo De Consolidación: Agrupa las Ordenes (Consolida) pertenecientes al mismo Grupo de Ordenes, seteado en el campo “GrupoConsolidacion”.

    Ignorar Depósitos: Para la configuración "Depósitos Automáticos", permite anular los Depósitos seteados en los consolidados con el fin de ser agrupadas en conjunto (aunque se encuentren asignados a distintos Depósitos de Salida y Llegada).

    Contemplar Tipo De Orden: Consolida respetando el Tipo de la Orden (Tipo).

    Atributo De Ordenes: La descripción del Consolidado contiene datos de las Referencias Externas y Descripciones de las Ordenes, puede ser:

    - Primera Orden: Coloca los datos de Referencia Externa y Descripción de la primer Orden consolidada.
    
    - Concatenación De Datos: Coloca los datos concatenados de todas las Referencias Externas y Descripciones de cada Orden consolidada en la Parada."


``Escenarios``
------------------

.. container:: justified-text

    En esta pestaña, puedes realizar varias acciones relacionadas con la gestión de escenarios. Puedes crear nuevos escenarios según tus necesidades específicas, restaurar versiones anteriores de escenarios mediante la opción de reestablecer históricos, seleccionar y utilizar escenarios existentes, o eliminar aquellos que ya no necesites. Esta funcionalidad te ofrece flexibilidad para administrar tus escenarios de manera eficiente.

.. image:: Escenarios.png
   :align: center

.. container:: justified-text

    También cuenta con subpestañas que cada una cuenta con configuraciones especificas las cuales se describen a continuación:

Parámetros Generales
~~~~~~~~~~~~~~~~~~~~~~

.. container:: justified-text

    Cantidad De Interacciones: Cantidad máxima de veces que se resolverá el problema de ruteo, por distintos enfoques, para realizar la elección del resultado óptimo. Los enfoques serán de acuerdo con la combinación de heurísticas de selección de Semillas (root) y heurísticas de selección de Vehículos disponibles."

    Corte Por Tiempo (MIN): Límite de tiempo TOTAL para la ejecución de todas las iteraciones en caso de que la complejidad del ruteo implique un mayor tiempo de análisis que el deseado por el Usuario.

Radio Densidad
^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Distancia Máxima (KM): Distancia máxima desde el centro geográfico de una ruta, para buscar posibles órdenes a insertar en la misma. 

    Radio Dinámico: Permite que la herramienta defina el radio distancia que utilizará desde el baricentro geográfico de la Ruta a cada Orden, según la densidad de puntos de entrega y las Ordenes que ya se encuentren ruteadas

    Radio Escalonado: Fracciona la distancia máxima a utilizar en N escalones con el objetivo de lograr rutas más compactas geográficamente. Es una manera de jerarquizar el ruteo, y realizarlo de manera progresiva.

    Radio Local: Distancia máxima lineal entre una Orden y su siguiente/anterior.

    Radio Local Flexible: Distancia máxima lineal entre Ordenes consecutivas en un solo sentido, pudiendo ser la Orden siguiente o la Orden anterior como distancia máxima.

PickUp and Delivery
^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Modo Inverso Con Latencia: Ruteados Delivery & Pickup: Realiza primero las entregas y luego de un período de tiempo (latencia), las recolecciones en el punto anterior. 

    Pickup En Misma Ruta: Check que forza que el Delivery como el Pickup asociado se encuentren en la misma ruta. Para activarlo debe estar seteado el check "Modo Inverso con latencia".

    Validar Carga Temporal: Evita un exceso de carga del vehículo en una visita (Pallets, Peso, Volumen o Bultos)

    Analizar Corte De Pickups: Asigna la recolección en una segunda vuelta de la Ruta. Para activarlo debe estar seteado el check "Modo Inverso con latencia".

    Cantidad Máxima De Depósitos A Visitar: Es la cantidad máxima de Depósitos de los que se permite la Recolección.

    Evitar Vuelta Implícita Con Deposito Pickup: Obliga que, en caso de que las recolecciones sean en Depósitos, estos sean visitados una sola vez durante el ruteo a menos que por capacidad sea imposible de realizar. 

Parámetros Opcionales
^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Considerar Barreras: Contemplar las demoras generadas por las barreras en el cálculo de tiempos. 

    Omitir Retorno Al Deposito: No se contabilizan tiempos ni distancias desde la última Orden al Depósito de llegada.

    Considerar Áreas: Habilita el CrossDock dinámico durante el ruteo

    Depósito De Salida Dinámico: La asignación de Ordenes a Depósitos se realiza de manera dinámica según la distancia de estas a los depósitos seleccionados, contemplando la carga que puede transportar la flota asociada a cada Depósito

Inicio de Rutas
~~~~~~~~~~~~~~~~~~~~~~

En esta subpestaña, se describen los parámetros que pueden configurarse mediante un Slider y se puede ajustar su prioridad.

Preferencias de Selección de Semilla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Apertura Temprana: Se da preferencia de iniciar la construcción de las rutas (semilla) a los clientes con inicio horario más temprano (inicioHorario)."

    Cierre Temprano: Se da preferencia de iniciar la construcción de las rutas (semilla) a los clientes con fin horario más temprano

    Horario Promedio: Se da preferencia de iniciar la construcción de las rutas (semilla) a los clientes con horario promedio entre su inicio y fin horario es decir aquella cuyo horario sea el más parecido al promedio de todas las ventanas horarias de las Ordenes involucradas.

    Cercanía Ultima Ruta: Se da preferencia de iniciar la construcción de las rutas (semilla) a los clientes más cercanos a la última ruta generada

    Sensibilidad: Se da preferencia de iniciar la construcción de las rutas (semilla) según la ponderación de la slider de heurística de mayor peso

    Barrido Angular: Se da preferencia de iniciar la construcción de las rutas (semilla) aquella Orden que minimice su ángulo polar con respecto al Depósito. Es decir que la primer Orden con la que se construye la Ruta sea la primera hallada "barriendo" angularmente en sentido horario un giro de 360º a partir del Depósito de Salida.

    Densidad: Se da preferencia de iniciar la construcción de las rutas (semilla) donde la primer Orden sea aquella que se halla en el lugar de mayor concentración de Ordenes.

    Distancia Deposito: Se da preferencia de iniciar la construcción de las rutas (semilla) tal que la primer Orden se encuentre más cerca del Depósito de Salida

    Demanda: Se da preferencia de iniciar la construcción de las rutas (semilla) donde la primer Orden sea aquella cuya demanda en promedio sea mayor (Volumen, Peso, Pallets, Bultos).

Prioridades Automáticas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Usar Prioridades Automáticas: Permite asignar valores dinámicos de prioridades absolutas a las Ordenes según distintos criterios: Por vehículo o Por importe, según se elija.

    - Por Vehículo: Prioriza el ruteo de órdenes que pueden ser transportadas por un porcentaje bajo de la flota disponible.

    - Por Importe: Prioriza el ruteo de órdenes según los valores de importe asociados.

    - Ignorar Valores: Se ignoran los valores de prioridades absolutas asociados a las órdenes durante el ruteo. Todas las Ordenes serán evaluadas sin Prioridad.

Grupos
~~~~~~~~~~

En esta subpestaña, se puede configurar los grupos de manera en la que se generan. A continuación se describe cada uno de los parámetros


Autoclustering
^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Habilitar Autoclustering: Habilita el uso de un algoritmo de clusterización K-Means. El agrupamiento se realiza minimizando el cuadrado de la suma de distancias entre cada Orden y el centroide de su grupo. Por lo tanto, permite al sistema dividir las Ordenes para tratar de segmentar el armado de rutas y que éstas sean más compactas."

.. note::
    
    K-Means es un algoritmo iterativo que divide un conjunto de Ordenes en k grupos diferentes de tal manera que cada Orden pertenece solo a un grupo que tiene propiedades similares.

.. container:: justified-text

    Factor: Es el número de grupos (k) o centroides que se escogerán inicialmente del conjunto total de Ordenes para inicializar el primer paso del Algoritmo de clusterización K-Means. Por Default k = 5

    Ignorar Grupos Previos: Si las Ordenes tienen Grupo Ruta, se ignoran los mismos y se arman nuevos Grupos utilizando el ruteador k-Means. Estos Grupos no van a poder ser mezclados entre sí.

    Respetar Cantidad: Al "ignorar Grupos previos" se construyen la misma cantidad de Grupos que el Usuario definió. Es decir, se setea el k = cantidad de Grupo Ruta.


Grupo de Rutas No Restrictivo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Habilitar Grupo De Rutas No Restrictivo: Permite la inserción de órdenes de distintos Grupos dentro de una misma ruta durante la Construcción de esta. Busca flexibilizar la mezcla ordenes de diferentes grupos en algunas rutas: 

    - MIN: respeta 100% el Grupo.

    - MAX: desactiva el grupo y permite mezclar todas las ordenes sin restricción.

Opciones de agrupamiento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Permitir Invasión De Grupos: Genera una Ruta primero con Ordenes de un mismo Grupo, y si la capacidad lo permite, se inserten Ordenes de otros Grupos. Tener en cuenta que debe setearse que Grupos están permitidos y la distancia máxima al baricentro geográfico del Grupo de Ruta Original puede buscar Ordenes (Grupos Permitidos y Radio de Invasión del modelo de condiciones).

Opciones de Agrupación en Ruta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Sumar Tiempos De Espera: Agrupación de Ordenes, que suman los tiempos de espera seteados en cada uno. Debe encontrarse seteado "Agrupación en ruta" en Configuración General. Valor mínimo 1 minuto."

    Considerar Espera En Segundos: Requiere el campo "Sumar tiempos de espera" seteado. Considera que la unidad de tiempo en "Tiempo de Espera" sean segundos, al finalizar lo divide para setearlo en minutos."

    Tiempos De Espera Máximo (MAX): Cota superior de suma de "Tiempo de Espera" en minutos de todas las Ordenes del mismo Domicilio. El valor del campo "TiempoEsperaMaximo" en la entidad “DomicilioOrden", de no encontrarse seteado utiliza el del escenario o no tendrá cota si no se encuentra esta última seteada.

    Tiempos De Espera Mínimo (MIN): Cota inferior de suma de "Tiempo de Espera" en minutos de todas las Ordenes del mismo Domicilio. El valor del campo "TiempoEsperaMinimo" en la entidad “DomicilioOrden", de no encontrarse seteado utiliza el del escenario o no tendrá cota si no se encuentra esta última seteada.

    Cantidad Máxima De Visitas: Indica cuántas veces puede ser visitado como máximo un domicilio (DomicilioOrden), en diferentes rutas de la misma Jornada, siempre que no sea posible hacerlo con la configuración indicada en el campo “Porcentaje mínimo de entrega parcial”, el cual estará al 100% para intentar que todos los consolidados de un cliente vayan en una sola ruta.

    Porcentaje Mínimo De Entrega Parcial: Permite realizar entregas parciales, seteandole cuál es el mínimo % que cumple la condición.

    Respetar Porcentaje En Segundas Vueltas: Respeta el % de entrega parcial para las segundas vueltas de la Ruta.

Vehículos
~~~~~~~~~~~~~~

.. container:: justified-text

    En esta subpestaña, se puede configurar los Vehículos para realizar la ejecución de rutas. A continuación se describe cada uno de los parámetros:

Modo
^^^^^^^^^

.. container:: justified-text

    Minimizar: Busca generar Rutas saturadas al utilizar la menor cantidad de Vehículos disponibles para la planeación

    Usar Todos: Busca utilizar todos los vehículos disponibles en la planeación, independientemente de la saturación de ruta resultante. 


Preferencia en selección de vehículos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Reutilizar Tipos De Vehículos: Permite que un Tipo de Vehículo realice varias vueltas en una Jornada

    Respetar Mismo Grupo De Rutas: Permite que un mismo Vehículo sea reutilizado para realizar una segunda vuelta, pero solo si ésta tiene como destino clientes del mismo Grupo de la Primer Vuelta. Debe encontrarse seteado "Reutilizar tipo".

    Flexible: Opción que permite que solo en las segundas vueltas puedan incluirse otros clientes de Grupos de Rutas distintos para optimizar el Vehículo en dicha segunda vuelta, siempre y cuando una de las Ordenes de la segunda vuelta sea de la primera vuelta. Debe encontrarse seteado "Respetar mismo grupo de rutas" para poder utilizar esta opción.

    Slider Vehículos Pequeños - Grandes: Permite ponderar la preferencia en el tipo de vehículo a ser seleccionado para generar un ruteo.

    Cantidad Según Grupo De Rutas: Modifica la cantidad de vehículo de cada Tipo Vehículo sea igual a la cantidad de Grupos de rutas a rutear.

    Usar Vehículos Auxiliares: Prioriza los Tipos de Vehículos a utilizar por Vehículo Operación que puedan generar segundas vueltas. Requiere seteado el check "Utilizar Flotas por operación" de Parámetros Generales.

Porcentaje de cargas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Volumen Máximo: Porcentaje de volumen máximo para tener en cuenta durante el ruteo

    Peso Máximo: Porcentaje de peso máximo para tener en cuenta durante el ruteo.

    Bultos Máximo: Porcentaje de bultos máximo para tener en cuenta durante el ruteo.

    Pallets Máximo: Porcentaje de pallets máximo para tener en cuenta durante el ruteo.

    Adicional 1 Máximo: Porcentaje de Adicional 1 máximo a tener en cuenta durante el ruteo.

    Adicional 2 Máximo: Porcentaje de Adicional 2 máximo a tener en cuenta durante el ruteo.

    Mínimo Global: Porcentaje mínimo de carga de los vehículos para que una ruta sea considerada como válida. Debe considerarse al menos una de las variables mínima de la Demanda (Pallets, Peso, Volumen o Bultos)

    Restrictivo: Permite las validaciones de las demandas mínimo.

    Restrictivo Mínimo Global: Construye rutas sin validar el mínimo global, y luego elimina post construcción las rutas que no cumplen con algún mínimo.

    Mínimo Global Segundas Vueltas: Permite considerar distintos porcentajes mínimos para la segunda vuelta de la ruta. En caso de no habilitarlo, el algoritmo utilizará el porcentaje mínimo definido para la primera vuelta.

Productos
^^^^^^^^^^^^^^^

.. container:: justified-text

    No Mezclar Dadores De Carga: Dada la existencia de un mismo Producto (SKU) que pertenece a dadores de carga diferentes, se busca parametrizar la entrega de modo tal de evitar el riesgo de que el conductor entregue el lote de producto incorrecto al destinatario.  Por lo tanto, el seteo permite que si dos órdenes poseen Productos con mismo SKU y distinto IdCliente (obtenido de la entidad Producto,  no de la Orden) no podrán ser ruteados juntos."

    Permitir En Mismo Destino: El seteo permite que si dos órdenes poseen productos con mismo SKU solo pueden rutearse juntos si ambos ordenes posean el mismo destinatario (mismo cliente, mismo domicilio). Requiere "No mezclar dadores de carga" " activo."

Volumetría
^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Volumetría: Análisis y cálculo de la ubicación 3D de los ítems asociados a las ordenes dentro del Vehículo.

    Agrupar Por Orden: La ubicación de los ítems se calcula contemplando la secuencia de las órdenes dentro de la ruta, aunque esto implique dejar huecos por las características volumétricas de los ítems. Es decir, forzará a que sean ubicados según el orden de secuencia ( método LIFO )

    Permitir Apilabilidad Por Camas: Permite poder apilar objetos de distintas dimensiones, colocando niveladores / separadores para indicar el nuevo nivel (cama). Para lograrlo deben estar marcadas las opciones anteriores:  "procesar volumetría" y "agrupar por orden". 

    Procesar Compartimentos Espejados: Una vez finalizada la construcción de la Ruta, validará que la carga de la misma sea tipo espejo (simetría espejada) con el fin de evitar bamboleo de Carga. La condición es seteada en la entidad Compartimento. Tener en cuenta que puede quitar Ordenes para cumplir lo anterior.

    Tolerancia De Altura: Diferencia de altura permitida entre distinto productos al "Procesar compartimentos espejados" en cm

    Procesar Compartimentos: Los cálculos de volumetría de los ítems se realizan luego de ser paletizados, por compartimentos disponibles por vehículo.

Depósitos automáticos
^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Permitir Múltiples Depósitos: Al utilizar "Depósitos Automáticos", las órdenes que queden sin rutear de un depósito pueden ser ruteadas utilizando la flota de otro depósito.

Horarios
~~~~~~~~~~~~~~

.. container:: justified-text

    En esta subpestaña se puede configurar los Horarios para configuración de Depósitos, Vehículos y Ordenes. A continuación, se describe cada uno de los parámetros.

Depósitos 
^^^^^^^^^^^^^^

.. container:: justified-text

    Depósitos Sin Límite Horario: No se considera el horario final de los depósitos de llegada, permitiendo el retorno a los mismos en cualquier momento (no necesariamente en el mismo día). 

    Salida Temprana De Depósitos: Se generan rutas de manera tal que su inicio corresponde al horario más tardío entre el inicio horario del Depósito de Salida y el inicio horario del vehículo.

Vehículos
^^^^^^^^^^^^^^^^

.. container:: justified-text

    Tolerancia De Arribo Al Depósito (Min): Permite planificar la llegada al Depósito dentro de N minutos posteriores a su fin horario, solo cuando la herramienta lo encuentre necesario. Las entregas se realizarán dentro de la ventana horaria del tipo de vehículo excepto el horario de arribo al depósito.

Ordenes
^^^^^^^^^^^

.. container:: justified-text

    Tolerancia De Arribo Tardío (Min): Permite planificar la visita a un cliente dentro de N minutos posteriores a su fin horario, solo cuando la herramienta lo encuentre necesario. Lo aplica a todas las Ordenes. El algoritmo priorizará el ruteo de las Ordenes que respeten las ventanas horarias originales."

    Múltiples Días: Se permite que las Ordenes sean entregadas N días posteriores al día de la Jornada, según los días permitidos de las mismas.

    Visita En Ventana Horaria: El inicio y el fin de la visita deben ocurrir dentro de la ventana horaria de la Orden.

Simulación de Ventanas
^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Modificar Ventanas Horarias: Habilita la modificación de las ventanas horarias.

    Por Intervalos: Genera N segmentos (turnos de visita) entre el inicio más temprano y fin más tardío dentro de la jornada

    Ampliar Fin (Min): Modifica dinámicamente el valor del fin horario en N minutos de todas las órdenes. Es decir, agrega los N minutos indicados al FinHorario de TODAS las Ordenes/Paradas.

Parámetros Avanzados
~~~~~~~~~~~~~~~~~~~~~~

.. container:: justified-tex

    En esta subpestaña se puede configurar parámetros avanzados como restricciones, concurrencias, Ruteos por calles. A continuación, se describe cada uno de los parámetros.

Construcción de Ruta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Priorizar Distancia Versus Tiempo (Alpha): Prioriza la distancia de las Ordenes sobre el tiempo de espera producido por ventanas horarias de corta duración; induciendo así al algoritmo a producir rutas más cortas en distancia sin considerar los tiempos muertos de espera (resultando rutas quizás más largas en tiempo de duración).
    
    Ahorro En Distancia (Delta): Factor que considera el ahorro en distancia entre clientes al analizar la inserción de un tercero entre ellos.

    Priorizar Punto Lejos (Gamma): Prioriza las ordenes lejanas del depósito de llegada, considerando que son las más difíciles de rutear, independientemente de cuan malo sea su costo de inserción.

    Priorizar Puntos Cercanos (Omega): Prioriza las ordenes más cercanas al centro geográfico de la Ruta. Este centro se calcula obteniendo baricentro geográfico de todas las ordenes de la ruta, sin considerar el Depósito de Salida ni el de Llegada.

    Omega Root: Prioriza las ordenes más cercanas a la posición de la semilla de la ruta.

    Epsilón: Rutas cuya prioridad de inserción son las Ordenes más cercanas a la recta armada entre el baricentro de la ruta al Depósito de Salida. A mayor valor que Épsilon, mayor es la incidencia. Default Value = 0 (nula incidencia) 

    Epsilón Root: Rutas cuya prioridad de inserción son las Ordenes más cercanas a la recta armada entre la posición de la semilla de la ruta al Depósito de Salida. A mayor valor que Épsilon, mayor es la incidencia. Default Value = 0 (nula incidencia)

    Ventana De Inspección: Cantidad de arcos de ruta que se evaluarán para Determinar el Punto de inserción de la Ordene en una ruta. Default: últimos 10 arcos realizados de la Ruta

    Ventana De Inspección Automática: El producto seleccionará automáticamente los tramos a realizar las evaluaciones para determinar el mejor punto de inserción de la Orden no ruteada, siendo esta la mitad de las entregas realizadas en la ruta.

    Parámetros Automáticos: Pondera Priorizar distancia versus tiempo (Alpha) según las optimizaciones realizadas.

    Heurística De Mínimos Rápidos: Penaliza las Ordenes a utilizar como semilla que al haber sido utilizadas anteriormente han construido rutas desarmadas por no cumplir los mínimos de Demanda.

    Analizar Motivos De No Ruteo: Se analizarán los motivos de no inserción de las órdenes que queden sin rutear en todas las rutas.

    Contorno Avanzado: Genera un polígono tal que busque el contorno más preciso de todas las Ordenes a Rutear (Alpha Hull)

    Considerar Áreas: Genera un polígono tal que busque un contorno aproximado que englobe a todas las Ordenes a Rutear (Convex Hull)

    Impedir Cruces: Se impide durante la construcción y optimización de rutas la generación de cruces entre ellas. No considera los trayectos desde y hacia los Depósitos.

Restricciones
^^^^^^^^^^^^^^

.. container:: justified-text

    Ignorar Producto - Producto: Permite deshabilitar la condición restrictiva entre Productos a ser transportados.

    Ignorar Tipo De Vehículo - Producto: Permite deshabilitar la condición restrictiva entre los Productos a ser transportados y el Tipo de Vehículo permitido para realizarlo.

    Ignorar Tipo De Vehículo - Domicilio Orden: Permite deshabilitar la condición restrictiva entre el Tipo de Vehículo y el domicilio de entrega permitido.

    Ignorar Tipo De Vehículo - Categoría Orden: Permite deshabilitar la condición restrictiva entre el Tipo de Vehículo y la Categoría de la Orden por Empresa.

Primera Orden 
^^^^^^^^^^^^^^^^

.. container:: justified-text

    Considerar Valor Importe: El armado de rutas contemplará que el primer orden a visitar deberá ser aquella que maximice y supere el valor importe indicado en el campo Importe de la entidad Orden.

    Mínimo: Permite indicar la cota mínima a considerar el importe de la Orden. 

Concurrencia
^^^^^^^^^^^^^^^

.. container:: justified-text

    Usar Múltiples Hilos: Las N iteraciones configuradas para resolver el problema de ruteo, se repartirán en tantos hilos como el usuario indique. Depende de la cantidad de procesadores disponibles en el servidor, pueden usarse hasta 4 para mejorar el tiempo de procesamiento al generar Rutas.

Ruteo por calles
^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Limitar Vecinos: Cantidad de órdenes lindantes entre sí que se considerarán para calcular las distancias entre ellas por "calles" según un criterio de "cercanía", mientras que para el resto de las Ordenes el ruteo será lineal. Se utiliza cuando las distancias entre clientes son largas e implican un recorrido amplio ente clientes. Default Value: 30 clientes.

    penalización Lineal: Al no encontrar un camino entre dos órdenes, la distancia entre ambas al armar la ruta se considerará lineal, penalizada por un factor.

    Distancia Temporal Avanzada: Utiliza para el cálculo una velocidad que surge del promedio entre el promedio armónico, el promedio aritmético y la velocidad mínima del conjunto de velocidades dado.

    Porcentaje Velocidad Vial: Permite modificar la velocidad dada por la red de calles a utilizar para viajar entre dos puntos.

    Usar Servidor: Permite la selección y utilización de un servidor particular para realizar el ruteo por calles.

    Origen: Indica el path del servidor a utilizar.

Optimización
~~~~~~~~~~~~~~~~~~~~~~

.. container:: justified-tex

    En esta subpestaña se puede configurar Optimizadores para dar mayor prioridad. A continuación, se describe cada uno de los parámetros.

Selección de Resultado Optimo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Criterio de selección de mejor iteración, según:

    Cantidad De Vehículos: Asociado a utilizar la menor cantidad de vehículos.

    Solapamiento: Asociado a la menor área total solapada entre las rutas.

    Optimización De Carga: Asociado a la mayor demanda total transportada en las rutas generadas.

    Distancia Recorrida: Asociado a la menor distancia total de las rutas generadas.

    Tiempo: Asociado a la menor duración total de las rutas generadas.

    Espera En Muelles: Menor tiempo de espera en patio para los muelles del Depósito de llegada.

    Menor Costo: Asociada al menor Costo por tipo de vehículo.

Post-Optimizadores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Busca mejorar el resultado de ruteo de la mejor iteración.

    Cantidad De Iteraciones: Cantidad de veces que correrá el proceso de optimización. 

    Secuencia: Optimización de la secuencia de cada ruta, eliminando, si es posible, cruces internos.

    Cargas: Se verifica el nivel de carga del vehículo asignado a la ruta y en caso de que el mismo no se encuentre completo, intentará cambiarlo por otro de menor carga máxima (o sea que mejor se ajuste a la carga de la Ruta). Se ejecuta automáticamente siempre.

    Secuencial Lineal: Optimización de la secuencia de cada ruta, eliminando, si es posible, cruces internos considerando distancias lineales y no por "Calles".

    Segundo Interno: Luego de optimizar las rutas generadas, se evalúa nuevamente la inserción de las órdenes que quedaron sin rutear. Corre automáticamente luego de los Optimizadores.

    Permitir Invasión De Grupos: Durante el "Segundo intento" se invalida el Grupo de las Ordenes para que encuentre un mejor resultado. P.e. Necesidad de optimizar de Rutas fijas.

    Distancias: Optimización de rutas realizando cambios de secuencia o intercambio de Ordenes entre Rutas con el objetivo de disminuir la distancia total de las Rutas generadas.

    Distancia A Deposito: Re secuencia las Rutas dejando en lo posible como primera visita la Orden más cercana al Depósitos de salida, ignorando la prioridad de ruteo de las Ordenes.

    Baricentros: Busca eliminar solapamiento, al intercambiar Ordenes entre dos Rutas entendiendo que el ""área"" de cobertura de cada Ruta será menor. Logra Rutas más compactas y elimina cruces entre ellas. A su vez, evita desvíos en las Rutas al rutear por baricentro de Cargas.  "

    Opt-Remove: Optimiza la distancia total de una Ruta (kms) al reordenar la posición de sus órdenes determinando nuevamente su punto de inserción a la ruta armada.

Procesos
^^^^^^^^^^^^^

.. container:: justified-text

    Distancia Por Calles: Post Proceso que Re secuencia la Ruta minimizando la cantidad de recirculaciones en los viales. Requiere que todas las Ordenes posean la misma Ventana Horaria. No contempla en su validación: Visita en ventana horaria, Prioridad relativa (Orden.PreOrden), Ultima Visita y demás reglas que afecten a la secuencia de las visitas."

    Tsp Trip: Optimizador que Re secuencia la ruta. Requiere que todas las Ordenes posean la misma Ventana Horaria. No contempla en su validación: Visita en ventana horaria, Prioridad relativa (Orden.PreOrden), Ultima Visita y demás reglas que afecten a la secuencia de las visitas.  Requiere tener un parámetro configurado: OSRM_Trip http://router.project-osrm.org/trip/v1/driving/"". Pueden ser:

    Automático: Valor Default.
    + Distancia: Re secuencia tal que la última Orden es la de mayor distancia
    
    + Cercanía: Opuesto a lo anterior. empieza por la Orden más alejada finalizando en la más cercana

    Balancear: Optimización de rutas armadas realizando intercambio de Ordenes entre ellas para que se encuentren balanceadas (similitud) según:
    
    Cantidad: Total.

    Peso: Total.

    Volumen: Total.

    Bultos: Total.
    
    Pallets: Total.
    
    Adicional 1: Total.
    
    Adicional 2: Total.

    Tiempo: Total.
    
    % Peso: porcentaje de carga del tipo de vehículo.
    
    % Volumen: porcentaje de ocupación del tipo de vehículo.
    
    % Bultos: porcentaje de bultos del tipo de vehículo.
    
    % Pallets: Porcentaje de Pallets del Tipo de Vehículo.

    Contemplar Distancia: Anula el procedo "Balancear" anterior, al realizarse este aumenta la distancia total de las Rutas.

    Limitar Cuadros: Solamente se permitirá el proceso de "Balancear" entre Rutas de la misma zona (área conformada por el conjunto de Ordenes de la Ruta sin considerar los Depósitos)

    Tolerancia (%): Grado de aceptación de rutas que se consideran balanceadas.

    Objetivo: Valor mínimo que se considera como balanceado.

Parámetro de Optimizadores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: justified-text

    Permitir Invasión De Grupos: Durante el proceso de optimización permite invalidar el Grupo de las Ordenes para que encuentre un mejor resultado. P.e. Para la optimización de rutas fijas

    Impedir Absorción De Rutas: Impedirá minimizar la cantidad de vehículos utilizados durante la construcción. La cantidad de Vehículos post construcción será fija.

    Respetar Cantidad De Grupos: Impedirá minimizar la cantidad de Rutas con respecto a los Grupos de Rutas utilizados durante la construcción. La cantidad de Grupo de Rutas post construcción será fija.

    Análisis Lineal: Los análisis de aceptación de cambios de mejores se realizarán con distancias lineales.

    Contemplar Tiempo: Los análisis de aceptación de cambios de mejores se realizarán según los tiempos de viaje.

    Recalcular Radio: Redefine el radio de densidad a utilizar en el proceso de optimización según el radio de las rutas o Grupos de rutas armadas: Máximo, Mínimo, Promedio o Grupos.


``Barreras y Áreas``
----------------------

.. image:: Escenarios.png
   :align: center

.. container:: justified-text
    
    **Agregar Barreras**

    Barrera -1

    Dibujo: Dibujo Tipo trayecto con condición Barrera.

    Tiempo De Espera: Tiempo que se sumará al Tiempo de viaje entre dos Ordenes si se cruza la barrera. (En minutos)

    Activo: Considerar el uso de la Barrera durante el proceso de ruteo.

    **Agregar Ventana Horaria**

    Permite agregar una nueva Ventana Horaria a la barreara, activándola por horarios. 

    **Ventana Horaria**

    Inicio Horario: Inicio del período en el que la Barrera se encontrará activa.

    Fin Horario: Finalización del período en el que la Barrera se encontrará activa.

    Tiempo De Espera: Es la demora que se adicionará al trayecto que interceda la Barrera (En minutos).

    Propagación: Permite que la adición de los minutos debido a la barrera no sea abrupta, sino que se efumine en el tiempo.

    **Zona**

    Área de estacionamiento permitido para dejar el acoplado.

    Dibujo: Área de estacionamiento permitido para dejar el acoplado.

    Tiempo De Espera: Tiempo de demora para tareas auxiliares en el Área (desenganche, enganche, etc).

    Activo: Permite el uso del área durante el proceso de ruteo.

    Permite Cargar: Habilita el permiso de carga en la operación.
