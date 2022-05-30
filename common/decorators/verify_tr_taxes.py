"""
    @decorator that evaluates if the property <cfdi:Impuestos> has more properties
"""
def it_contains_properties(function):
    def wrapper(*args, **kwargs):
        keys = ['@TotalImpuestosRetenidos','@TotalImpuestosTrasladados']

        fn = function(*args, **kwargs)
        if keys[1] and keys[0] in args[0]["cfdi:Comprobante"]["cfdi:Impuestos"]:
            get_props = args[0].get("cfdi:Comprobante").get("cfdi:Impuestos")
            if type(fn) is list:
                fn.append({
                    keys[1]: get_props[keys[1]],
                    keys[0]: get_props[keys[0]]
                })
            elif(type(fn) is dict):
                fn.update({
                    keys[1]: get_props[keys[1]],
                    keys[0]: get_props[keys[0]]
                })
            return fn
        if keys[0] not in args[0]["cfdi:Comprobante"]["cfdi:Impuestos"]:
            if keys[1] in args[0]["cfdi:Comprobante"]["cfdi:Impuestos"]:
                get_props = args[0].get("cfdi:Comprobante").get("cfdi:Impuestos")
                if type(fn) is list:
                    fn.append({
                        keys[1]: get_props[keys[1]]
                    })
                elif(type(fn) is dict):
                    fn.update({
                        keys[1]: get_props[keys[1]]
                    })
                return fn
            return fn
        if keys[1] not in args[0]["cfdi:Comprobante"]["cfdi:Impuestos"]:
            if keys[0] in args[0]["cfdi:Comprobante"]["cfdi:Impuestos"]:
                get_props = args[0].get("cfdi:Comprobante").get("cfdi:Impuestos")
                if type(fn) is list:
                    fn.append({
                        keys[0]: get_props[keys[0]]
                    })
                elif(type(fn) is dict):
                    fn.update({
                        keys[0]: get_props[keys[0]]
                    })
                return fn
            return fn
        
        return fn

    return wrapper
