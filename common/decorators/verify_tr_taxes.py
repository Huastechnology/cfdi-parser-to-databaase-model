def it_contains_properties(function):
    def wrapper(*args, **kwargs):
        fn = function(*args, **kwargs)

        if (
            args[0].get("cfdi:Comprobante").get("cfdi:Impuestos").get("cfdi:Traslados")
            is not None
        ):
            if (
                args[0]
                .get("cfdi:Comprobante")
                .get("cfdi:Impuestos")
                .get("@TotalImpuestosTrasladados")
                is not None
            ):
                fn.update(
                    {
                        "total_taxes_tranfered": args[0]["cfdi:Comprobante"][
                            "cfdi:Impuestos"
                        ]["@TotalImpuestosTrasladados"]
                    }
                )
                return fn
        if (
            args[0]
            .get("cfdi:Comprobante")
            .get("cfdi:Impuestos")
            .get("cfdi:Retenciones")
            is not None
        ):
            fn.update(
                {
                    "total_taxes_retained": args[0]["cfdi:Comprobante"][
                        "cfdi:Impuestos"
                    ]["@TotalImpuestosRetenidos"]
                }
            )
            return fn
        elif args[0].get("cfdi:Comprobante", {}).get("cfdi:Impuestos", {}) is not None:
            fn.update(
                {
                    "total_taxes_tranfered": args[0]["cfdi:Comprobante"][
                        "cfdi:Impuestos"
                    ]["cfdi:Traslados"]["cfdi:Traslado"]["@Importe"]
                }
            )
            return fn
        return fn

    return wrapper
