import urllib.request
import json

url = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json"
with urllib.request.urlopen(url) as json_stream:
    data = json_stream.read().decode('utf-8')
    load_date = json.loads(data)
    for year,value in load_date['data'].items():
        year,value = int(year),float(value)
        print(f"{year}...{value:6.2f}")