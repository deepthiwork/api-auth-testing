import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def get(self, endpoint, token=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = {}

        if token:
            headers['Authorization'] = f"Bearer {token}"

        return self.session.get(url, headers=headers)

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.post(url, json=data)

