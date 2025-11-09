from rich.console import Console
from rich.prompt import Prompt

from player_stats import PlayerStats
from player_reader import PlayerReader

def main():
    # Select season
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    season = Prompt.ask("Select a season", choices=seasons)

    # Fetch season data
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = Prompt.ask("Select nationality", choices=stats.get_all_nationalities())

    # Print table
    console = Console()
    console.print(stats.top_scorers_by_nationality_table(nationality))

if __name__ == "__main__":
    main()
