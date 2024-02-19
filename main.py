#1 задача
import csv
import json
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data_list = []

    for row in reader:
        if some_complex_condition(row):
            data_list.append(row)

with open('output.json', 'w') as jsonfile:
    json.dump(data_list, jsonfile)

#2 задача
import json
import requests
with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)

host = data['host']
port = data['port']
server_address = f'http://{host}:{port}'
response = requests.get(server_address)

if response.status_code == 200:
    data_list = response.json()
    for data in data_list:
        some_data = data['some_key']
        print(some_data)
else:
    print(f'Ошибка: статус кода {response.status_code}')

#3 задача
import argparse
import json
import requests
parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', required=True, help='Хост сервера')
parser.add_argument('-P', '--port', required=True, help='Порт сервера')
args = parser.parse_args()
host = args.host
port = args.port


server_address = f'http://{host}:{port}'

response = requests.get(server_address)

if response.status_code == 200:
    data_dict = response.json()
    data_list = [data for data in data_dict.values() if some_condition(data)]

    with open('output.json', 'w') as jsonfile:
        json.dump(data_list, jsonfile)
else:
    print(f'Ошибка: статус кода {response.status_code}')
