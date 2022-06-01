def it_contains_currency(func):
    def wrapper(*args, **kwargs):
        fn = func(*args, **kwargs)
        key = "@Moneda"
        
        if key in args[0]["cfdi:Comprobante"]:
            get_common = args[0].get("cfdi:Comprobante")
            if(type(fn) is dict):
                fn.update(
                    {
                        "currency": get_common[key]
                    }
                )
            return fn
        if key in args[0]["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
            get_props = args[0].get("cfdi:Comprobante").get("cfdi:Conceptos").get("cfdi:Concepto")
            if type(fn) is list:
                print(type(fn))
                fn.append({
                    "currency": get_props[key]
                })
            if(type(fn) is dict):
                fn.update(
                    {
                        "currency": get_props[key]
                    }
                )
            return fn
        return fn

    return wrapper
