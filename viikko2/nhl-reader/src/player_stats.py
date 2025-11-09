from rich.table import Table

class PlayerStats():
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality : str):
        fin_players = filter(lambda p : p.nationality ==  nationality, self.players)
        return sorted(fin_players, key=lambda p : p.points(), reverse=True)

    def top_scorers_by_nationality_table(self, nationality : str):
        # Create a Rich table
        table = Table(title="Top Finnish Scorers 2024-25")
        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Team", justify="left", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        # Add filtered player data
        players = self.top_scorers_by_nationality(nationality)
        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.points())
            )

        return table

    def get_all_nationalities(self):
        return sorted({player.nationality for player in self.players})
