import requests
from player import Player

class PlayerReader:
    def __init__(self, url : str):
        self.url = url

    def change_ulr(self, url : str):
        self.url = url

    def get_players(self) -> list[Player]:
        response = requests.get(self.url, timeout=3.0).json()

        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
