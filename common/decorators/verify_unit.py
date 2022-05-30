def it_contains_unit(func):
    def wrapper(*args, **kwargs):
        fn = func(*args, **kwargs)
        key = "@Unidad"
        if key in args[0]["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
            fn.update(
                {
                    "unit": args[0]["cfdi:Comprobante"]["cfdi:Conceptos"][
                        "cfdi:Concepto"
                    ]["@Unidad"]
                }
            )
            return fn
        return fn

    return wrapper
