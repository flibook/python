import requests

url = 'https://cloud-api.yandex.net/v1/disk/resources'
token = 'YOUR_API_TOKEN'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск
        savefile: Путь к файлу на Диске
        loadfile: Путь к загружаемому файлу
        replace: true or false Замена файла на Диске"""
        res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
        with open(loadfile, 'rb') as f:
            try:
                requests.put(res['href'], files={'file':f})
            except KeyError:
                print(res)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = 'YOUR_API_TOKEN'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)



