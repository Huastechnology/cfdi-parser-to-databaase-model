from .cfdi_service import InvoiceServices

def verify_invoice_type(data):
    invoice_types=["I","E","T","P","N"]
    voucher_type = ""
    if invoice_types[0] == data["voucher"]:
        voucher_type = "Ingreso"
        return voucher_type
    if invoice_types[1] == data["voucher"]:
        voucher_type = "Egreso"
        return voucher_type
    if invoice_types[4] == data["voucher"]:
        voucher_type = "Nomina"
        return voucher_type


def it_contains_data(data):
    if  data is not None:
        return True
    return False



def generate_invoice(file):
    xml_parser = InvoiceServices(file); payload = {}

    # Get voucher type Ingreso and validate
    if verify_invoice_type(xml_parser.get_invoice_payload()) =="Ingreso":
        payload.update(xml_parser.get_invoice_payload())
        if it_contains_data(xml_parser.get_concept_payload()):
            payload.update({"Concepts":xml_parser.get_concept_payload()})
        
        if it_contains_data(xml_parser.get_taxe_concept_payload()):
            payload.update({"ConceptTaxes":xml_parser.get_taxe_concept_payload()})
        
        if it_contains_data(xml_parser.get_taxe_retention_payload()):
            payload.update({"TaxeRetentions":xml_parser.get_taxe_retention_payload()})
        
        if it_contains_data(xml_parser.get_taxe_invoice_payload()):
            payload.update({"TaxeTransfers":xml_parser.get_taxe_invoice_payload()})
        
        if it_contains_data(xml_parser.get_taxe_invoice_retentions_payload()):
            payload.update({"Retentions":xml_parser.get_taxe_invoice_retentions_payload()})
        return payload

    # Get voucher type Nomina and validate
    if verify_invoice_type(xml_parser.get_invoice_payload()) =="Nomina":
        payload.update(xml_parser.get_invoice_payload())
        return payload
    return None