import pprint
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
    conceptData = {
        "unit_key": param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]["@ClaveUnidad"],
        "amount": param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]["@Cantidad"],
        "description": param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]["@Descripcion"],
        "unit_value": param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]["@ValorUnitario"],
        "total_amount": param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]["@Importe"],
        "prod_serv_key": param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]["@ClaveProdServ"],
    }
    return conceptData

# not tested in payroll invoice
def parse_taxe_concepts(param):
    key = "cfdi:Impuestos"
    get_props = param.get('cfdi:Comprobante').get('cfdi:Conceptos').get('cfdi:Concepto').get('cfdi:Impuestos').get('cfdi:Traslados').get('cfdi:Traslado')
    taxeConcept={}
    taxe_list =[]
    if key in param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
        if type(get_props) is list:
            for i in range(len(get_props)):
                taxeConcept = {
                    "taxe": get_props[i]["@Impuesto"],
                    "base": get_props[i]['@Base'],
                    "factor_type": get_props[i]['@TipoFactor'],
                    "rate_or_fee": get_props[i]['@TasaOCuota'],
                    "total_amount": get_props[i]['@Importe']
                }
                taxe_list.append(taxeConcept)
            return taxe_list
        elif(type(get_props) is dict):
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
    
    if keys[1] in param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]['cfdi:Impuestos']:
        get_props = param.get('cfdi:Comprobante').get('cfdi:Conceptos').get('cfdi:Concepto').get('cfdi:Impuestos').get('cfdi:Retenciones').get('cfdi:Retencion')
 
        if keys[0] in param["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
            if type(get_props) is list:
                for i in range(len(get_props)):
                    retention = {
                        "taxe": get_props[i]["@Impuesto"],
                        "base": get_props[i]['@Base'],
                        "factor_type": get_props[i]['@TipoFactor'],
                        "rate_or_fee": get_props[i]['@TasaOCuota'],
                        "total_amount": get_props[i]['@Importe']
                    }
                    taxe_list.append(retention)
                return taxe_list
            elif(type(get_props) is dict):
                retention = {
                    "taxe": get_props["@Impuesto"],
                    "base": get_props['@Base'],
                    "factor_type": get_props['@TipoFactor'],
                    "rate_or_fee": get_props['@TasaOCuota'],
                    "total_amount": get_props['@Importe'],
                }
            return retention
    return None
    

