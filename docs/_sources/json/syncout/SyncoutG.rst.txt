Syncout Genérico
=======================

Descripción 
--------------

.. container:: justified-text

    JSON Syncout permite realizar el envío de información de los cambios de estado a través de las tablas sistema externo a servicios que no requieran autenticación, esta nueva versión va a permitir la autenticación de diferentes formar como Basic Auth, Bearer Token, OAUTH y con el envío de Json genérico que tiene el actual o diferente según lo requiera el cliente.

    Tener un Syncout es una herramienta para enviar información a cualquier tipo de servicio y con diferentes formatos de tal forma que pueda reemplazar los Syncout Custom y disminuir el tiempo de implementación de este, solo se deberá configurar y levantar la instancia en el servidor.

    Es necesarios solicitar el deploy del Syncout que se encuentra en la siguiente ruta: U:\Producto\Otros\JSON_SyncOut\UNIGIS_JsonSyncOutV2.zip  

    En el config del Syncout solo se debe configurar lo siguiente: 
    
    - Base de datos  
    
    - parámetros
        - SistemaExterno: Nombre del sistema externo a monitorear.
        
        - CustomParam0 (1,2,3…): Funcionan igual que en la versión 1 de JSON Syncout con el mismo formato Name0|Value0.
        
        - Path Log: Ruta donde se depositará el archivo log, solo para casos donde aplique.

**Ejemplo:**

.. code-block:: xml
    :linenos:

            <appSettings>
                <add key="SistemaExterno" Value= "ArchivosPlANOS_FleteCCU" />
                <add key="CustomParam0" value="Name0|Value0" />
                <add key="CustomParam1" value="Name0|Value1" />
                <add key="CustomParam2" value="Name0|Value2" />
                <add key="CustomParam3" value="Name0|Value3" />
                <add key="Path_Log"     value="C:\Log"  />

Parámetros
------------

.. container:: justified-text

    Se genera la tabla SistemaExternoConfiguración con el objetivo de concentrar la configuración de cualquier entidad dentro de una sola tabla y Json Syncout V2 busque en esta lo necesario para poder operar 

.. image:: parametro.png
   :align: center

.. container:: justified-text

    Es necesario ingresar a :kbd:`Administración del Sistema` --> :kbd:`Sistema` -->  :kbd:`Parámetros`.


Parámetros Claves y Descripción de Parámetros
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: justified-text

    :kbd:`< JsonConfiguracion >` Estructura Json que se detalla más adelante y tendrá como función tener todo lo necesario sobre la API a consumir como: URL, parámetros, credenciales, método de consumo, configuración requerida previa a consumo entre otros datos. Este se podrá configurar dentro de un ABM.
    
    :kbd:`< JsonSQL >`	El campo indica la combinación entre JSON y SQL ya que como primer paso el campo contendrá una consulta SQL con una clave que permite darle una salida en formato JSON.
    
    :kbd:`< Entidad >`	Indica la tabla SistemaExterno[modificar/crear]estado[viaje/pedido/parada/guia]salida relacionada al sistema externo que se pretende habilitar.
    
    :kbd:`< IdSistemaExternoEntidad >`	Este campo no tiene llave foránea, pero va relacionado al campo anterior con el ID de la tabla que se selecciones para ese campo, en el ABM se mostrara la lista de los registros configurados previamente para relacionarlo.
    
    :kbd:`< Activo y FechaCreacion >`	Campos de control interno para habilitar o deshabilitar y fecha de registro.
    
Procesos
~~~~~~~~~~~~~

.. container:: justified-text
    
    Habilitar Permisos para uso de Integrations Center.

    Es necesario configurar los permisos de acceso para el nuevo módulo para ello es necesario ingresar a :kbd:`Administrador del sistema` --> :kbd:`Grupos`. Seleccionar el grupo que desee actualizar y dar la opción de editar, 


Funcionalidad
----------------

.. container:: justified-text

    Una vez que se tiene levantada la instancia de Json Syncout V2 se debe realizar la configuración de la tabla Por ABM - Integraciones – Sistema Externo – Json – Crear (Documentación de ABM en el siguiente ticket: https://unigis.atlassian.net/browse/DEV-19928. 

Configuración JSON
~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: justified-text

    El formato JSON se explica en este documento (En caso de no poderlo visualizar se adjunta al ticket directamente): 

.. code-block:: xml
    :linenos:

        "Jason": [{
                    "URL":{
                    "URI": "www.url.com./metodo",
                        "key": "@WareHouse"
                        "Entity": "Viaje.DepositoSalida",
                        "Field": "ReferenciaExterna"
                  }
        ]
        "Headers": [],
        "ParamsBody": [],
        "Method": "GET",
        "ContentType": "",
        "Accept": "*/*",
        "AuthorizationType": {
            "AUTH": "Basic Auth".
            "Credentials": [{
                    "Key": "Username",
                    "Value": "User"
                    }
                ]
            "Response": {
                "Type": "",
                "Field": "
                }
            },
        "EnvioUnico": true,
        "Sequence": 1
    }


.. Note::
    
    De forma temporal se tendrá que ingresar el JSON en un cuadro de texto con el formato solicitado, más adelante se estará modificando a un formulario

.. container:: justified-text

    A continuación, el detalle de cada campo en el JSON:

.. image:: detalle.png
   :align: center

.. container:: justified-text

    Una vez configurada esta tabla y que la instancia nueva este arriba en el servidor cuando se realicen los cambios de estado se buscará en esta tabla y dependiendo de la configuración realizada hará los envíos 

    En caso de no requerir esta configuración basta con seguir utilizando el método de lo que hoy es Json Syncout donde configuran la URL en la tabla de la entidad con el alias Salida y se enviara en un método POST con el formato JSON base

Configuración del campo JSON SQL 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: justified-text

    El objetivo de este campo es que con una consulta se pueda obtener el JSON con la especificación que el servicio lo pide y poder dar más flexibilidad en caso de que esta llegue a cambiar poderlo modificar directo en el ABM y no en el Syncout. 

    Por ejemplo con la siguiente consulta:

.. code-block:: SQL
    :linenos:

    SELECT 
            IdViaje, Descripcion
    FROM 
            Viaje
    WHERE 
            Viaje.IdViaje. IN (272,273)
    FOR JSON PATH

.. container:: justified-text

    Se obtiene el siguiente JSON por la instrucción que tiene el final “FOR JSON PATH”

.. code-block:: xml
    :linenos:

    [
        {  
            "IdViaje": 272,
            "Descripción": "Desc-272"
        }
        {
            "IdViaje": 273,
            "Descripción": "Desc-273"
        }
    ]

.. container:: justified-text

    **Caso de Uso**

    Para guardar el SQL es necesario considerar 1 a 2 parámetros.

    1.	parámetro que es la base de la entidad que estamos enviando (Viaje, Parada, Orden, etc.)
    
    2.	parámetros cuando en el JSON se mandará detalle como en viaje se mandará Idparada
    
    Por ejemplo, 

    SQL con 2 parámetros, estos siempre llevaran este nombre independiente a la entidad: 

.. code-block:: SQL
    :linenos:
    
    select 
    o.ReferenciaAdicional 'orderkey',
    r.IdRuta 'route',
    o.Orden 'stop',
    rtrim(v.Dominio) 'trailernumber',
    rtrim(v.Dominio) 'susr4',
    o.RefOrdenExterna 'susr3',
    'INT0122-1' 'susr1',
    GETDATE() 'susr2'
    from ruta r with(nolock)
    inner join orden o  with(nolock) on (r.Ruta = o.IdRuta and o.IdJornada = r.IdJornada)
    inner join Vehiculo v  with(nolock) on (v.IdVehiculo = r.IdVehiculo)
    where r.IdRuta = !!ID_ENTIDAD!! and r.IdOrden = !!ID_ENTIDAD2!!
    FOR JSON PATH, WITHOUT_ARRAY_WRAPPER

.. container:: justified-text

    Hay casos más complejos donde se necesita obtener un formato con arreglos, ejemplo:

.. code-block:: SQL
    :linenos:

    select
    p.ReferenciaExterna 'externalreceptkey2',
    p.ReferenciaAdicional 'externreceiptkey',
    d.RefDomicilioExterno 'storerkey',
    2 'type',
    ( 
                SELECT 
                'TEST2226000' 'externlineno'
                'RETORNO'  'toloc'
                'TEST001676' 'externreceiptkey'
                oid.lottable01 'lottable01'
                oid.lottable01 'lottable02'
                oid.lottable01 'lottable03'
                oid.lottable01 'lottable04'
                oid.lottable01 'lottable05'
                oid.lottable01 'lottable06'
                oid.lottable01 'lottable07'
                oid.lottable01 'lottable08'
                oid.lottable01 'lottable09'
                oid.lottable01 'lottable10'
                oid.lottable01 'lottable11'
                oid.lottable01 'lottable12'    
                (pi.Cantidad - pic.Cantidad) 'qtyexpected',
                prd.ReferenciaExterna 'sku',
                d.RefDomicilioExterno 'storerkey'
                FROM ParadaItem AS pi
                inner join Producto prd on (prd.IdProducto = pi.IdProducto)
                left join ParadaItemCantidad pic on (pi.IdParadaItem) = (pic.IdParadaItem)
                inner join OrdenItem oi on (pi.IdOrdenItem = oi.IdOrdenItem)
                left join OrdenItem_Dyn oid on (oid.IdOrdenItem = oi.IdOrdenItem)
                WHERE pi.IdParada = p.IdParada
                FOR JSON PATH
                ) AS receptdetails
        from parada p 
        inner join DomicilioOrden d on (p.IdDomicilioOrden = d.IdDomicilioOrden)
        where p.IdParada = !!ID_ENTIDAD!!
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER,INCLUIDE_NULL_VALUES
    
.. container:: justified-text
    
    Para estructurar el SQL contaran con el apoyo del equipo DEV por medio de SOP o REQ según corresponda para estructurar lo que se necesite.
