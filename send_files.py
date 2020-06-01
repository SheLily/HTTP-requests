import requests
from glob import glob

URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
KEY = 'OAuth'


if __name__ == '__main__':
    files = glob('*_translate.txt')
    header = {
        'Authorization': 'OAuth ' + KEY
    }
    for file in files:
        params = {
            'path': file,
            'overwrite': True
        }

        response = requests.get(URL, params=params, headers=header)
        json_ = response.json()
        up_url = json_['href']

        with open(file, 'rb') as fin:
            response = requests.put(up_url, data=fin, headers=header)


