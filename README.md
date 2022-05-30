## Cfdi XML parser to dabatase model

[]: # Language: markdown
[]: # Path: README.md

## Installation

```bash
pip install -r requirements.txt
```

## Usage
> **Import your xml file create a new folder called files and put your xml files inside**

```python
path = '/home/user/Desktop/cfdi-parser-to-databaase-model/files/retenciones.xml'
```
> **Run the scrpts**
```bash
python index.py
```

### Console output expected

```console
{  'currency': 'MXN',
   'discount': '65.00',
   'expedition_place': '06500',
   'fop': '99',
   'issuer_business_name': 'TELEFONOS DE MEXICO S.A.B. DE C.V.',
   'issuer_rfc': 'TME840315KT6',
   'payment_method': 'PPD',
   'receiver_business_name': 'HIJUELOS GARCIA JUAN JOSE',
   'receiver_rfc': 'HIGJ671130D85',
   'tax_regime_code': '601',
   'total': '388.99',
   'use_cfdi': 'G03',
   'voucher': 'I'}


Concept:{ 

{  'amount': '1.00',
   'currency': 'MXN',
   'description': 'Servicios de Telecomunicaciones',
   'discount': '65.00',
   'prod_serv_key': '81161700',
   'total_amount': '393.44',
   'unit': 'Unidad de Servicio',
   'unit_key': 'E48',
   'unit_value': '393.44'}
 }


[  {  'base: '335.34',
      'factor_type': 'Tasa',
      'rate_or_fee': '0.160000',
      'taxe': '002',
      'total_amount': '53.65'},
   {  'base': '229.98',
      'factor_type': 'Tasa',
      'rate_or_fee': '0.030000',
      'taxe': '003',
      'total_amount': '6.90'}]

```