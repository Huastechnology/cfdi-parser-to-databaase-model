def it_contains_discount(func):
    def wrapper(*args, **kwargs):
        fn = func(*args, **kwargs)
        key = "@Descuento"
        if key in args[0]["cfdi:Comprobante"]:
            fn.update({"discount": args[0]["cfdi:Comprobante"]["@Descuento"]})
            return fn
        elif key in args[0]["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
            get_props = args[0].get("cfdi:Comprobante").get("cfdi:Conceptos").get("cfdi:Concepto")
            if type(fn) is list:
                fn.append(
                    {
                        "discount": get_props[key]
                    }
                )
            if(type(fn) is dict):
                fn.update(
                    {
                        "discount": get_props[key]
                    }
                )
            return fn
        return fn

    return wrapper
