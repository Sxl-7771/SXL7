import unittest
import TestCase


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = TestCase.Runner("TestRunner", speed=5)

    @skip_if_frozen
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.usein = TestCase.Runner("Усэйн", speed=10)
        self.andrei = TestCase.Runner("Андрей", speed=9)
        self.nick = TestCase.Runner("Ник", speed=3)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = TestCase.Tournament(90, self.usein, self.nick)
        results = tournament.start()
        last_place = max(results.keys())
        self.assertEqual(results[last_place], "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = TestCase.Tournament(90, self.andrei, self.nick)
        results = tournament.start()
        last_place = max(results.keys())
        self.assertEqual(results[last_place], "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = TestCase.Tournament(90, self.usein, self.andrei, self.nick)
        results = tournament.start()
        last_place = max(results.keys())
        self.assertEqual(results[last_place], "Ник")
