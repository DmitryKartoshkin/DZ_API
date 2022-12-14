import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        # Заголовки
        return {'Content-Type': 'application/json',  'Authorization': f'OAuth {self.token}'}

    def _get_upload_link(self, disk_file_path):
        #
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        """Метод загружает файлы на яндекс диск"""
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    TOKEN = ""
    path_to_file = "test.txt"
    uploader = YaUploader(token = TOKEN)
    result = uploader.upload(path_to_file, path_to_file)




