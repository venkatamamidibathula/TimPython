import json

json_data_file = 'temperature_anomaly.json'

with open(json_data_file,encoding='utf-8',mode='r') as temperature_data:
    data = json.load(temperature_data)
    for year,value in data['data'].items():
        year,value = int(year),float(value)
        print(f"{year}...{value:6.2f}")
print(data['description'])
