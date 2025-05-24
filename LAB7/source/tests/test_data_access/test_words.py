import unittest
from source.data_access.words import get_diagonal_word

class TestWordOperations(unittest.TestCase):
    def setUp(self):
        self.test_matrix = [
            [1 if j == (i + 1) % 16 else 0 for j in range(16)]
            for i in range(16)
        ]

    def test_word_extraction(self):
        word = get_diagonal_word(self.test_matrix, 0)
        expected = [0]*15 + [1]
        self.assertEqual(word, expected)

    def test_word_wrapping(self):
        word = get_diagonal_word(self.test_matrix, 15)
        expected = [0, 1] + [0]*14
        self.assertEqual(word, expected)