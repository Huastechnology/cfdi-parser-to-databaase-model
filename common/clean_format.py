from .decorators.verify_discount import it_contains_discount
from .decorators.verify_currency import it_contains_currency
from .decorators.verify_unit import it_contains_unit
from .decorators.verify_tr_taxes import it_contains_properties


# probado en facturas tipo ingreso y Nomina
@it_contains_currency
@it_contains_discount
def parse_invoice_data(param):
    """
    Parse the data from the xml file
    """
    invoiceData = {
        "tax_regime_code": param["cfdi:Comprobante"]["cfdi:Emisor"]["@RegimenFiscal"],
        "payment_method": param["cfdi:Comprobante"]["@MetodoPago"],
        "fop": param["cfdi:Comprobante"]["@FormaPago"],
        "voucher": param["cfdi:Comprobante"]["@TipoDeComprobante"],
        "use_cfdi": param["cfdi:Comprobante"]["cfdi:Receptor"]["@UsoCFDI"],
        "issuer_rfc": param["cfdi:Comprobante"]["cfdi:Emisor"]["@Rfc"],
        "issuer_business_name": param["cfdi:Comprobante"]["cfdi:Emisor"]["@Nombre"],
        "receiver_rfc": param["cfdi:Comprobante"]["cfdi:Receptor"]["@Rfc"],
        "receiver_business_name": param["cfdi:Comprobante"]["cfdi:Receptor"]["@Nombre"],
        "expedition_place": param["cfdi:Comprobante"]["@LugarExpedicion"],
        "total": param["cfdi:Comprobante"]["@Total"],
    }
    return invoiceData


# probado en facturas tipo ingreso y Nomina
@it_contains_unit
@it_contains_currency
@it_contains_discount
def parse_concepts(param):
    key = "cfdi:Conceptos"
    concept_list = []
    concept_dict = {}
    if key in param["cfdi:Comprobante"]:
        get_props = param.get('cfdi:Comprobante').get('cfdi:Conceptos').get('cfdi:Concepto')
        if type(get_props) is list:
            concept_list = []
            for i in range(len(get_props)):
                concept_list.append({
                    "unit_key": get_props[i]['@ClaveUnidad'],
                    "amount": get_props[i]['@Cantidad'],
                    "description": get_props[i]['@Descripcion'],
                    "unit_price": get_props[i]['@ValorUnitario'],
                    "total_amount": get_props[i]['@Importe'],
                    "prod_serv_key": get_props[i]['@ClaveProdServ'],
                })
            return concept_list
        elif(type(get_props) is dict):
            concept_dict = {
                "unit_key": get_props['@ClaveUnidad'],
                "amount": get_props['@Cantidad'],
                "description": get_props['@Descripcion'],
                "unit_value": get_props['@ValorUnitario'],
                "total_amount": get_props['@Importe'],
                "prod_serv_key": get_props['@ClaveProdServ'],
            }
            return concept_dict
    return None

# not tested in payroll invoice
def parse_taxe_concepts(param):
    key = "cfdi:Impuestos"
    taxeConcept={}; taxe_list =[]; taxe_array_dict = []

    taxe_type = param.get('cfdi:Comprobante').get('cfdi:Conceptos').get('cfdi:Concepto')
    if type(taxe_type) is list:
        for i in range(len(taxe_type)):
            get_props = taxe_type[i].get('cfdi:Impuestos').get('cfdi:Traslados').get('cfdi:Traslado')
            if key in taxe_type[i]:
                
                if type(get_props) is list:
                    for j in range(len(get_props)):
                        taxe_list.append({
                            "taxe": get_props[j]['@Impuesto'],
                            "base": get_props[j]['@Base'],
                            "total_amount": get_props[j]['@Importe'],
                            "rate_or_fee": get_props[j]['@TasaOCuota'],
                            "factor_type": get_props[j]['@TipoFactor'],
                        })
                    return taxe_list

                if(type(get_props) is dict):
                    taxe_array_dict.append({
                        "taxe": taxe_type[i]['cfdi:Impuestos']['cfdi:Traslados']['cfdi:Traslado']['@Impuesto'],
                        "base":  taxe_type[i]['cfdi:Impuestos']['cfdi:Traslados']['cfdi:Traslado']['@Base'],
                        "total_amount": taxe_type[i]['cfdi:Impuestos']['cfdi:Traslados']['cfdi:Traslado']['@Importe'],
                        "rate_or_fee":  taxe_type[i]['cfdi:Impuestos']['cfdi:Traslados']['cfdi:Traslado']['@TasaOCuota'],
                        "factor_type":  taxe_type[i]['cfdi:Impuestos']['cfdi:Traslados']['cfdi:Traslado']['@TipoFactor'],
                    })
        return taxe_array_dict

    if type(taxe_type) is dict:
    
        if key in param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
            get_props = param.get('cfdi:Comprobante').get('cfdi:Conceptos').get('cfdi:Concepto').get('cfdi:Impuestos').get('cfdi:Traslados').get('cfdi:Traslado')
            if type(get_props) is list:
                for i in range(len(get_props)):
                    taxe_list.append({
                        "taxe": get_props[i]["@Impuesto"],
                        "base": get_props[i]['@Base'],
                        "factor_type": get_props[i]['@TipoFactor'],
                        "rate_or_fee": get_props[i]['@TasaOCuota'],
                        "total_amount": get_props[i]['@Importe']
                    })
                return taxe_list
            if(type(get_props) is dict):
                taxeConcept = {
                    "taxe": get_props["@Impuesto"],
                    "base": get_props['@Base'],
                    "factor_type": get_props['@TipoFactor'],
                    "rate_or_fee": get_props['@TasaOCuota'],
                    "total_amount": get_props['@Importe'],
                }
            return taxeConcept
    return None


# not tested in payroll invoice
def parse_taxe_retention(param):
    keys = ["cfdi:Impuestos","cfdi:Retenciones"]
    retention={}
    taxe_list =[]
    taxe_type = param.get('cfdi:Comprobante').get('cfdi:Conceptos').get('cfdi:Concepto')

    if (type(taxe_type) is list and taxe_type is not None):

        for i in range(len(taxe_type)):
            if keys[1] in taxe_type[i] and keys[1] in taxe_type[i][keys[0]]:

                get_props = taxe_type[i][keys[0]][keys[1]].get('cfdi:Retencion')

                if type(get_props) is list:
                    for j in range(len(get_props)):
                        taxe_list.append({
                            "taxe": get_props[j]["@Impuesto"],
                            "base": get_props[j]['@Base'],
                            "factor_type": get_props[j]['@TipoFactor'],
                            "rate_or_fee": get_props[j]['@TasaOCuota'],
                            "total_amount": get_props[j]['@Importe']
                        })
                    return taxe_list

                if(type(get_props) is dict):
                    retention = {
                        "taxe": get_props["@Impuesto"],
                        "base": get_props['@Base'],
                        "factor_type": get_props['@TipoFactor'],
                        "rate_or_fee": get_props['@TasaOCuota'],
                        "total_amount": get_props['@Importe'],
                    }
                    return retention
    
    if(type(taxe_type) is dict):

        if keys[1] in param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]['cfdi:Impuestos']:
            get_props = param.get('cfdi:Comprobante').get('cfdi:Conceptos').get('cfdi:Concepto').get('cfdi:Impuestos').get('cfdi:Retenciones').get('cfdi:Retencion')
 
            if keys[0] in param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
                if type(get_props) is list:
                    for i in range(len(get_props)):
                        taxe_list.append({
                            "taxe": get_props[i]["@Impuesto"],
                            "base": get_props[i]['@Base'],
                            "factor_type": get_props[i]['@TipoFactor'],
                            "rate_or_fee": get_props[i]['@TasaOCuota'],
                            "total_amount": get_props[i]['@Importe']
                        })
                    return taxe_list
                if(type(get_props) is dict):
                    retention = {
                        "taxe": get_props["@Impuesto"],
                        "base": get_props['@Base'],
                        "factor_type": get_props['@TipoFactor'],
                        "rate_or_fee": get_props['@TasaOCuota'],
                        "total_amount": get_props['@Importe'],
                    }
                return retention
    return None


@it_contains_properties
def parse_taxe_invoice_transfer(param):
    key = "cfdi:Traslados"
    taxe_transfer_list =[]; taxe_transfer_dict = {}

    # Transfer with four properties
    if key in param["cfdi:Comprobante"]["cfdi:Impuestos"]:
        get_props = param.get('cfdi:Comprobante').get('cfdi:Impuestos').get('cfdi:Traslados').get('cfdi:Traslado')
        if type(get_props) is list:
            for i in range(len(get_props)):
                taxe_transfer_list.append({
                    "taxe": get_props[i]["@Impuesto"],
                    "factor_type": get_props[i]['@TipoFactor'],
                    "rate_or_fee": get_props[i]['@TasaOCuota'],
                    "total_amount": get_props[i]['@Importe']
                })
            return taxe_transfer_list
        if(type(get_props) is dict):
            taxe_transfer_dict = {
                "taxe": get_props["@Impuesto"],
                "factor_type": get_props['@TipoFactor'],
                "rate_or_fee": get_props['@TasaOCuota'],
                "total_amount": get_props['@Importe'],
            }
        return taxe_transfer_dict
    return None


@it_contains_properties
def parse_taxe_invoice_retentions(param):
    key = 'cfdi:Retenciones'
    taxe_retention_list = []; taxe_retention_dict = {}
    
    # retentions with two properties
    if key in param["cfdi:Comprobante"]["cfdi:Impuestos"]:
        get_props = param.get('cfdi:Comprobante').get('cfdi:Impuestos').get('cfdi:Retenciones').get('cfdi:Retencion')
        if type(get_props) is list:
            for i in range(len(get_props)):
                taxe_retention_list.append({
                    "taxe": get_props[i]["@Impuesto"],
                    "total_amount": get_props[i]['@Importe']
                })
            return taxe_retention_list
        elif(type(get_props) is dict):
            taxe_retention_dict = {
                "taxe": get_props["@Impuesto"],
                "total_amount": get_props['@Importe'],
            }
        return taxe_retention_dict
    return None
