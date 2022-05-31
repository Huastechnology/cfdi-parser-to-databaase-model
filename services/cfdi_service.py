from common.clean_format import (
    parse_invoice_data,
    parse_concepts,
    parse_taxe_concepts,
    parse_taxe_invoice_transfer,
    parse_taxe_retention,
    parse_taxe_invoice_transfer,
    parse_taxe_invoice_retentions,
)

from .xml_parser_service import OpenXML

class InvoiceServices:

    def __init__(self, xml_data):
        self.xml_data = xml_data

    def get_invoice_payload(self):
        return parse_invoice_data(OpenXML(self.xml_data))

    def get_concept_payload(self):
        return parse_concepts(OpenXML(self.xml_data))
         
    def get_taxe_concept_payload(self):
        return parse_taxe_concepts(OpenXML(self.xml_data))
    
    def get_taxe_retention_payload(self):
        return parse_taxe_retention(OpenXML(self.xml_data))

    def get_taxe_invoice_payload(self):
        return parse_taxe_invoice_transfer(OpenXML(self.xml_data))

    def get_taxe_invoice_retentions_payload(self):
        return parse_taxe_invoice_retentions(OpenXML(self.xml_data))

        