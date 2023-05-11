import requests

r = requests.get('https://www.assamcareer.com/')
print(r.text)