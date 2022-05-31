import xmltodict
import requests

# get xml from local file
def OpenXML(path):
    with open(path, "r", encoding="utf-8") as file:
        file_selected = file.read()
    
    return xmltodict.parse(file_selected)

# get xml from url server
def fetch_xml(url):
    response = requests.get(url)
    return xmltodict.parse(response.content)