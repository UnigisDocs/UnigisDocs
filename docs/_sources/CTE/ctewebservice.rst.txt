Web Service CTE 
================

Descripción 
--------------

.. container:: justified-text

    Es un servicio que permite registrar los CTE (Conhecimento de Transporte Eletrônico) enviados por los clientes con base a la nueva estructura de datos. Con esto se permite enviar los CTE de una manera más eficiente aceptando el lenguaje XML con estructura en versión 3.0 y 4.0.

Pre Requisitos
----------------

- Disponer con la versión 10.216.0.0 o superior.

- Dar de alta el tipo idTipoDocumento con valor CTE en caso de no existir.

- Dar de alta el estado de documento con ReferenciaExterna “inicial” en caso de no existir. 
  
Información Técnica 
---------------------

Tablas y Campos
~~~~~~~~~~~~~~~~~~

- DocumentoCTEConfiguracion.

Descripción: Tabla que almacenará la configuración necesaria para hacer la consulta al servicio CTE.

.. list-table:: DocumentoCTEConfiguración
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdDocumentoCTEConfiguracion
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - CNPJConsulta	
      - Varchar 	
      - CNPJ enviado en el request de CTE.
    * - UFEConsulta	
      - Varchar 	
      - cUFAutor enviado en el request de CTE.
    * - RutaCertificado	
      - Varchar 	
      - Ruta del certificado.
    * - PasswordCertificado	
      - Varchar 	
      - Contraseña del certificado.
    * - UltimoNSURecuperado	
      - Varchar 	
      - NSU enviado en el request de CTE.
    * - FechaUltimaConsulta	
      - DateTime	
      - Fecha de última consulta enviada.
    * - RutaZIP	
      - Varchar
      - Ruta donde generará los archivos Zips recuperados por el servicio CTE.
    * - URLIntegracion	
      - Varchar	
      - Url del servicio CTE.

- CTEDocumento

Descripción: Tabla principal de CTE que almacenará en el encabezado principal del CTE, en el campo referenciaDocumento se almacenará el valor del path “ProtCTe/ chCTe” sobre el cual se validará la existencia del CTE.

.. list-table:: CTEDocumento
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdCTEDocumento 	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - IdDocumentoNFE 	
      - INT	
      - Llave foránea relacionado a la tabla DocumentoNFE.
    * - IdEstadoDocumento 	
      - INT	
      - Llave foránea relacionado a la tabla EstadoDocumento.
    * - IdTipoDocumento 	
      - INT	
      - Llave foránea relacionado a la tabla TipoDocumento.
    * - IdTipoModal 	
      - INT	
      - Llave foránea relacionado a la tabla TipoModal.
    * - IdTipoServicio 	
      - INT	
      - Llave foránea relacionado a la tabla TipoServicio.
    * - cUF 	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/cUF”.
    * - cCT 	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/cCT”.
    * - cFOP 	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/cFOP”.
    * - natOp   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/natOP”.
    * - mod   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/mod”.
    * - serie   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/serie”.
    * - nCT   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/nCT”.
    * - dhEmi  	
      - DateTime	
      - Mapeo xml path “CTe/InfCte/Ide/dhEmi”.
    * - tpImp  	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/tpImp”.
    * - tpEmis   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/tpEmis”.
    * - cDV   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/cDV”.
    * - tpAmb   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/tpAmb”.
    * - tpCTe   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/tpCTe”.
    * - procEmi   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/procEmi”.
    * - verProc   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/verProc”.
    * - indGlobalizado   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/ indGlobalizado”.
    * - cMunEnv   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/cMunEnv”.
    * - xMunEnv   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/xMunEnv”.
    * - uFEnv     	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/uFEnv”.
    * - cMunIni   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/cMunIni”.
    * - xMunIni   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/xMunIni”.
    * - uFIni    	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/uFini”.
    * - cMunFim  	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/cMunFim”.
    * - xMunFim  	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/xMunFim”.
    * - uFFim   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/uFFim”.
    * - retira  	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/retira”.
    * - xDetRetira  	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/xDetRetira”.
    * - indIEToma   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/indIEToma”.
    * - dhCont  	
      - DateTime	
      - Mapeo xml path “CTe/InfCte/Ide/dhCont”.
    * - xJust   	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/xJust”.
    * - dhSaidaOrig   	
      - DateTime	
      - Mapeo xml path “CTe/InfCte/Ide/ dhSaidaOrig”.
    * - dhChegadaDest   	
      - DateTime	
      - Mapeo xml path “CTe/InfCte/Ide/ dhChegadaDest”.
    * - NFEAsociada  	
      - Varchar	
      - Se almacena un valor vacío, se usará posteriormente para otros módulos.
    * - vTPrest   	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/vPrest/vTPrest”
    * - vRec   	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/vPrest/vRec”
    * - TotalMercancia   	
      - Decimal	
      - Guardar el total de la mercancía.
    * - TotalCobrar  	
      - Decimal	
      - Se almacena el valor cero, se usará posteriormente para otros módulos.
    * - ReferenciaDocumento	
      - Varchar	
      - Mapeo xml path “ProtCTe/chCTe”.
    * - RNTRC	
      - Varchar	
      - Mapeo xml Path “CTe/InfCte/InfModal/rodo/RNTRC”.
    * - qrCodCTe	
      - Varchar	
      - Mapeo xml Path “CTe/infCTeSupl/qrCodCTe”.


- TipoModal

Descripción: Tabla de tipo catálogo que sincronizará los diferentes tipos de Modal enviados en el XML.

.. list-table:: TipoModal
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdTipoModal	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - Descripcion	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/modal”.
    * - ReferenciaExterna	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/modal”.

- TipoServicio

Descripción: Tabla de tipo catálogo que sincronizará los diferentes tipos de Servicio enviados en el XML.

.. list-table:: TipoServicio
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdTipoServicio	
      - INT	
      - Llave primaria de la tabla autoincrementable.
    * - Descripcion	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/tpServ”.
    * - ReferenciaExterna	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/Ide/tpServ”.

- CTEDocumentoCarga

Descripción: Tabla que almacenará la información de la carga del CTE.

.. list-table:: CTEDocumentoCarga
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * -	IdCTEDocumentoCarga	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * -	IdCTEDocumento	
      - INT	
      - Llave foránea relacionado a la tabla CTEDocumento.
    * -	vCarga	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/infCTeNorm/infCarga/vCarga”.
    * -	proPred	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/infCTeNorm/infCarga/proPred”.
    * -	xOutCat	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/infCTeNorm/infCarga/xOutCat”.
    * -	vCargaAverb	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/infCTeNorm/infCarga/vCargaAverb”.

- CTEDocumentoCargaMedida

Descripción: Tabla que almacenará la información de la carga del CTE.

.. list-table:: CTEDocumentoCargaMedida
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * -	IdCTEDocumentoCargaMedida
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * -	IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumento.
    * -	IdCTEDocumentoCarga	
      - INT	
      - Llave foránea sobre la tabla CTEDocumentoCarga.
    * -	IdUnidadCarga	
      - INT	
      - Llave foránea sobre la tabla UnidadCarga.
    * -	tpMed	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/infCTeNorm/infCarga/InfQ/tpMed”.
    * -	qCarga	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/infCTeNorm/infCarga/InfQ/qCarga”.

- UnidadCarga

Descripción: Tabla de tipo catálogo que sincronizará los diferentes tipos de unidad de carga en el XML.

.. list-table:: UnidadCarga
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdUnidadCarga	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - Descripcion	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/infCTeNorm/infCarga/InfQ/cUnid”.
    * - ReferenciaExterna	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/infCTeNorm/infCarga/InfQ/cUnid”.

- CTEDocumentoComplemento

Descripción: Tabla que almacenará la información del complemento de CTE.

.. list-table:: CTEDocumentoComplemento
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdCTEDocumentoComplemento	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumento.
    * - xCaracAd	
      - Varchar	
      - Mapeo xml path “CTe/compl/xCaracAd”.
    * - xCaracSer	
      - Varchar	
      - Mapeo xml path “CTe/compl/xCaracSer”.
    * - xEmi	
      - Varchar	
      - Mapeo xml path “CTe/compl/xEmi”.
    * - origCalc	
      - Varchar	
      - Mapeo xml path “CTe/compl/origCalc”.
    * - destCalc	
      - Varchar	
      - Mapeo xml path “CTe/compl/destCalc”.
    * - xObs	
      - Varchar	
      - Mapeo xml path “CTe/compl/xObs”.
    * - ValorComplemento	
      - Decimal	
      - Se almacena un valor cero, se usará posteriormente para otros módulos.

- CTEDocumentoComplementoDetalle

Descripción: Tabla que almacenará la información del Detalle del Complemento de CTE.

.. list-table:: CTEDocumentoComplementoDetalle
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdCTEDocumentoComplemento	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumento.
    * - IdCTEDocumentoComplemento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumentoComplemento.
    * - xCampo	
      - Varchar	
      - Mapeo xml path “CTe/compl/ObsCont/xCampo” o “CTe/compl/ObsFisco/xCampo”. 
    * - xTexto	
      - Varchar	
      - Mapeo xml path “CTe/compl/ObsCont/xTexto” o “CTe/compl/ObsFisco/xTexto”. 
    * - ReferenciaComplemento	
      - Varchar	
      - Concatenación del campo xCampo y xTexto.

- CTEDocumentoConcepto

Descripción: Tabla que almacenará la información de los conceptos del CTE.

.. list-table:: CTEDocumentoConcepto
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdCTEDocumentoConcepto	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumento.
    * - IdTipoConcepto	
      - INT	
      - Llave foránea sobre la tabla TipoConcepto.
    * - vComp	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/vPrest/Comp/vComp”.

- TipoConcepto

Descripción: Tabla de tipo catálogo que sincronizará los diferentes tipos de Conceptos en el XML.

.. list-table:: TipoConcepto
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdTipoConcepto	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - Descripcion	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/vPrest/Comp/vNome”.
    * - ReferenciaExterna	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/vPrest/Comp/vNome”.


- CTEDocumentoNFE

Descripción: Tabla que almacenará la información de los conceptos de los DocuementosNFE.

.. list-table:: CTEDocumentoNFE
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción
    * - IdCTEDocumentoNFE	
      - INT	
      - Llave primaria de la tabla auto incrementable
    * - IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumento
    * - Tipo	
      - Varchar	
      - Tipo de Nfe el cual dependerá del nodo enviado: NFE: Si se envía sobre el path “CTe/InfCte/InfCteNorm/infDoc/ infNFE”. NF: Si se envía sobre el path “CTe/InfCte/InfCteNorm/infDoc/ infNF”. NF: Si se envía sobre el path “CTe/InfCte/InfCteNorm/infDoc/infOutros”. CTE: Si se envía sobre el path “CTe/InfCte/InfCteComp”
    * - Nfe	
      - Varchar	
      - Valor de Nfe el cual dependerá del DocuementosNFE.Tipo. NFE: Mapeo xml path “CTe/InfCte/InfCteNorm/infDoc/ infNFE/chave”. NF: Mapeo xml path “CTe/InfCte/InfCteNorm/infDoc/ infNF/mod” + “CTe/InfCte/InfCteNorm/infDoc/infNF/serie” + “CTe/InfCte/InfCteNorm/infDoc/infNF/nDoc” + “CTe/InfCte/InfCteNorm/infDoc/ infNF/dEmi” Otros: Mapeo xml path “CTe/InfCte/InfCteNorm/infDoc/infOutros/mod” +  “CTe/InfCte/InfCteNorm/infDoc/infOutros/serie” + “CTe/InfCte/InfCteNorm/infDoc/infOutros/nDoc” + “CTe/InfCte/InfCteNorm/infDoc/infOutros/dEmi” CTE: Mapeo xml path “CTe/InfCte/InfCteComp/chCTE”
 
- CTEDocumentoPersonasJuridicas

Descripción: Tabla de tipo catálogo que sincronizará los diferentes tipos de Personas relacionadas al documento CTE.

.. list-table:: CTEDocumentoPersonasJuridicas
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción 
    * - IdCTEDocumentoPersonasJuridicas
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumento.
    * - IdTipoPersona	
      - INT	
      - Llave foránea sobre la tabla TipoPersona.

- TipoPersona

Descripción: Tabla que almacenará la información de los conceptos de los DocuementosNFE, el path de búsqueda dependerá del tipo de persona enviado y sobre el cual se define en el campo “TipoPersona”. “Descripción”.

.. list-table:: TipoPersona
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción 
    * - IdTipoPersona	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - Descripcion	 
      - Varchar	
      - Tipo de persona el cual dependerá de donde se toma la información TOMADOR: Si se envía sobre el path “CTe/InfCte/ide/toma3” o  “CTe/InfCte/ide/toma4” EMISOR: Si se envía sobre el path “CTe/InfCte/emit” REMITENTE: Si se envía sobre el path “CTe/InfCte/rem” EXPEDIDOR: Si se envía sobre el path “CTe/InfCte/exped” DESTINATARIO: Si se envía sobre el path “CTe/InfCte/ dest” ReferenciaExterna	Varchar	 Se almacena el mismo valor enviado en TipoPersona.Descripción.
    * - CNPJ	
      - Varchar	
      - El valor dependerá del TipoPersona.Descripcion enviado TOMADOR: Mapeo xml path “CTe/InfCte/ide/toma3/toma” o “CTe/InfCte/ide/toma4/toma” EMISOR, REMITENTE, EXPEDIDOR, DESTINATARIO: Mapeo del atributo “CNPJ” IE	Varchar	Mapeo xml atributo “IE”.
    * - RazonSocial	
      - Varchar	
      - Mapeo xml atributo “xNome”.
    * - NombreFantasia	
      - Varchar	
      - Mapeo xml atributo “xFant”.
    * - Direccion	
      - Varchar	
      - Mapeo xml atributo “xLgr”.
    * - Numero	
      - Varchar	
      - Mapeo xml atributo “nro”.
    * - Barrio	
      - Varchar	
      - Mapeo xml atributo “xBarirro”.
    * - CodigoMunicipio	
      - Varchar	
      - Mapeo xml atributo “cMun”.
    * - Municipio	
      - Varchar	
      - Mapeo xml atributo “xMun”.
    * - CEP	
      - Varchar	
      - Mapeo xml atributo “CEP”.
    * - Telefono	
      - Varchar	
      - Mapeo xml atributo “fone”.
    * - Complemento	
      - Varchar	
      - Mapeo xml atributo “xCpl”.
    * - UF	
      - Varchar	
      - Mapeo xml atributo “UF”.
    * - CodigoPais	
      - Varchar	
      - Mapeo xml atributo “cPais”.
    * - Pais	
      - Varchar	
      - Mapeo xml atributo “xPais”.
    * - CPF	
      - Varchar	
      - Mapeo xml atributo “CPF”.
    * - Email	
      - Varchar	
      - Mapeo xml atributo “email”.
    * - IdCTETipoImpuesto	
      - INT	
      - Llave foránea CTETipoImpuesto que se utilizara posteriormente para otros módulos.

- CTEDocumentoProtocolo

Descripción: Tabla que almacenará la información del protocolo del documento. 

.. list-table:: CTEDocumentoProtocolo
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción 
    * - IdCTEDocumentoProtocolo	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumento.
    * - tpAmb	
      - Varchar	
      - Mapeo xml path “protCTe/tpAmb”.
    * - verAplic	
      - Varchar	
      - Mapeo xml path “protCTe/verAplic”.
    * - chCTe	
      - Varchar	
      - Mapeo xml path “protCTe/chCTe”.
    * - dhRecbto	
      - DateTime	
      - Mapeo xml path “protCTe/dhRecbto”.
    * - nProt	
      - Varchar	
      - Mapeo xml path “protCTe/nProt”.
    * - digVal	
      - Varchar	
      - Mapeo xml path “protCTe/digVal”.
    * - cStat	
      - Varchar	
      - Mapeo xml path “protCTe/cSat”.
    * - xMotivo	
      - Varchar	
      - Mapeo xml path “protCTe/xMotivo”.
    * - Id	
      - Varchar	
      - Mapeo xml path “protCTe/Id”.

- CTEDocumentoImpuesto

.. list-table:: CTEDocumentoImpuesto
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción 
    * - IdCTEDocumentoImpuesto	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumento.
    * - vTotTrib	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/imp/vTotTrib”.
    * - infAdFisco	
      - Varchar	
      - Mapeo xml path “CTe/InfCte/imp/infAdFisco”.
    * - vBCUFFim	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/imp/ICMSUFFim/vBCUFFim”.
    * - pFCPUFFim	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/imp/ICMSUFFim/pFCPUFFim”.
    * - pICMSUFFim	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/imp/ICMSUFFim/pICMSUFFim”.
    * - pICMSInter	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/imp/ICMSUFFim/pICMSInter”.
    * - vFCPUFFim	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/imp/ICMSUFFim/ vFCPUFFim”.
    * - vICMSUFIni	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/imp/ICMSUFFim/ vICMSUFIni”.
    * - vICMSUFFim	
      - Decimal	
      - Mapeo xml path “CTe/InfCte/imp/ICMSUFFim/vICMSUFFim”.

- CTEDocumentoImpuestoDetalle

Descripción: Tabla que almacenará la información de los detalles del impuesto, el path de búsqueda dependerá del tipo de impuesto enviado y sobre el cual se define en el campo “CTEDocumentoImpuestoDetalle”.”ReferenciaExterna”.

.. list-table:: CTEDocumentoImpuestoDetalle
    :widths: 10 10 45
    :header-rows: 1

    * - Campo
      - Tipo
      - Descripción 
    * - IdCTEDocumentoImpuestoDetalle	
      - INT	
      - Llave primaria de la tabla auto incrementable.
    * - IdCTEDocumentoImpuesto	
      - INT	
      - Llave foránea sobre la tabla CTEDocumentoImpuesto.
    * - IdCTEDocumento	
      - INT	
      - Llave foránea sobre la tabla CTEDocumentoImpuesto.
    * - IdCTETipoImpuesto	
      - INT	
      - Llave foránea sobre la tabla CTETipoImpuesto, en esta versión se almacenará el valor null, se utilizará posteriormente en otros módulos.
    * - ReferenciaExterna	
      - Varchar	
      - Tipo de impuesto el cual dependerá de donde se envía la información ICMS00: Mapeo xml path “CTe/InfCte/imp/ICMS00” ICMS45: Mapeo xml path “CTe/InfCte/imp/ICMS45” ICMS60: Mapeo xml path “CTe/InfCte/imp/ICMS60” ICMS90: Mapeo xml path “CTe/InfCte/imp/ICMS90” ICMSOutraUF: Mapeo xml path “CTe/InfCte/imp/ICMSOutraUF” ICMSSN: Mapeo xml path “CTe/InfCte/imp/ICMSSN”.
    * - cST	
      - Varchar	
      - Mapeo xml atributo “cST”.
    * - pRedBC	
      - Decimal	
      - Mapeo xml atributo “pRedBC”.
    * - vBC	
      - Decimal	
      - Mapeo xml atributo “vBC”.
    * - pICMS	
      - Decimal	
      - Mapeo xml atributo “pICMS”.
    * - vICMS	
      - Decimal	
      - Mapeo xml atributo “vICMS”.
    * - indSN	
      - Decimal	
      - Mapeo xml atributo “indSN”.
    * - vCred	
      - Decimal	
      - Mapeo xml atributo “vCred”.


Forma de Uso
--------------

Para acceder a este enlace se deberá ingresar con un usuario que tenga acceso al módulo de “Integrations Center”, posteriormente en el menú de Log Out seleccionar :kbd:`Integrations Center` --> :kbd:`CTE` --> :kbd:`Web Service`.

.. image:: cte1.png
   :align: center

Al dar clic en Web Service se abrirá el enlace "MAPI/SOAP/CTE/Service.ashx" para poder consumirla.

.. image:: cte2.png
   :align: center

Es necesario realizar una configuración previa con los siguientes pasos en SOAP UI:

- Método: Post
- Endpoint: MAPI/SOAP/CTE/Service.ashx 
- Media type:  Text XML
- Body: 
- Add Header: 
    - ApiKey
    - Value: MAPI token

.. image:: endpoint.png
   :align: center

Puede surgir el caso donde se tenga un error de integración, el cual depende que el CTE ya exista o que no cuente con una estructura XML valida.

Ejemplo error XML:

.. code-block:: xml
    :linenos:

        <CTEResposta xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <DocumentodeReferencia/>
    <Codigo>0</Codigo>
    <Mensagem>Erro. CTE não integrado: Error en el documento XML (1, 2)., Un nombre no puede empezar con el carácter '&lt;', valor hexadecimal 0x3C. línea 1, posición 2.</Mensagem>
    </CTEResposta>


Ejemplo exitoso XML:

.. code-block:: xml
    :linenos:

    <CTEResposta xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <DocumentodeReferencia>52230144914992001886570010023207311023207316</DocumentodeReferencia>
    <Codigo>1</Codigo>
    <Mensagem>CTE Integrado corretamente</Mensagem>
    </CTEResposta>


.. note::

    Los únicos códigos de integración son los siguientes: - (0) = error de integración (1) = Integración exitosa.






