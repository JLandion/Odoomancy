import requests


class DndApiService:
    BASE_URL = "https://www.dnd5eapi.co/api/2014"

    def _get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()
        return response.json()

    def list_monsters(self):
        return self._get("monsters")

    def get_monster(self, index):
        return self._get(f"monsters/{index}")

    def list_equipment(self):
        return self._get("equipment")

    def _get_equipment(self, index):
        return self._get(f"equipment/{index}")