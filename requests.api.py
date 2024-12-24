import requests

HOST = 'http://127.0.0.1:8000'

def post():
    post_data = {
        'title': 'Название',
        'description': 'description',
        'owner': 'owner'
    }

    response = requests.post(f'{HOST}', json=post_data)
    print(response.json())


def get():
    response = requests.post(f'{HOST}')
    print(response.json())


def delete():
    response = requests.delete(f'{HOST}')
    print(response.json())
