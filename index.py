import pprint
from services.order_data import generate_invoice


if __name__ == "__main__":
    # testing locale file
    path = "/home/vicenteyah/Desktop/Python/ManageFiles/files/retenciones.xml"
    payload = generate_invoice(path)

    pprint.pprint(payload, indent=3)

