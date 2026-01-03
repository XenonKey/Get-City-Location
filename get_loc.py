import requests
from my_api_token import API_TOKEN, GEO


def get_lat_and_lon(city, API_TOKEN):
    params = {'q': city, 'appid': API_TOKEN}
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=params)

    ndict = {'name': response.json()[0]['name'],
             'country': response.json()[0]['country'],
             'lat': response.json()[0]['lat'],
             'lon': response.json()[0]['lon']}

    print(ndict)

get_lat_and_lon('Moscow', API_TOKEN)


q = 1
