import xmltodict
import pprint
from common.clean_format import (
    parse_invoice_data,
    parse_concepts,
    parse_taxe_concepts,
    parse_taxe_retention,
)


class InvoiceServices:
    def __init__(self, xml_data):
        self.xml_data = xml_data

    def get_invoice_payload(self):
        dict_result = xmltodict.parse(self.xml_data)
        invoice_payload = parse_invoice_data(dict_result)
        return invoice_payload

    def get_concept_payload(self):
        dict_result = xmltodict.parse(self.xml_data)
        concepts = parse_concepts(dict_result)
        return concepts

    def get_taxe_concept_payload(self):
        dict_result = xmltodict.parse(self.xml_data)
        taxe_concepts = parse_taxe_concepts(dict_result)
        return taxe_concepts
    
    def get_taxe_retention_payload(self):
        dict_result = xmltodict.parse(self.xml_data)
        taxe_retentions = parse_taxe_retention(dict_result)
        return taxe_retentions



if __name__ == "__main__":
    # testing locale file
    path = "/home/vicenteyah/Desktop/Python/ManageFiles/files/example.xml"
    with open("{}".format(path), "r", encoding="utf-8") as file:
        file_selected = file.read()

    xml_parser = InvoiceServices(file_selected)

    pprint.pprint(xml_parser.get_invoice_payload(), indent=3)
    print("\n")
    print("Concept:{ \n")
    pprint.pprint(xml_parser.get_concept_payload(), indent=3)
    print(" }")
    print("\n")
    pprint.pprint(xml_parser.get_taxe_concept_payload(), indent=3)
    print("\n")
    pprint.pprint(xml_parser.get_taxe_retention_payload(), indent=3)
