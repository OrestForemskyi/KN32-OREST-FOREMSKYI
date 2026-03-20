import requests

version = requests.__version__
print(f"Версія бібліотеки requests: {version}")

r = requests.get('https://google.com')

print(f"Статус-код відповіді від Google: {r.status_code}")