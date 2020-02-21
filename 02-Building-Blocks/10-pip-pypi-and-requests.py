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


# -------------------
import math

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2) ** 2 + \
        math.cos(lat1) * \
        math.cos(lat2) * \
        math.sin( (lon2 - lon1) / 2 ) ** 2
    
    return 6372.8 * 2 * math.asin(math.sqrt(h))


calc_dist(50.775000, 6.083330, 29.424122, -98.493628)
    # 8453.035130181917


# -------------------
my_loc = (29.424122, -98.493628)

for meteor in meteor_data:
    # if 'reclat' not in meteor or 'reclong' not in meteor: continue
    if not ('reclat' in meteor and 'reclong' in meteor):
        continue
    
    # added to json
    meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']), my_loc[0], my_loc[1])

meteor_data[0]








