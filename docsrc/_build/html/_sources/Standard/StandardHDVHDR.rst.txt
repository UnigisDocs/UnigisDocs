Standard HDV & HDR
======================

Descripción
--------------
.. container:: justified-text

    Unigis Reports es un componente que facilita la información de manera estándar de manera inicial, pero con facilidad de ajustar la información de acuerdo con las necesidades presentadas para cada operación dentro de la planificación o seguimiento del viaje.

Objetivos
-------------

.. container:: justified-text

    - Incluir en el abanico de soluciones de UNIGIS, la generación de reportes estándar para detallar la planificación de la ruta y hacer el correcto seguimiento del viaje.
    
    - Contar con una plantilla para la implementación de reportes “Custom” y se adapten a las operaciones del cliente.
    
    - Mitigar la solicitud de hojas Custom.

Desarrollo
-------------

.. container:: justified-text

    Se actualiza un solo formato estándar de hoja de ruta y hoja de viaje. Esto permite contar con reportes adaptados por operación, lo que genera un ahorro significativo en el costo del proyecto de implementación y facilita la implementación de UNIGIS para nuevos clientes.

    - Dev Express (Reporteador). El Reporteador DevExpress (Core) es una herramienta para generar informes en aplicaciones web basadas en ASP.NET Core. Se Ofrece una amplia gama de características y controles que facilitan la creación de informes personalizados y visualmente atractivos. Con el reporteador DevExpress, es posible diseñar, exportar y personalizar informes utilizando una interfaz de usuario intuitiva y flexible.

    - Microsoft.NET. 

    - Angular Js

Parámetros
------------

Disponer con los permisos (ModuloConfigurationSheets) necesarios para visualizar la opción "Hojas Configuración" correspondiente al componene Unigis Reports.

:kbd:`Integrations Center` --> :kbd:`Sistema` --> :kbd:`Hojas Configuración`


.. image:: rutareports.png
   :align: center

Forma de Uso
------------------

.. container:: justified-text

    Las hojas de configuración pueden adaptarse o reutilizarse dependiendo de su operación, mostrando diferentes datos necesarios para su correcta ejecución. Además, al seleccionar el botón de :kbd:`+`, se puede crear una nueva configuración por tipo de hoja que se desea.

    :kbd:`lupa` Realiza una búsqueda por nombre y/o operación de la hoja que desea encontrar.

    :kbd:`lápiz` Permite abrir el formulario para editar la configuración del reporte.

    :kbd:`bote` Elimina el registro seleccionado.

.. image:: hojas.png
   :align: center

Configuración
~~~~~~~~~~~~~~~~~~~~

.. container:: justified-text

    La pestaña de configuración presenta dos opciones de reporte: una hoja de ruta o un viaje. En ambos casos, la descripción es un campo obligatorio que se utiliza como un campo de texto libre para detallar el tipo de reporte. Cada campo del reporte está relacionado dentro de un apartado que se integra automáticamente en el reporte seleccionado. Los apartados y campos que se muestran son los siguientes:

    - Emisión de Hoja. Empresa, Dirección, Sucursal, Email, Teléfono, Fecha Hora Creación, Viaje Número y Código QR.
        
    - Información de Ruta. Fecha Hora Inicio de Ruta, Tipo de Vehículo, Depósito de Salida, Kms Planificados, Fecha Hora Fin de Ruta, Dominio, Domicilio de Salida, Total de Ítems a Entregar, Transporte, Categoría Vehículo, Depósito de Llegada, Muelle, Nombre del Conductor, Nombre del Acompañante, Ruta y Jornada.
        
    - Órdenes. Número de Orden, Referencia Externa, Fecha de Entrega, Razón Social, Nombre de Cliente, Descripción, Domicilio de Entrega, Número de Entrega, Número de Parada, No. Pedido/Guía/Factura, Cantidad Ítems, Unidad de Medida, Cantidad Ítem, Peso, Volumen, Bultos, Pallets, Importe, Firma de Entregad y Firma de Recolectado.
        
    - Cantidades Totales. Entregas a Realizar, Ítems, Peso, Volumen, Bultos y Pallets.
        
    - Anexos y Firmas. Observaciones, Firma del Conductor, Firma Despachador Receptor, Firma Receptor y Texto Legal.

    - Logotipo. Además, para mejorar la visualización del reporte, se brinda la opción de cargar un archivo PNG que sirva como logotipo representativo de la empresa u operación correspondiente. Esta función ayuda a personalizar y dar identidad al reporte.

.. image:: configuracion.png
   :align: center

Operaciones
~~~~~~~~~~~~~~~~~~

.. container:: justified-text

    En la hoja de configuración actual, se seleccionan una o varias operaciones previamente creadas que correspondan a la hoja configuración específica

.. image:: operaciones.png
   :align: center


.. container:: justified-text

    Al seleccionar el botón :kbd:`Ver vista previa` del reporte, se visualiza una nueva ventana con la vista del reporte seleccionado y con la configuración para visualizar de manera general un preview de lo que se requiere o necesita. 

.. image:: vistaprevia.png
   :align: center