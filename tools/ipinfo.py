import requests

# Input from previous node
ip_address = items[0]['json']['ioc']  # Ensure 'ioc' holds the IP

# IPinfo.io config
api_token = 'XXX_REDACTED_XXX'  # Get it from https://ipinfo.io/account/token
base_url = f'https://ipinfo.io/{ip_address}?token={api_token}'

# Query IPinfo
response = requests.get(base_url)

# Check for errors
if response.status_code != 200:
    return [{
        'json': {
            'ioc': ip_address,
            'error': f'Failed to fetch from IPinfo: {response.status_code}',
            'details': response.text
        }
    }]

# Successful result
data = response.json()

# Return back to N8N
return [{
    'json': {
        'ioc': ip_address,
        'ipinfo': data
    }
}]
