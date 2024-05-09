Syncout V2
=======================

Descripción 
--------------

.. container:: justified-text

    La siguiente Guía de configuración y uso de ABM JSON SYNCOUT V2, servirá para comprender la funcionalidad, información técnica, Configuración paso a paso, así como la descripción de la funcionalidad a detalle y organizada con la finalidad de que sea comprensible en todos los niveles y tener al alcance la información que pueda ser de utilidad en cualquier momento.

    **Habilitar Permisos para uso de Integrations Center**

    Es necesario configurar los permisos de acceso para el nuevo módulo para ello es necesario ingresar a :kbd:`AdministradordelSistema` --> :kbd:`Grupos`. Seleccionar el grupo que desee actualizar y dar la opción de editar, posteriormente en la pestaña de aplicaciones se debe seleccionar el check de :kbd:`IntegrationsCenter`.

.. image:: config.png
   :align: center

.. note::

    Esto se debe aplicar para todos los grupos que requieran acceder a este nuevo módulo.

Funcionalidad
---------------

.. container:: justified-text

    Se puede acceder al módulo de integraciones desde dos secciones diferentes, desde el menú lateral, o desde el menú de Log Out, ambos seleccionando la opción de :kbd:`IntegrationsCenter`.

    Al dar clic en alguna de estas opciones se abrirá el nuevo módulo mostrando la siguiente pantalla y seleccionaremos la opción de Syncout.

.. image:: integrationsyncout.png
   :align: center

.. container:: justified-text

    Dependiendo de los sistemas externos que se tengan creados se debe de dar clic en el incono señalado para realizar la configuración del Json Syncout.

.. image:: señalar.png
   :align: center

.. container:: justified-text

    A continuación se muestra una lista de las configuraciones realizadas y para agregar una nueva debe dar clic al icono de :kbd:`+`.

.. image:: agregar.png
   :align: center

.. container:: justified-text

    Al dar clic se mostrará una pantalla con los campos a llenar y configurar el Json que se necesita para hacer las peticiones así como la Query para la obtención de los datos para generar el request. 

    1. Primeramente en “Descripción sistema externo” podemos ver el nombre del sistema externo al que daremos de alta el Syncout.
    
    2. Enseguida un combo donde se muestran las entidades posibles para configurar ejemplo: SistemaExternoModificarEstadoViajeSalida.

.. image:: formulario.png
   :align: center

.. container:: justified-text

    Al seleccionar en el combo de “Sistema Externo” y “Sistemas configurados” mostrará las configuraciones en la tabla de salida ejemplo: SistemaExternoModificarEstadoViajeSalida.

    La descripción se mostrará: identidad (IdSistemaExternoSalidaModificarEstadoViaje) separado de ‘|’ enseguida del estado de la entidad (EstadoViaje) separado de ‘|’ y por último el sistema externo. 

.. image:: formulario2.png
   :align: center

.. note::
    
    Cabe destacar que el combo es multiseleccionable por lo que con una sola configuración se pueden dar de alta todos los cambios de estado de una entidad y así evitar subir una configuración por cada cambio de estado.

.. container:: justified-text

    Una vez seleccionado la configuración de la tabla de salida se comienza con la configuración del Json que se creara para las peticiones al WebServices del cliente.

    En primer lugar, se muestra caja de texto ‘URL’ en ella se colocará la Url del WebServices que se necesita para la autenticación ya sea para obtener un token.

.. note::
    
    Cabe recalcar que conforme se tenga la documentación del cliente para su Syncout son los parámetros que se configuraran.

.. image:: formulario3.png
   :align: center

.. container:: justified-text

    El siguiente apartado se llama ‘Replace’ aquí se configura cuando en la Url que proporcionan tiene parámetros para reemplazar ejemplo : https://prueba/wmtst/wmwebservice_rest_oltp/@WareHouse/shipments

    Se deben completar los campos:

    - Key (es el parámetro a remplazar que forma parte de la Url)
    - Entidad (entidad o tabla a la cual se va a hacer referencia para obtener el campo)
    - Campo (es el campo de la entidad que se va a obtener para reemplazar en la URL)

.. image:: formulario4.png
   :align: center

.. image:: formulario5.png
   :align: center

.. container:: justified-text

    Una vez que se completen estos datos se verán reflejados en el Json de esta forma.

.. code-block:: Json
    :linenos:
    
    {
        "Json" : [
            {
                "URL":{
                    "URI": "http://wmstest.iflow.corp./wmtst/wmwebservice_rest_oltp/@wareHouse/shipments",
                    "Replace":[
                        {
                            "Key": "@WareHouse",
                            "Entity": "DepostioSalida",
                            "Field": "ReferenciaExterna"
                        }
                    ]
                ]

.. container:: justified-text

    Cada vez que se requiera agregar un parámetro más se debe dar clic en el signo :kbd:`+` en caso contrario de borrar un parámetro dar clic al icono de borrar.

.. image:: replace.png
   :align: center

.. image:: replace2.png
   :align: center

.. container:: justified-text

    Otra sección más del llenado del Json es “Headers” en el cual se agregarán que necesite el web services. Cada vez que se quiera agregar un header se debe dar clic en el icono :kbd:`+` o si se necesita quitar dar clic al icono :kbd:`Borrar`.

.. image:: replace3.png
   :align: center

.. container:: justified-text

    Los datos se observarán de la siguiente forma:

.. code-block:: Json
    :linenos:

            "Headers": [
              {
                "Key": "Accept-Encoding",
                "Value": "gzip, deflate, br",
              }
            ]

.. container:: justified-text

    El siguiente Apartado es ‘Paramsbody’ en el cual se agregaran todos los parametros que se tienen que configurar en el body.

    Para agregar se debe dar click en el icono :kbd:`+` y para quitar es con el icono de :kbd:`Borrar`.
 
 .. image:: params.png
   :align: center

.. code-block:: Json
    :linenos:

        "ParamsBody": [{
            "Key": "",
            "Value": ""
        }],

.. container:: justified-text

    El siguiente apartado es la selección de combos los cuales son:

    Método: Se elegirá el tipo de método del webservices

.. image:: método.png
   :align: center

.. container:: justified-text

    Tipo de método : Se elegirá el tipo de contenido 

    Aceptar: este encabezado es tipo de respuesta del servidor puede aceptar un cliente.
 
    Auth: el tipo de autenticación a la que está configurado el web services 

    Envió único:
    
    Para agregar credenciales en el caso de requerir ejemplo un usuario y contraseña agregarlos en este apartado dando clic en el icono (+) y para eliminar en icono borrar.

    La configuración de este apartado se verá así en el Json.

.. code-block:: Json
    :linenos:

        "Credentials": [
            {
                "Key": "User",
                "Value": "Pruebas"
            },
            {
                "Key": "Password",
                "Value": "1234"
            }]

.. container:: justified-text

    Para agregar otro Json el cual se encargará de hacer la petición al WebServices debe configurarse por lo cual se dará clic en el botón agregar Json

.. image:: nuevo.png
   :align: center

Al dar clic copiara la pantalla y clonara otro apartado esto para configurar el segundo JSON.

.. image:: nuevo2.png
   :align: center

Al terminar la configuración del segundo Json se debe dar clic en botón :kbd:`ComprobarJson`.

Esto creara el Json de acuerdo con lo configurado.

.. image:: comprobar.png
   :align: center

En la siguiente imagen se muestra como se ve el Json al ser configurado:

.. image:: configjson.png
   :align: center

Al final se debe de crear una consulta en SQL la cual va a recabar los datos que se van a enviar al webservices a reportar. Y una vez finalizado dar clic en el botón de crear.

.. image:: final.png
   :align: center



