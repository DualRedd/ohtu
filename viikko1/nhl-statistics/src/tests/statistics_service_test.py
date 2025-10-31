import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]
    

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_exact_match(self):
        player = self.stats.search("Yzerman")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Yzerman")

    def test_search_partial_match(self):
        player = self.stats.search("Gret")
        self.assertEqual(player.name, "Gretzky")

    def test_search_not_found(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        edm_players = self.stats.team("EDM")
        edm_names = [p.name for p in edm_players]
        self.assertEqual(edm_names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_for_unknown_team(self):
        unknown_team = self.stats.team("XYZ")
        self.assertEqual(unknown_team, [])

    def test_top_zero_returns_one(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_returns_correct_players(self):
        top_players = self.stats.top(2)
        top_names = [p.name for p in top_players]
        # Gretzky (124), Lemieux (99), Yzerman (98)
        self.assertEqual(top_names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_all_players(self):
        top_players = self.stats.top(4)
        self.assertEqual(len(top_players), 5)
        top_names = [p.name for p in top_players]
        self.assertEqual(top_names, ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"])

    def test_top_sorted_by_goals(self):
        top_by_goals = self.stats.top(2, SortBy.GOALS)
        top_names = [p.name for p in top_by_goals]
        # Lemieux (45), Yzerman (42), Kurri (37)
        self.assertEqual(top_names, ["Lemieux", "Yzerman", "Kurri"])

    def test_top_sorted_by_assists(self):
        top_by_assists = self.stats.top(2, SortBy.ASSISTS)
        top_names = [p.name for p in top_by_assists]
        # Gretzky (89), Yzerman (56), Lemieux (54)
        self.assertEqual(top_names, ["Gretzky", "Yzerman", "Lemieux"])
