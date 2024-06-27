FAQs
=======

Aquí presentamos las respuestas a algunas de las preguntas frecuentes sobre nuestro producto UNIGIS TMS.

.. raw:: html 

 <html>
 <head>
   <style>
       .inline-list li { display: inline; }
       .special-link { cursor: pointer; }
       #searchInput {
           width: 100%;
           padding: 10px;
           margin-bottom: 20px;
           background-color: white;
           color: black;
           border: 1px solid #ccc;
           border-radius: 4px;
       }
   </style>
 </head>
 <body>
   <input type="text" id="searchInput" onkeyup="filterQuestions()" placeholder="Búsqueda">

   <script>
       function filterQuestions() {
           var input = document.getElementById('searchInput');
           var filter = input.value.toLowerCase();
           var questions = document.querySelectorAll('.question');
           var sectionTitles = document.querySelectorAll('.section-title');

           questions.forEach(function(question) {
               var text = question.textContent || question.innerText;
               if (text.toLowerCase().indexOf(filter) > -1) {
                   question.style.display = '';
               } else {
                   question.style.display = 'none';
               }
           });

           sectionTitles.forEach(function(title) {
               var section = title.nextElementSibling;
               var visibleQuestions = section.querySelectorAll('.question:not([style*="display: none"])');
               if (visibleQuestions.length > 0) {
                   title.style.display = 'block';
               } else {
                   title.style.display = 'none';
               }
           });
       }

       document.addEventListener('DOMContentLoaded', function() {
           var specialLinks = document.querySelectorAll('.special-link');
           specialLinks.forEach(function(link) {
               link.addEventListener('click', function(event) {
                   var tag = event.target.getAttribute('data-tag');
                   var questions = document.querySelectorAll('.question');
                   questions.forEach(function(question) {
                       question.style.display = 'none';
                   });
                   var taggedQuestions = document.querySelectorAll('.question.' + tag);
                   taggedQuestions.forEach(function(question) {
                       question.style.display = 'block';
                   });
               });
           });
           var questions = document.querySelectorAll('.question');
           questions.forEach(function(question) {
               question.style.display = 'block';
           });
       });
   </script>

.. raw:: html

   <h2 class="section-title">MAPI</h2>
   <div class="section-content">
       <details class="question mapi apikey webservice">
           <summary class="card-header">¿Cómo se Configura "ApiKey" para WebService de MAPI?</summary>
          <ul class="inline-list">
          <li><a href="javascript:void(0)" class="special-link" data-tag="mapi">MAPI</a></li>
          <li><a href="javascript:void(0)" class="special-link" data-tag="apikey">ApiKey</a></li>
          <li><a href="javascript:void(0)" class="special-link" data-tag="webservice">WebService</a></li>
          </ul>
           <p>La ApiKey por default es la misma que MAPI TOKEN (Ver "Estado Del Sistema").</p>
           <p>Por defecto UNIGIS NO la valida, para activar la validación se debe configurar en App.Config de UNIGIS Web el siguiente paramatro en True: "ValidarApiKey". (add key="ValidarApiKey" value="true")</p>
       </details>

       <details class="question mapi webservice">
           <summary class="card-header">¿Existe algún WebService para obtener Distancias por calles?</summary>
           <ul class="inline-list">
           <li><a href="javascript:void(0)" class="special-link" data-tag="mapi">MAPI</a></li>
           <li><a href="javascript:void(0)" class="special-link" data-tag="webservice">WebService</a></li>
           </ul>
           <p>Si, se debe utilizar el método "BuscarTrayecto" de MAPI GeoGraphic.</p>
           <p>El método recibe Origen y Destino.</p>
           <p>Retorna el Tiempo en Minutos considerando la velocidad por tipo de vial (Según el perfil de Routed), Distancia y una Lista de Puntos que es el recorrido visual para desplegar en un mapa.</p>
       </details>
   </div>

   <h2 class="section-title">Tracking</h2>
   <div class="section-content">
       <details class="question tracking alarmas">
           <summary class="card-header">¿Cómo generar una alarma cuando se va llegar tarde a una parada?</summary>
           <ul class="inline-list">
           <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
           <li><a href="javascript:void(0)" class="special-link" data-tag="alarmas">Alarmas</a></li>
           </ul>
           <p>Es necesaria una alarma que evaluara si se llega a tiempo a la fecha planificada y que si este viaje no llega lanzaba una alarma.</p>
           <p>Este control lo realiza el modulo de Control de Viajes de Control console.</p>
           <p>El control analiza los viajes en estado de seguimiento activo cuyo donde las paradas tengan una diferencia entre la fecha Estimada y la Fecha Planificada mayor (en minutos) al parametro DesvioMaximoParadaDesvio (15 minutos default) O el campo DesvioMaximo de la tabla parada.</p>
       </details>

       <details class="question tracking archivos">
           <summary class="card-header">¿Cómo subir archivos relacionadas a una Parada mediante POST?</summary>
           <ul class="inline-list">
           <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
           <li><a href="javascript:void(0)" class="special-link" data-tag="archivos">Archivos</a></li>
           </ul>
           <p>Upload = "1"</p>
           <p>IdParada = “IdParada”</p>
           <p>Token = Token de acceso a UNIGIS.</p>
           <p>Para obtener el token de un usuario, se puede usar el Servicio MAPI/Soap/Auth/Service.asmx método Login.</p>
       </details>

   <details class="question tracking">
    <summary class="card-header">¿En qué momentos se recalcula los tiempos estimados de llegada de un viaje?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       </ul>    
    <p>En cambio de Estado de Parada cuando el estado destino es del tipo anulacion ( EstadoParada.Anulacion = 1).</p>
    <p>Al momento de Activar el viaje.</p>
    <p>En el servicio CalcularViaje de MAPI Logistic.</p>
    <p>Al momento de agregar o eliminar una parada de forma manual al viaje desde Tracking.</p>         
    <p>Luego de reordenar el viaje desde Tracking o Mobile.</p>
    <p>Luego de cambiar una parada de un viaje a otro desde Tracking.</p>
  </details>

   <details class="question tracking alarmas">
    <summary class="card-header">¿Cómo funciona la Criticidad, TimeOut y nivel de alarmas acumuladas en Tracking?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="alarmas">Alarmas</a></li>
       </ul> 
    <p>La criticidad está asociada al tipo de alarma y sirve para clasificar la importancia o urgencia en función de cada tipo de alarma. Se configura en la tabla Criticidad y se apunta en TipoAlarma.IdCriticidad. Es fija por tipo de alarma; nunca una alarma cambia de criticidad.</p>
    <p>El timeout se configura en TipoAlarma y representa el tiempo que tiene cada alarma, según su tipo, para ser tratada. Las alarmas no escalan; simplemente, en tracking, el campo TimeOut cambia de color si se supera ese tiempo en minutos desde su creación hasta que es tratada.</p>
    <p>El campo CantidadAlarmasNoTratadas en la tabla Vehículo se incrementa con cada nueva alarma no tratada automáticamente (TipoAlarma.TratamientoAutomatico). Este valor se decrementa cuando una alarma es tratada. En tracking, se muestra en dos momentos: </p>
    <p>Cantidad total de alarmas no tratadas: Se visualiza al hacer clic en "Alarmas" en el panel superior, en la pestaña "Vehículos". Es el acumulado total en la base de datos (Vehículo.CantidadAlarmasNoTratadas).</p>
    <p>Cantidad de alarmas no tratadas desde el inicio: Se muestra desde que el usuario abre UNIGIS Tracking.</p>
    <p>Estos valores pueden cambiar de color según su importancia, definido en la tabla NivelAlarmasAcumuladas, donde se establece el color por cada rango.</p>
      </details>
   
   <details class="question tracking alarmas">
    <summary class="card-header">¿Cómo se desactiva los PopUps de alarmas en Tracking?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="alarmas">Alarmas</a></li>
       </ul> 
    <p>Para desactivarlo globalmente existe el parámetro (Tabla Parámetros) "IdTipoAlarma_PopUp".</p>
    <p>En dicho parámetro se pueden configurar que tipos de alarmas son los habilitados para el pop up. En el caso que este vacío entonces TODOS los tipos de alarma generar el PopUp al usuario.</p>
    <p>Se debe completar con una lista separada por "," de los ID de tipo alarma que se quieran notificar via popup. Ejemplo: </p>
    <pre><code>&lt;system.net&gt;
    &lt;defaultProxy&gt;
    &lt;proxy proxyaddress="http://220.26.11.3:3128" bypassonlocal="true" /&gt;
    &lt;/defaultProxy&gt;
    &lt;/system.net&gt;</code></pre>
      </details>
   
   <details class="question tracking rutas">
    <summary class="card-header">¿Por qué no se puede visualizar el módulo de rutas en Tracking?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="rutas">Rutas</a></li>
       </ul> 
    <p>Se debe validar los permisos para la visualización del módulo de rutas, en caso de disponer con los permisos y aún no es visible, se debe validar que el parámetro (Tabla parámetro) con clave = "cfg0" tenga el valor (1). En caso de modificar ese valor por base de datos y no por administración del sistema se debe reiniciar el cache del servidor web.</p>
    </details>

   <details class="question tracking">
    <summary class="card-header">No inicia UNIGIS Tracking con error "The type initializer for..."</summary>
           <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       </ul> 
    <p>Para aquellos servidores donde existen mas sitios Web, se recomienda reciclar el pool de aplicaciones utilizados por UNIGIS, asi no se ven afectados todos los sitios por causa del restart del IIS.</p>
    </details>

   <details class="question tracking gps">
    <summary class="card-header">¿Cuál es la diferencia entre FechaHoraEvento, FechaHoraRecepcion, FechaHoraReportado y FechaHoraCalculada?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="gps">GPS</a></li>
       </ul> 
    <p>Respecto a las posiciones GPS recibidas desde los prestadores, a continuación se describen detalles de los campos de fecha de la tabla EVENTO:</p>
    <p>FECHAHORAEVENTO. Dato reportado por el GPS y corresponde al valor informado directamente a través del web método responsable de insertar los eventos. Este el valor desplegado en aplicación Tracking.</p>
    <p>FECHAHORARECEPCION. Teóricamente es la fecha de cuando el prestador proceso el dato informado por el GPS. Este valor es entregado por el prestador a través de web método que procesa las transmisiones, se identifica que en algunos casos informan el mismo valor de FECHAHORAEVENTO.</p>
    <p>FECHAHORAREPORTADO. Fecha y hora de cuando se procesó el dato en base de datos de UNISOLUTIONS.</p>
    <p>FECHAHORACALCULADA. Corresponde al dato reportado por el GPS calculado en base la huso horario configurado para el prestador.</p>
    </details>

   <details class="question tracking paradas">
    <summary class="card-header">¿Cómo se calcula el desvío de un viaje?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="paradas">Paradas</a></li>
       </ul> 
    <p>Se calcula en función de la próxima parada de un viaje ( Viaje.IdParadaSiguiente )</p>
    <p>Si la próxima parada de un viaje tiene FinVisitaReal, se calcula la diferencia entre el horario real y el planificado ( FinVisitaPlanificado )</p>
    <p>Si no tiene horario planificado se utiliza el horario estimado ( Parada.FinVisita )</p>
    </details>

   <details class="question tracking">
    <summary class="card-header">¿Cómo se configura una alarma cuando se supera el desvío de un viaje?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       </ul> 
    <p>Este control lo realiza el modulo de Control de Viajes de Control console.</p>
    <p>El control analiza los viajes en estado de seguimiento activo cuyo Viaje.Desvio sea mayor a su desvío máximo ( Viaje.Seguimiento.DesvioMaximo )</p>
    <p>Viaje.Desvio > Viaje.Seguimiento.DesvioMaximo</p>
    <p>Se debe configurar el parámetro IdTipoAlarmaDesvio en la entidad parámetro indicando el id de tipo de alarma a generarse cuando se genere la detección.</p>
    </details>

   <details class="question tracking">
    <summary class="card-header">¿Como se activa un viaje de forma automática?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       </ul> 
    <p>Los viajes podrán activarse automáticamente usando ControlConsole. Para tal fin se deberá contar con el parámetro ControlGeneral y ControlActivacionViajes en True.</p>
    <p>•	Criterio activación: se activará un viaje al salir de un deposito (en otras palabras, un dibujo con condición 10 o 4, "inicio fin de viaje" o "inicio viaje" ). A su vez dicho seguimiento tiene que estar en estado inactivo.</p>
    <p>•	Criterio desactivación de viajes: entrada a un deposito (dibujo con condición 10 o 6,  "inicio fin de viaje" o "fin de viaje"). A su vez se valida que el seguimiento este activo, adicionalmente se valida lo siguiente:</p>
    <p>- Si el viaje tiene paradas, y todas están pendientes no lo cierro. </p>
    <p> - Si no tiene paradas me fijo la fecha de inicio real. Le doy 30' mins de gracia.</p>
    </details>

   <details class="question tracking paradas">
    <summary class="card-header">¿Como se configura el flujo de Paradas para cambiar el estado cuando un vehículo visita una parada?</summary>
           <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="tracking">Tracking</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="paradas">Paradas</a></li>
       </ul> 
    <p>En configuración del console poner el parametro "ControlEstadiaParada" = true y configurar la transicion de pendiente a visitado en el flujo de cambios de estados de paradas</p>
    </details>
   </div>

   <h2 class="section-title">Alarmas</h2>
   <div class="section-content">
   <details class="question alarmas notificaciones">
       <summary class="card-header">¿Cómo notificar Alarmas por Email o SMS?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="alarmas">Alarmas</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="notificaciones">Notificaciones</a></li>
       </ul>
       <p>Se debe configurar dentro del Administración del Sistema -> Alertas -> Tipo Alarmas. Se debe marcar el tipo de alarma como "Notificable" y luego entrar al modulo de notificaciones, configurar el tipo de gateway (SMS o Email ), destinatarios y contenido de correo.</p>
       <p>El módulo Control Console debe estar activo con el parámetro en App.Config de notificaciones activo.</p>
   </details>
   </div>

   <h2 class="section-title">DataBase</h2>
   <div class="section-content">
   <details class="question database memoria cache">
       <summary class="card-header">¿Por qué luego de modificar un valor por base de datos, el sistema sigue mostrando un dato antiguo?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="database">DataBase</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="memoria">Memoria</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="cache">Caché</a></li>
       </ul>
       <p>UNIGIS mantiene un cache para muchas entidades (Parámetro, EstadoParada, EstadoViaje, TipoVehiculo), generalmente aquellas con muchas operaciones de lectura (READ) y no una cantidad enorme de registros (tablas maestras, de workflow o parámetros). Este cache se utiliza para evitar leer constantemente la base de datos.</p>
       <p>El cache está en memoria en el servidor web, por lo que si se modifica el valor directamente en la base de datos, la aplicación web no tiene forma de saberlo. Sin embargo, si una de estas entidades se modifica a través de la interfaz de usuario (UI), el cache se regenera.</p>
       <p>En caso de dudas, NO REINICIAR IIS. En su lugar, ingresa a "Estado del Sistema" en /UNIGIS/Status (debes hacerlo localmente o con el usuario System) y haz clic en "Vaciar Cache".</p>
   </details>

   <details class="question database memoria cache">
       <summary class="card-header">¿Cuál es la forma de poder ver los mensajes XML que se reciben vía MAPI?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="database">MAPI</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="memoria">SOAP</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="cache">Integraciones</a></li>
       </ul>
       <p>En UNIGIS, existe un parámetro de configuración llamado LogRequestsLogistic el cual, al estar en estado "Verdadero" (True) logueara los requests recibidos por el servidor (siempre que el método consumido implemente esta opción).</p>
       <p>El registro se guarda en dos ubicaciones: Tabla LogMapi y en un XML que sera generado en la ruta por defecto de unigis en la sub carpeta \MAPI\Requests</p>
   </details>

   <details class="question database">
    <summary class="card-header">¿Qué es un changescript?</summary>    
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="database">DataBase</a></li>
       </ul>    
    <p>Un "changescript" es un conjunto de instrucciones utilizadas en el desarrollo de software y administración de bases de datos para describir y aplicar cambios específicos, como modificaciones en el esquema de la base de datos, actualizaciones de datos, o alteraciones en el código fuente de una aplicación. Estos scripts son esenciales para gestionar versiones, implementar actualizaciones, corregir errores y mejorar funcionalidades, permitiendo una aplicación controlada y ordenada de cambios en sistemas de software y bases de datos.</p>
    <p>Archivo del tipo .SQL, que contiene un conjunto de sentencias SQL que aplican en una actualización de versión de UNIGIS (a nivel de base de datos).</p>
    <p>Se define el siguiente formato estantar de nombre ChangeScript_VERSION_ORIGEN a VERSION_DESTINO. Ejemplo: ChangeScript_5.12.0.0 a 5.13.0.0</p>
    </details>
   
      <details class="question database viajes">
    <summary class="card-header">¿Como se relaciona un Viaje con una Ruta a nivel Base de Datos?</summary> 
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="database">DataBase</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="viajes">Viajes</a></li>
       </ul> 
    <p>La relación Viaje con Ruta es a través de los campos ( Viaje.IdRuta = Ruta.Ruta Y Viaje.IdJornada = Ruta.IdJornada  )</p>
    </details>
   </div>

   <h2 class="section-title">Resorce-Planner</h2>
   <div class="section-content">
   <details class="question Resource-Planner">
    <summary class="card-header">¿Cómo clasificar los conductores y vehículos en primarios y secundarios?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="Resource-Planner">Resource Planner</a></li>
       </ul>
    <p>Para ello existen los atributos en las entidades Conductor y vehículo. Los atributos son primario y secundario.</p>
    <p>El valor por defecto en vehículo es 1 en ambos casos.</p>
    <p>Dentro de Administración del Sistema -> Planeación -> Catálogos se puede modificar los valores de categoría para cada vehículo y conductor, el formulario de asignación manual.</p>
  </details>

   <details class="question Resorce-Planner">
    <summary class="card-header">¿Cómo configurar que un usuario pueda asignar vehículos y conductores a una ruta no asignados a la operación en planificación de recursos?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="fleet">Fleet</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="Resource Planner">Resource-Planner</a></li>
       </ul> 
        <p>Se debe Establecer el permiso via Action "IgnorarOperacion" del form "Fleet_Rutas"</p>
    </details>
   </div>

   <h2 class="section-title">Adapter</h2>
   <div class="section-content">
   <details class="question adapter viajes">
    <summary class="card-header">¿Cómo subir un archivo para que sea procesado por un Adapter de viajes?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="adapter">Adapter</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="viajes">Viajes</a></li>
       </ul> 
    <p>Se puede utilizar el uploader dentro de la aplicación web de UNIGIS en la ruta /UNIGIS/Apps/Viajes/UploadFile.aspx</p>
    <p>El archivo será subido al directorio /UNIGIS/Uploads/Shipments/, luego se deberá pedir configurar el Adapter de viajes para que procese desde ese directorio.</p>
    </details>

   <details class="question deploy web">
    <summary class="card-header">¿Cómo configurar UNIGIS Web a través de un proxy?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="deploy">Deploy</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="web">Web</a></li>
       </ul> 
    <p>Se debe establecer en <code>web.config</code> lo siguiente. Debe estar dentro de <code>Configuration</code> y NO en otro nodo interior. Ejemplo con proxy <code>220.26.11.3:3128</code>:</p>
    <pre><code>&lt;system.net&gt;
    &lt;defaultProxy&gt;
    &lt;proxy proxyaddress="http://220.26.11.3:3128" bypassonlocal="true" /&gt;
    &lt;/defaultProxy&gt;
    &lt;/system.net&gt;</code></pre>
    </details>
    </div>

   <h2 class="section-title">Routing</h2>
   <div class="section-content">
   <details class="question routing varonet">
    <summary class="card-header">¿Como funciona el tiempo de Inactividad en tipos de vehículos?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="routing">Routing</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="varonet">Varonet</a></li>
       </ul> 
    <p>El tiempo de inactividad está compuesto por cuatro geotipos:</p>
    <p>1. Inicio de Inactividad: Indica el inicio de la ventana horaria en la cual se puede asignar el tiempo de inactividad.</p>
    <p>2. Fin de Inactividad: Indica el fin de la ventana horaria en la cual se puede asignar el tiempo de inactividad.</p>
    <p>3. Tiempo Mínimo de Inactividad: si el conductor va a tomarse un descanso, el mismo debe estar justificado. Con este valor, uno indica cual es el tiempo mínimo que debe durar una ruta para validar la asignación de un descanso..</p>
    <p>4. Tiempo de Inactividad: Es el tiempo de descanso del vehículo que debe esperar para retomar sus tareas.</p>
    <p>Si alguno de estos cuatro valores llegara a ser negativo, se considera que el tipo de vehículo no tiene inactividad asignada.Siguiendo con la idea de tiempo mínimo de inactividad, no se va a asignar un descanso para un vehículo si este ya se lo tomó de alguna otra forma: </p>
    <p>•	Si dentro de una ruta se detecta una orden con un tiempo muerto igual o superior al tiempo de inactividad se considera que el descanso ya fue tomado y no se asignará.</p>
    <p>•	En el caso de haber segundas vueltas, si la diferencia entre el tiempo de llegada de una vuelta y el tiempo de salida de la siguiente es mayor o igual al tiempo de inactividad se considera que el descanso ya fue tomado y no se asignará en ninguna de las vueltas.</p>
    <p>•	Si el tiempo de inactividad fue asignado en la última vuelta de un vehículo y se encuentra al final de la ruta, el mismo será removido de la planificación, ya que se considera que el conductor puede descansar una vez finalizadas sus tareas. En caso de que la inactividad sea removida y la llegada al depósito ocurriera en un horario posterior al Fin de Inactividad se volverá a agregar ya que el conductor no se estaría tomando un descanso dentro de la ventana indicada.</p>
    <p>Estos geotipos únicamente se tienen en cuenta al realizar ruteos de deliveries o de recolecciones.</p>
    </details>

   <details class="question routing varonet">
    <summary class="card-header">¿Cómo funciona el reordenamiento automático de Rutas?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="routing">Routing</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="varonet">Varonet</a></li>
       </ul> 
    <p>Al reordenar automáticamente una ruta se corre sobre la misma, en una primera instancia, los optimizadores de Secuencia y Distancia, este último dos veces consecutivas. Al finalizar, intenta incorporar ordenes que hayan quedado sin rutear en la jornada.</p>
    <p>Como se pueden llegar a incorporar nuevas ordenes y el optimizador de Distancias se corre dos veces solamente, es posible encontrar mejores resultados si se corre nuevamente el reordenamiento.</p>
    <p>Los parámetros que se utilizan al reordenar son los que se encuentren cargados en el escenario de ruteo en ese momento, los cuales pueden llegar a diferir con los parámetros utilizados en el ruteo original por cambios realizados por el usuario.</p>
    </details>
   
   <details class="question routing varonet">
    <summary class="card-header">¿Cómo funciona el geotipo Grupo de Rutas y cuál es la diferencia con Grupo de Rutas Inclusivo?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="routing">Routing</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="varonet">Varonet</a></li>
       </ul> 
    <p>Al tener asignado el geotipo Grupo de Rutas, cada una de las rutas que se obtengan solo tendrán ordenes pertenecientes a un mismo grupo. De esta forma, ordenes con valor de grupo 1, por ejemplo, no podrán ser ruteadas con otras ordenes cuyo valor de grupo sea distinto, obteniendo como resultado rutas que pertenecen a distintos grupos.</p>
    <p>En caso de que el valor de este geotipo sea 0 para una orden, la misma será ignorada a la hora de rutear, ya que se entiende que no pertenece a ningún grupo.</p>
    <p>Por otro lado, el geotipo Grupo de Rutas Inclusivo tiene el mismo comportamiento que el geotipo anterior, pero difiere en su forma de tratar a las ordenes que tengan valor 0. Las mismas pueden ser incorporadas en cualquier ruta. Es decir, es posible obtener rutas con ordenes pertenecientes al grupo 1 y al grupo 0.</p>
    </details>
    </div>

   <h2 class="section-title">Mobile</h2>
   <div class="section-content">
   <details class="question mobile offline">
    <summary class="card-header">¿Cómo funciona Unigis Mobile Offline?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="mobile">Mobile</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="offline">Offline</a></li>
       </ul> 
    <p>Al perder la conexión se muestra la leyenda "Sin conexión - Intente más tarde".</p>
    <p>En caso de perder la conexión, todos los elementos relacionados con la entrega serán guardados. Las paradas confirmadas sin conexión, serán resaltadas en colo amarillo.</p>
    <p>Cuando el dispositivo vuelva a tener conexión, se sincroniza de manera automatica las paradas almacenadas. En caso de que haya quedado almacenada se puede utilizar el botón para actualizar.</p>
    </details>
   </div>

   <h2 class="section-title">Cartografía</h2>
   <div class="section-content">
   <details class="question cartografía mapserver">
    <summary class="card-header">¿Cómo se instala/actualiza un mapa en UNIGIS MapServer?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="cartografía">Cartografía</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="mapserver">MapServer</a></li>
       </ul> 
    <p>DEFINICIONES</p>
    <p>"...\UNIGIS MapServer\mapas\mapas.ini" ==> es el archivo de configuración donde se indica el nombre del mapa mediante el Id y su ruta de acceso donde se encuentra el MAPA.INI de cada mapa.</p>
    <p>"...\UNIGIS MapServer\mapas\mi_mapa\MAPA.INI" ==> archivo de configuración del mapa donde se indica el Id o Nombre con sus respectivas características.</p>   
    <p>"...\UNIGIS MapServer\mapas\mi_mapa\mi_mapa.AVF" ==> archivo de vista para el mapa que sirve para especificar como veremos nuestro mapa. En ella se especifica el Id del mapa, el zoom máximo y mínimo,la extensión del mapa y el estilo de cada layers.</p>
    <p>"...\UNIGIS MapServer\mapas\mi_mapa\mi_mapa_Routing.AVF" ==> archivo de vista del mapa para ruteo que sirve para especificar como veremos nuestro mapa (con menor detalles en zoom lejanos que el anterior). En ella se especifica el Id del mapa, el zoom máximo y mínimo,la extensión del mapa y el estilo de cada layers.</p>     
    <p>Al momento de actualizar el mapa se debe descargar el archivo comprimido de la consultora correspondiente. </p>
    <p>Pasos</p>
    <p>1. Descargar mapa en "...\UNIGIS MapServer\mapas" y descomprimir. Si existe ya el mapa reemplazarlo.</p>
    <p>2. Frenar el servicio/proceso de UNIGIS MapServer que vamos a actualizar el mapa.</p>
    <p>3. Borrar el archivo "árbol_mapas.ini". Lo que hace el "mapas.ini" es buscar la conexión con nuestros mapas. En el Id se indica el nombre de nuestro mapa, que lo encontramos en el archivo "MAPA.INI", sobre la linea "Id_mapa=". El path es la ruta de acceso donde se encuentra nuestro "MAPA.INI" y debe ser indicado como ".\mi_mapa". Tanto el Id_0 y Path_0 deben ser incrementado cada vez que se agregue un nuevo mapa.</p>
    <p>4. Seleccionamos nuestras vistas ubicadas en "...\UNIGIS MapServer\mapas\mi_mapa\" y lo copiamos a nuestra carpeta de "...\UNIGIS MapServer\usu\INTERNET\PORTALES\Vistas".</p>
    <p>5. Es necesario actualizar la vista ya que la información puede ser modificada, esto es, que se haya agregado o quitado información y por ende, el mapa y el orden de layers se modifica, por lo que nuestro mapa podría no verse de la manera correcta.</p>
    <p>En caso de actualizar el mapa, si la configuración es correcta, lo único que hay que hacer es reemplazar el mapa por la nueva versión, y su vista correspondiente.</p>
      </details>
   </div>

   <h2 class="section-title">Deploy</h2>
   <div class="section-content">
   <details class="question deploy">
    <summary class="card-header">¿Donde se encuentran los entregables de Producto, Instaladores, Customs y Cartografia?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="deploy">Deploy</a></li>
       </ul> 
    <p>Los entregables pueden encontrarse en los siguientes directorios:</p>
    <p>•	Producto: \\fs01\UNIGIS\Producto\Entregables</p>
    <p>•	Cartografia: \\fs01\UNIGIS\Cartografia\Finales</p>
    <p>•	Changescripts: \\fs01\UNIGIS\Producto\ChangeScripts</p>
    <p>•	Customs: \\fs01\UNIGIS\Customs</p>
    </details>
   </div>

   <h2 class="section-title">Control-Console</h2>
   <div class="section-content">
   <details class="question control-console parámetros">
    <summary class="card-header">¿Cómo se configuran los parámetros de App.config de Control Console?</summary>
       <ul class="inline-list">
       <li><a href="javascript:void(0)" class="special-link" data-tag="control console">Control-Console</a></li>
       <li><a href="javascript:void(0)" class="special-link" data-tag="parámetros">Parámetros</a></li>
       </ul>
    <p>- name="EntityFrameworkContext" -> Conexión a la base de datos.</p>
    <p>- name="ConnectionString" -> Conexión a la base de datos.</p>
    <p>- name="Usuario" -> se debera registrar un usuario administrador de la base de datos. (Tipicamente "Admin").</p>
    <p>- name="Delay" -> valor que determina un sleep en la operatoria del proceso. Se recomienda no modificar el valor.</p>
    <p>- name="SleepKmsVuelta" -> Valor en minutos que determina el tiempo para realizar la suma de kilómetros por vuelta.</p>
    <p>- name="ControlGeneral" -> booleano que enciende o apaga el control de vehículos (estadías en zona, activación automática, detenciones, distancia recorrida, punto cercano).</p>
    <p>- name="ControlNotificacion" -> enciende o apaga el envío de notificaciones.</p>
    <p>- name="ControlEstadiaParada" -> enciende o apaga el control de estadías.</p>
    <p>- name="ControlViajes" -> enciende o apaga el control de viajes (eta, desvío superado, arribo próximo, detención).</p>
    <p>- name="ControlActivacionViajes" -> enciende o apaga la activación automática de viajes.</p>
    <p>- Configuración de mapServer.</p>
    <p><!-- Map Server --></p>
    <p>(< add key="map_server_host" value="localhost" /> --> URL)</p>
    <p>(< add key="map_server_port" value="15000" /> --> Puerto)</p>
    </details>
   </div>