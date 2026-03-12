import requests


class DndApiService:
    BASE_URL = "https://www.dnd5eapi.co/api/2014"

    def _get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()
        return response.json()

    def list_(self, param):
        return self._get(param)

    def get_(self, param, index):
        return self._get(f"{param}/{index}")
