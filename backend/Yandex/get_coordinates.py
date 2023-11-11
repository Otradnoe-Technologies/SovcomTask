import requests
import json

API_KEY = "d987ffa6-e6c2-42fe-86e1-3953c4fa483a"

def get_coordinates_by_address(address):
    params = {'apikey': API_KEY, 'geocode': address, 'format' : "json"}

    response = requests.get("https://geocode-maps.yandex.ru/1.x/", params=params)

    response_obj = json.loads(response.text)
    found = response_obj['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found']
    found = int(found)
    coordinates = (0, 0)
    if found > 0:
        coordinates = response_obj['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        coordinates[0] = float(coordinates[0])
        coordinates[1] = float(coordinates[1])

    return coordinates

coordinates = get_coordinates_by_address("Тверская+6")
print(coordinates)