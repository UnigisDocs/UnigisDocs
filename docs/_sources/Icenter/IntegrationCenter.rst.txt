Integrations Center
=======================

Descripción 
--------------

.. container:: justified-text

    Integrations Center es una sección que centraliza todas las funcionalidades referentes a las integraciones en una nueva pantalla reubicando mucho de los enlaces que se encontraban anteriormente en la pantalla de administrador.
    
    Todos los enlaces referentes a las integraciones estarán centralizados en un solo módulo.

Pre Requisitos
---------------

Disponer con una versión 10.215.0.0 o superior.

Información Técnica
---------------------

Tablas y Campos
~~~~~~~~~~~~~~~~~~

Se inserta un nuevo registro sobre la tabla “Application” la cual hará referencia al nuevo módulo de Integrations Center.

.. image:: icenter.png
   :align: center

Configuración 
-----------------

Es necesario configurar los permisos de acceso para el nuevo módulo para ello es necesario ingresar a :kbd:`Administrador del sistema` --> :kbd:`Grupos`

Seleccionar el grupo que desee actualizar y dar la opción de editar, posteriormente en la pestaña de aplicaciones se debe seleccionar el check de “IntegrationsCenter”.

.. image:: check.png
   :align: center

Esto se debe aplicar para todos los grupos que requieran acceder a este nuevo módulo.

.. note::

  Se debe validar que el usuario que estas utilizando cuentas con los permisos para acceder al módulo para ello se debe de ir a la siguiente ruta: :kbd:`Administrador del sistema` --> :kbd:`Grupos`
  
  Seleccionar el grupo de tu usuario y verificar que se tenga el check activo de Integrations Center 


Forma de Uso 
--------------

Se podrá acceder al módulo de integraciones desde dos secciones diferentes, desde el menú lateral, o desde el menú de Log Out, ambos seleccionando la opción de Integrations Center.

.. image:: icenter2.png
   :align: center

Al dar clic en alguna de estas opciones se abrirá el nuevo módulo mostrando la siguiente pantalla.

.. image:: icenter3.png
   :align: center

.. container:: justified-text

    Es importante recalcar que los enlaces no tuvieron algún cambio, simplemente se centralizaron en una nueva pantalla, en la sección de MAP Web Services se agregan los enlaces de los WS services, se agrega también la sección de Documentación y la Api Key la cual indicará la clave actual y el estatus si esta activa o desactivada la validación de Api Key esta será de solo lectura y si requieres actualizar su valor se deberá seguir actualizando desde la sección de parámetros.

    La lista de MAPI Web Services enviarán a los siguientes enlaces.

.. list-table:: webservice
    :widths: 10 45
    :header-rows: 1

    * - WebService 
      - Link
    * - Infor 
      - {URL_Base_UNIGIS}/Mapi/INFOR/Service.asmx
    * - SAP	
      - {URL_Base_UNIGIS}/Mapi/SAP/Service.asmx
    * - SOAP Audit	
      - {URL_Base_UNIGIS}/Mapi/SOAP/Audit/Service.asmx
    * - SOAPAuth	
      - {URL_Base_UNIGIS}/Mapi/SOAP/Auth/Service.asmx
    * - SOAP CommServer	
      - {URL_Base_UNIGIS}/Mapi/SOAP/CommServer/Service.asmx
    * - SOAP Geographic	
      - {URL_Base_UNIGIS}/Mapi/SOAP/Geographic/Service.asmx
    * - SOAP Gepgraphic Admin	
      - {URL_Base_UNIGIS}/Mapi/SOAP/Geographic/Admin/Service.asmx
    * - SOAP GPS	
      - {URL_Base_UNIGIS}/Mapi/SOAP/GPS/Service.asmx
    * - SOAP Logistic	
      - {URL_Base_UNIGIS}/Mapi/SOAP/Logistic/Service.asmx
    * - SOAP Logistic English	
      - {URL_Base_UNIGIS}/Mapi/SOAP/Logistic/EN/Service.asmx
    * - SOAP Stock	
      - {URL_Base_UNIGIS}/Mapi/SOAP/Stock/Service.asmx
    * - SOAP Timezone	
      - {URL_Base_UNIGIS}/Mapi/SOAP/TimeZone/Service.asmx

.. container:: justified-text

    Al generar este nuevo módulo algunos links ya no serán visibles desde el módulo “Administrador del Sistema”, y solo serán visibles desde “Integrations center”.

    Se adjunta tabla donde se resalta las secciones eliminadas con el comparativo de donde se podrá visualizar ahora, ya que algunas opciones fueron renombradas para tener un nombre más claro de la acción que realiza.

.. list-table:: opciones
    :widths: 10 45
    :header-rows: 1

    * - Pantalla Administrador Versión Anterior
      - Pantalla Integrations Center
    * - :kbd:`Integraciones` --> :kbd:`Sistema Externo`	
      - :kbd:`SyncOut` --> :kbd:`Configuración SyncOut`
    * - :kbd:`Integraciones` -> :kbd:`OCR`	
      - NOTA: Se omite la pantalla que redirige a los subenlaces de OCR y los enlaces se muestran de forma directa en la nueva pantalla. (:kbd:`OCR` --> :kbd:`OCR Credenciales`).   (:kbd:`OCR` --> :kbd:`OCR Formato`).  (:kbd:`OCR` --> :kbd:`OCR Log`).
    * - :kbd:`Integraciones` --> :kbd:`SAT`
      - NOTA: Se omite la pantalla que redirige a los subenlaces de SAT y los enlaces se muestran de forma directa en la nueva pantalla. (:kbd:`SAT` --> :kbd:`Catálogo Integraciones SAT`). (:kbd:`SAT` --> :kbd:`Entidad Integración SAT`). (:kbd:`SAT` --> :kbd:`Estructura Integraciones SAT`). (:kbd:`SAT` --> :kbd:`Log Integraciones SAT`).
    * - :kbd:`Integraciones` --> :kbd:`RNDC`
      - NOTA: Se omite la pantalla que redirige a los subenlaces de RNDC y los enlaces se muestran de forma directa en la nueva pantalla (:kbd:`RNDC` --> :kbd:`Documento Integración`).   (:kbd:`RNDC` --> :kbd:`Monitor RNDC`).  (:kbd:`RNDC` --> :kbd:`Entidad Integración`). (:kbd:`RNDC` --> :kbd:`Log Integración RNDC`). (:kbd:`RNDC` --> :kbd:`Proceso RNDC`).
    * - :kbd:`Integraciones` --> :kbd:`Integraciones`	
      - :kbd:`Integraciones Logs` --> :kbd:`Logs / Bitacoras`
    * - :kbd:`Integraciones` --> :kbd:`MAPI`
      - :kbd:`MAPI Web Services` --> :kbd:`MAPI Asincrónica`
    * - :kbd:`Sistema` --> :kbd:`Hojas Configuración`
      - :kbd:`Sistema` --> :kbd:`Hojas Configuración`
    * - :kbd:`Sistema` --> :kbd:`Parámetros`
      - NOTA: Se omite la pantalla que redirige a los subenlaces de parámetros y los enlaces se muestran de forma directa en la nueva pantalla. (:kbd:`Sistema` --> :kbd:`Parámetros). (Sistema` --> :kbd:`App Config`).

Se adjunta imagen con la nueva posición y nombre de los enlaces en la pantalla Integrations Center.

.. image:: icenter4.png
   :align: center

En la sección Api Key se mostrará la clave, e indicará cuando la validación se encuentre activa o inactiva.

.. image:: icenter5.png
   :align: center   

El valor de la validación activa o inactiva se obtiene del config de la key “ValidarApiKey_MAPI”.


Al acceder a cualquier enlace referente a integrations center se mostrará con el nuevo menú referente solo a los enlaces de integrations center.

Ejemplo 
-------------

Al acceder a cualquier enlace referente a integrations center se mostrará con el nuevo menú referente solo a los enlaces de integrations center.

.. image:: ejemplo.png
   :align: center

