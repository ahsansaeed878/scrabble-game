"""
Unit tests for the Scrabble game.

This module contains tests that verify the functionality of the Scrabble game,
ensuring that word scoring, word validation, and other
game features work correctly.
"""

import unittest
from scrabble_game import ScrabbleGame


class TestScrabbleGame(unittest.TestCase):
    """
    Test cases for the ScrabbleGame class.

    This class contains unit tests to ensure the correct functionality of the
    methods in the ScrabbleGame class.
    """
    def setUp(self):
        self.game = ScrabbleGame()

    def test_scrabble_score_simple_word(self):
        """
        Test that the calculate_score method computes the correct
        Scrabble score
        for a given word.
        """
        self.assertEqual(self.game.calculate_score("cabbage"), 14)

    def test_scrabble_score_case_insensitive(self):
        """
        Test that the calculate_score method computes
        the correct Scrabble score
        for a given word.
        """
        self.assertEqual(self.game.calculate_score("CaBbaGe"), 14)

    def test_invalid_characters(self):
        """
        Test that the calculate_score method computes the
        correct Scrabble score
        for a given word.
        """
        with self.assertRaises(ValueError):
            self.game.calculate_score("cabbage1")  # Invalid character

    def test_invalid_word_from_dictionary(self):
        """
        Test that the is_valid_word method correctly
        identifies valid words from
        the dictionary.
        """
        self.assertFalse(self.game.is_valid_word("zzzzz"))

    def test_timer_and_length(self):
        """
        Test that the is_valid_length method correctly
        identifies valid length of the word.
        """
        self.assertTrue(self.game.is_valid_length("apple", 5))


if __name__ == '__main__':
    unittest.main()
