import requests
import json


def get_loc(city, api_token):
    params = {'q': city, 'appid': api_token}
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=params)

    data = response.json()
    if not data:
        return None

    ndict = {'name': data[0]['name'],
             'country': data[0]['country'],
             'lat': data[0]['lat'],
             'lon': data[0]['lon']}
    return ndict


def save_city_to_file(data, filename='city_locations.json'):
    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(data, f)
        f.write('\n')

