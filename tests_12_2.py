import unittest
import TestCase


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = TestCase.Runner("Усэйн", speed=10)
        self.andrei = TestCase.Runner("Андрей", speed=9)
        self.nick = TestCase.Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_usein_nick(self):
        tournament = TestCase.Tournament(90, self.usein, self.nick)
        results = tournament.start()
        self.__class__.all_results[1] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")

    def test_race_andrei_nick(self):
        tournament = TestCase.Tournament(90, self.andrei, self.nick)
        results = tournament.start()
        self.__class__.all_results[2] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")

    def test_race_usein_andrei_nick(self):
        tournament = TestCase.Tournament(90, self.usein, self.andrei, self.nick)
        results = tournament.start()
        self.__class__.all_results[3] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")


if __name__ == '__main__':
    unittest.main()
