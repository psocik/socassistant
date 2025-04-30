from pymisp import ExpandedPyMISP
import json

# Input from previous node
ioc = _items[0]['json']['ioc']  # Adjust 'ioc' key if your input field is named differently

# MISP Configuration
misp_url = 'XXX_REDACTED_XXX'
misp_key = 'XXX_REDACTED_XXX'
misp_verifycert = False  # Set True if your MISP cert is trusted

# Connect to MISP
misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

# Search MISP for the IOC
result = misp.search(controller='attributes', value=ioc)

# Return result back to N8N
return [{
    'json': {
        'ioc': ioc,
        'result': result
    }
}]
