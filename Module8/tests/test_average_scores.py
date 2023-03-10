import unittest
from Module8.dictionary_update import average_scores


class MyTestCase(unittest.TestCase):

    def test_average(self):
        self.dictionary = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666
        # Act
        actual = average_scores(self.dictionary)
        # Assert
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        self.dictionary = {'score1': 80, 'score2': 90, 'score3': 100, 'score4': 85, 'score5': 75}
        expected = 86
        # Act
        actual = average_scores(self.dictionary)
        # Assert
        self.assertEqual(expected, actual)

    def test_average_zero(self):
        self.dictionary = {}
        expected = None
        # Act
        actual = average_scores(self.dictionary)
        # Assert
        self.assertEqual(expected, actual)