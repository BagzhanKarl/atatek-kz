import requests

def get_tree_data(item_id):
    url = 'https://tumalas.kz/wp-admin/admin-ajax.php?action=tuma_cached_childnew_get&nodeid=14&id='

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url + str(item_id), headers=headers)
    data = response.json()
    return data
