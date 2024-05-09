Courrier Adapter 
==================

Descripción 
--------------

.. container:: justified-text

    UNIGIS Courier tiene como objetivo centralizar la integración de paqueteras y líneas de transporte usadas para el seguimiento de entregas por mensajería y que su consumo es por un tercero entre UNIGIS y el cliente. 
    
    Las integraciones que se agregan a UNIGIS Courier tienen como objetivo resolver la necesidad inicial y tener la capacidad de implementarse en otros clientes en caso de requerirlo ya que se usa el formato de consumo más estándar y se mantiene la funcionalidad VS UNIGIS en cada integración. 

    La funcionalidad principal es obtener el seguimiento de cada guía (Paquete), que es almacenada a nivel de parada y una vez que llegue al estado final realizar el cambio de estado. Como función adicional y por configuración podrá realizar este seguimiento a nivel de viaje y agrupado. 
    
    Courier se mantiene monitoreando los estados 24/7 con el objetivo de tener el seguimiento en tiempo real. 

Pre Requisitos
---------------

1. Solicitar la instalación de UNIGIS_AdapterCourier.

2. Ruta en repositorio: U:\Producto\Otros\UNIGIS_CourierAdapter.

.. note::
    
    Validar la versión que se va a instalar.


Información Técnica
---------------------

Tablas y Campos
~~~~~~~~~~~~~~~~~~

- Paquetera 

Tabla principal en la que se definen los filtros para recuperar los viajes y campo de búsqueda, (Entre más filtros se agregan se restringe más la consulta).

.. list-table:: Paquetera
    :widths: 10 10 45
    :header-rows: 1

    * - Campo 
      - Tipo    
      - Descripción/Uso
    * - ReferenciaExterna
      - Varchar	
      - Nombre de la paquetera.
    * - Descripcion	
      - Varchar
      - Breve descripción de la paquetera o mismo nombre.
    * - IdVehiculo	
      - Int
      - Filtro opcional al dejar nulo considera todos los vehículos.
    * - IdConductor	
      - Int
      - Filtro opcional al dejar nulo considera todos los conductores.
    * - IdCategoriaViaje
      - Int	
      - Filtro opcional al dejar nulo considera todas las categorías.
    * - IdTipoViaje
      - Int
      - Filtro opcional al dejar nulo considera todos los tipos de viaje.
    * - CampoGuia
      - Varchar	
      - Cualquier campo tipo Varchar de la tabla Parada o Viaje.
    * - IdTransporte	
      - Int
      - Filtro opcional al dejar nulo considera todos los vehículos.
    * - IdEstadoViaje	
      - Int
      - Filtro opcional al dejar nulo considera todos los estados de viaje.
    * - IdClienteOrden	
      - Bigint
      - Filtro opcional al dejar nulo considera todos los Clientes orden.
    * - IdCliente	
      - Int
      - Filtro opcional al dejar nulo considera todos los Clientes.
    * - Entidad	
      - Varchar
      - Nulo para mantener default Parada Viaje para buscar información a ese nivel.
    * - Activo	
      - Bit
      - Flag de control de registros activos o disponibles.
    * - FechaCreacion	
      - Datetime
      - Al realizar el registro se guarda en automático.
    * - FechaUltimaConsulta	
      - Datetime
      - Dato actualizado por cada consulta realizada.	

- PaqueteraConfiguracion

Tabla de homologación de estados de la paquetera VS estados UNIGIS.

.. note::
    
    Sin estados configurados no se hacen cambios de estado 

.. list-table:: PaqueteraConfiguración
    :widths: 10 10 45
    :header-rows: 1

    * - Campo 
      - Tipo    
      - Descripción/Uso
    * - IdPaquetera	
      - Int
      - Relación con la tabla Paquetera.
    * - EstadoPaquetera	
      - Varchar
      - Este dato corresponde al dato con el que se hará el match VS el estado UNIGIS Ejemplo: INGRESADO EN AGENCIA.
    * - IdEstadoParada
      - Int	
      - Estado UNIGIS al que corresponde con el campo anterior.
    * - Finalizado	
      - Bit
      - Marcar en true, cuando las paradas se encuentren en este estado ya no serán consideradas porque ya finalizaron su ruta.
    * - FechaCreacion
      - Datetime
      - Dato generado en automático por cada registro.	

- PaqueteraCredenciales

Tabla para configurar los accesos al servicio.

.. list-table:: PaqueteraCredenciales
    :widths: 10 10 45
    :header-rows: 1

    * - Campo 
      - Tipo    
      - Descripción/Uso
    * - IdPaquetera
      - Int
      - Relación con la tabla Paquetera.
    * - Clave
      - Varchar
      - Depende de cómo se configure la paquetera el uso, puede ser un token o una contraseña especifica.	
    * - Usuario
      - Varchar
      - Usuario o cuenta de acceso.
    * - Password
      - Varchar	
      - Password o token de acceso.
    * - URL
      - Varchar
      - URL del servicio de la paquetera a consumir.
    * - URL2
      - Varchar
      - En casos para recuperar POD u otro proceso agregar otra URL.

- MotivoConfiguración

Cuando existe un listado de motivos de no entrega se configuran en esta tabla. (Configuración similar a PaqueteraConfiguracion).

.. list-table:: PaqueteraCredenciales
    :widths: 10 10 45
    :header-rows: 1

    * - Campo 
      - Tipo    
      - Descripción/Uso
    * - IdPaquetera	
      - Int
      - Relación con la tabla Paquetera.
    * - MotivoPaquetera	
      - Varchar
      - Este dato corresponde al dato con el que se hará el match VS el motivo UNIGIS Ejemplo: RECHAZO CLIENTE.
    * - IdMotivo
      - Bigint	
      - Motivo UNIGIS al que corresponde con el campo anterior.	
    * - Activo	
      - Bit
      - Flag.
    * - FechaCreacion	
      - Datetime
      - Registro automático al momento de crear.

Parámetros
------------

Los parámetros que se deben configurar en el adapter se encuentran en el archivo App.config.

.. list-table:: Parámetros
    :widths: 10 40 15
    :header-rows: 1

    * - Clave 
      - Definición   
      - Ejemplo
    * - TimeZone	
      - Configurar zona según el país al que corresponde la información en la que se procesa.
      - Central Standard Time (México)
    * - DebugFile	
      - Número negativo, días que se va a mantener archivos o log.
      - -5
    * - Dir_Log	
      - Ruta para almacenar el log 	
      - C:\LOG
    * - StopsLimit	
      - Número máximo de paradas a recuperar en un bloque de ejecución.
      - 1000
    * - Culture	
      - Configuración de la región.
      - En
    * - LogFile	
      - Permite guardar log en archivo	
      - True
    * - RepetirCada	
      - Intervalo de tiempo de ejecución.
      - 300 (esto se convierte a milisegundos) Equivale a 5 minutos
    * - Take
      - Número de viajes a tomar por ejecución.
      - 100
    * - EndShipment	
      - Indicar si finaliza el viaje.
      - True
    * - EndShipmentStatus	
      - Si el parámetro anterior es true indicar el estado al que pasa el viaje para finalizar.
      - Finalizado
    * - ValidarTransicion	
      - Para cambios de estado valida la transición antes del cambio.
      - True
    * - MismoEstado	
      - Para cambios de estado valida si es el mismo origen y destino.
      - False
    * - Token	
      - Token maestro para realizar la petición del consumo de la API externa.	
      - eyJpc3MiOiJodHRwczpcL1wvYXBpLmNhc3R


Procesos
-------------

Una vez que se tiene el deploy y la configuración se comenzarán a ejecutar los siguientes procesos para lograr la recuperación de los estados y los cambios necesarios en UNIGIS. 

Los siguientes procesos son métodos utilizados de forma interna por el adapter, no requieren configuración: 

- ConsultaViajesConfiguracionPaquetera

Según los filtros configurados en la tabla Paquetera se buscan los viajes, en caso de no tener filtros por default busca todos los viajes en estado activo, esto como resultado generara una lista de viajes con todos sus datos para cada uno.  

- ObtieneParadasViajes

Con la lista de viajes del método anterior, uno a uno se recuperan las paradas que no se encuentren en estado finalizado, de acuerdo con lo configurado en PaqueteraConfiguracion, es decir que no se van a tomar en cuenta las paradas con estado donde el campo Finalizado se encuentre en true. 

.. image:: ejemplo.png
   :align: center

.. note::

    Paradas en el estado Entregado no serán consideradas ya que cumplieron su flujo completo.

El resto de las paradas del viaje que se está ejecutando en ese momento se recuperan y continúan al siguiente método. 

- BuscarDatosParadas

Con la lista de paradas se realiza el proceso de consulta según la paquetera en ejecución Se menciona a detalle en el anexo PANTALLAS DE CONFIGURACIÓN

- EndShipment

Si el parámetro “EndShipment” del archivo App.config se encuentra en true validará de nuevo las paradas del viaje y si estas ya se encuentran en un estado finalizado, realizará el cambio de estado del viaje al configurado en el parámetro “EndShipmentStatus” del archivo App.config.

El objetivo de pasar las paradas a un estado finalizado y los viajes es minimizar la cantidad de veces que se consultan en cada ejecución, permitiendo así la recuperación de información precisa en tiempo real. 

.. note::
    
    Todas las paqueteras integradas ejecutan los mismos métodos según la configuración de cada una.

- ModificarEstadoParada

Este método es el mismo utilizado en el servicio UNIGIS MAPI Logistic, la lógica que ejecuta de manera interna es la misma. 

Parámetros enviados a través del método: 


.. list-table:: Parámetros
    :widths: 15 45
    :header-rows: 1

    * - Parámetro pEstadoParada
      - Descripción  
    * - Estado	
      - Descripción del estado al que se va a modificar la parada.
    * - EstadoFecha	
      - Según la respuesta del servicio o API se recupera la fecha del estado en que se ejecutó, en caso de no tener fecha se pone la actual del servidor. 
    * - IdViaje	
      - Id del viaje al que pertenece la parada que se está ejecutando.
    * - RefDocumento	
      - Parada.ReferenciaExterna.
    * - Motivo	
      - Solo en las paqueteras que aplique. Descripcion del motivo.

Pantallas de Configuración 
-------------------------------

La ruta para llegar a los ABM de configuración es: 

:kbd:`Integrations Center` --> :kbd:`Couriers` --> :kbd:`Configuración`

En esta pantalla se podrán visualizar los registros de paquetera configurados y el log como funciones principales. 
Otras funciones: :kbd:`Crear`, :kbd:`Editar`, :kbd:`Borrar` o :kbd:`Buscar Registros`. 

Logs
~~~~~~~~

.. image:: logs.png
   :align: center

Los logs se guardan en forma descendente y se podrá realizar la búsqueda entre ellos por Id, Bultos, Parada, Destino y Estado.

Adicional a la pantalla de logs de Courier se almacenan registros de log general en el siguiente apartado: :kbd:`Integrations Center` --> :kbd:`Integrations Logs` --> :kbd:`Logs/Bitácoras`.
  
Este log guarda todos los errores, alertas y mensajes general del adapter. 

.. image:: logogrl.png
   :align: center

Crear/Editar
~~~~~~~~~~~~~~~~

En una sola pantalla se podrán configurar las 4 tablas de Courier las cuales son: 

1. Pestaña General: Configurar el nombre de la paquetera, filtros de consulta y el campo de la guía.  

.. image:: crear.png
   :align: center

2. Pestaña Credenciales: Muestra el formulario para ingresar los datos de seguridad y URL del servicio de la paquetera.

.. image:: credenciales.png
   :align: center

3. Pestaña Configuración: Con el botón :kbd:`+` se pueden agregar los estados necesarios y comenzar a relacionar con el estado UNIGIS, se muestra una lista con los estados de parada configurados. 

.. important::

    Marcar al menos 1 estado como finalizado que es el punto final de seguimiento.

.. image:: config.png
   :align: center

4. Pestaña Motivo: Con el botón :kbd:`+` se pueden agregar los motivos que sean necesarios siempre y cuando la paquetera lo utilice. 

.. image:: motivo.png
   :align: center

Al finalizar dar clic en Crear y se guardan todos los registros en las tablas que les corresponde. 

.. note::

    La configuración que se muestra en cada paquetera es en base a un requerimiento inicial, se puede modificar según la necesidad de cada cliente.









