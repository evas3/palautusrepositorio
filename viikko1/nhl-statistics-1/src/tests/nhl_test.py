import unittest
from player_reader import PlayerReader
from statistics_service import StatisticsService

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_players(self):
        st = PlayerReaderStub([Player("Semenko", "EDM", 4, 12)])
        stub = PlayerReader(st)
        self.assertEqual(stub.get_players(), "Player("Semenko", "EDM", 4, 12)")