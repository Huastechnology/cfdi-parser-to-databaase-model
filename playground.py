import xmltodict
import pprint

class XmlParser:
    def __init__(self, *args, **kwargs):
        self.xml_data = args[0]

    def get_invoice(self):
        dict_result = xmltodict.parse(self.xml_data)
        return dict_result


def dispatcher():
    path = "/home/vicenteyah/Desktop/Python/ManageFiles/files/concepts.xml"
    with open("{}".format(path), "r", encoding="utf-8") as file:
        file_selected = file.read()
    
    pprint.pprint(XmlParser(file_selected).get_invoice(), indent=3)



if __name__ == "__main__":
    # testing locale file
   dispatcher()