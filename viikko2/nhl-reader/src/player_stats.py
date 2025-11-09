class PlayerStats():
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality : str):
        fin_players = filter(lambda p : p.nationality ==  nationality, self.players)
        return sorted(fin_players, key=lambda p : p.points, reverse=True)

    def get_all_nationalities(self):
        return sorted({player.nationality for player in self.players})