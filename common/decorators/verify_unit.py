import pprint
def it_contains_unit(func):
    def wrapper(*args, **kwargs):
        fn = func(*args, **kwargs)
        key = "@Unidad"
        if key in args[0]["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
            get_props = args[0].get("cfdi:Comprobante").get("cfdi:Conceptos").get("cfdi:Concepto")
            if type(fn) is list:
                fn.append(
                    {
                        "unit": get_props[key]
                    }
                )
            if(type(fn) is dict):
                fn.update(
                    {
                        "unit": get_props[key]
                    }
                )
            return fn
        return fn

    return wrapper
