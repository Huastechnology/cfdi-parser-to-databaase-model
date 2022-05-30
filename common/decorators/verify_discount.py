def it_contains_discount(func):
    def wrapper(*args, **kwargs):
        fn = func(*args, **kwargs)
        key = "@Descuento"
        if key in args[0]["cfdi:Comprobante"]:
            fn.update({"discount": args[0]["cfdi:Comprobante"]["@Descuento"]})
            return fn
        elif key in args[0]["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
            fn.update(
                {
                    "discount": args[0]["cfdi:Comprobante"]["cfdi:Conceptos"][
                        "cfdi:Concepto"
                    ]["@Descuento"]
                }
            )
            return fn
        return fn

    return wrapper
