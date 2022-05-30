def it_contains_currency(func):
    def wrapper(*args, **kwargs):
        fn = func(*args, **kwargs)
        key = "@Moneda"
        if key in args[0]["cfdi:Comprobante"]:
            fn.update({"currency": args[0]["cfdi:Comprobante"]["@Moneda"]})
            return fn
        elif key in args[0]["cfdi:Comprobante"]["cfdi:Conceptos"]["cfdi:Concepto"]:
            fn.update(
                {
                    "currency": args[0]["cfdi:Comprobante"]["cfdi:Conceptos"][
                        "cfdi:Concepto"
                    ]["@Moneda"]
                }
            )
            return fn
        return fn

    return wrapper
