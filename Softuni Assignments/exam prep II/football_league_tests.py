import unittest
# import io
# import sys
import football_league as sut

class TestFootballLeague(unittest.TestCase):

    def test_get_teams(self):
        key = '??'
        text = '??ecnarF?? ??kramneD?? 0:0'
        teams = sut.get_teams(text, key)
        self.assertSequenceEqual(['France', 'Denmark'], teams)

    def test_get_points(self):
        text = '??ecnarF?? ??kramneD?? 3:4'
        points = sut.get_points(text)
        self.assertSequenceEqual([3, 4], points)



suite = unittest.TestLoader().loadTestsFromTestCase(TestFootballLeague)
unittest.TextTestRunner(verbosity=2).run(suite)