from player_stats import PlayerStats
from player_reader import PlayerReader

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

def main():
    # Select season
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    season = Prompt.ask("Select a season", choices=seasons)

    # Fetch season data
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = Prompt.ask("Select nationality", choices=stats.get_all_nationalities())

    # Create a Rich table
    table = Table(title="Top Finnish Scorers 2024-25")
    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Team", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    # Add filtered player data
    players = stats.top_scorers_by_nationality(nationality)
    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    console = Console()
    console.print(table)

if __name__ == "__main__":
    main()
