import requests


def get_data(query: str, country: str):
    url = 'https://nominatim.openstreetmap.org/search.php?format=jsonv2&q='
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MyApp/1.0; +http://alash.atatek.kz)'
    }
    response = requests.get(url + query + "+" + country, headers=headers)
    data = response.json()

    # Фильтруем только объекты с addresstype='town'
    filtered_data = [
        {
            'display_name': item['display_name'],
            'category': item['category'],
            'addresstype': item['addresstype'],
            'place_id': item['place_id'],
            'osm_id': item['osm_id']
        }
        for item in data
    ]

    return filtered_data


#print(get_data('Кеген', 'Kazakhstan'))
