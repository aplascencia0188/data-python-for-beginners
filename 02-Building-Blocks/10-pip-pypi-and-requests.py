pip3 install requests

ipython3

import requests

requests.get('http://nasa.gov')
# <Response [200]>

resp = requests.get('http://nasa.gov')

resp.status_code
resp.text
len(resp.text)

# -------------------
meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')

meteor_resp.status_code
meteor_resp.text

meteor_resp.json()

meteor_data = meteor_resp.json()
type(meteor_data)   # <class 'list'>

for meteor in meteor_data:
    print(type(meteor))

meteor_data[0]













