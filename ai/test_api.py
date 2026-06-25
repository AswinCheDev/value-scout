import requests

try:
    r = requests.get('http://localhost:5000/api/style-builder/myntra_07096320a6fe4eb49428fe3365f5f127', timeout=10)
    print('Status:', r.status_code)
    print('Response:', r.text)
except Exception as e:
    print('Error:', e)
