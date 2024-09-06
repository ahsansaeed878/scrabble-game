"""
scrabble_game.py

This module contains the implementation of a Scrabble game where players
can compute their scores based on letter values, check for valid words,
and manage game rounds. The game includes features for time bonuses,
length validation, and score tracking.

Author: Ahsan Saeed
Date: 2024-09-06
"""
import random
import time

# Dictionary that defines the value of each letter in Scrabble
SCRABBLE_SCORES = {
    1: "AEIOULNRST",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ",
}

# A simple dictionary of valid words for validation purposes
DICTIONARY = {
    "cat",
    "dog",
    "hat",
    "pen",
    "book",
    "milk",
    "bread",
    "juice",
    "shoe",
    "fish",
    "tree",
    "chair",
    "table",
    "house",
    "phone",
    "light",
    "clock",
    "paper",
    "mouse",
    "train",
    "shirt",
    "pants",
    "drink",
    "fruit",
    "smile",
    "learn",
    "study",
    "write",
    "bright",
    "season",
    "example",
    "student",
    "winter",
    "garden",
    "holiday",
    "journey",
    "elevator",
    "capture",
    "cabbage",
}


class ScrabbleGame:
    """
    A class to represent a Scrabble game.

    Attributes
    ----------
    total_score : int
        The total score accumulated by the player.
    Methods
    -------
    calculate_score(word):
        Calculates the score for a given word based on Scrabble letter values.
    validate_word(word):
        Checks if the provided word is valid.
    """
    def __init__(self):
        # This keeps track of the player's total score over multiple rounds
        self.total_score = 0

    def calculate_score(self, word):
        """Calculates the Scrabble score for a given word."""
        score = 0
        # Convert the word to uppercase to handle case insensitivity
        for letter in word.upper():
            score += self.get_letter_score(letter)
        return score

    def get_letter_score(self, letter):
        """Returns the score for a given letter based on Scrabble rules."""
        # Look up the letter in the SCRABBLE_SCORES dictionary
        for score, letters in SCRABBLE_SCORES.items():
            if letter in letters:
                return score
        # If an invalid character is found, raise an error
        raise ValueError(f"Invalid character in word: {letter}")

    def is_valid_word(self, word):
        """Checks if the word is valid by looking it up in the dictionary."""
        return word.lower() in DICTIONARY

    def is_valid_length(self, word, length):
        """Ensures the word is the correct length for this round."""
        return len(word) == length

    def play(self):
        """
        Runs the main game loop, continuing for 10 rounds or until
        the player quits.
        """
        round_number = 1
        while round_number <= 10:
            # Randomly choose a required word length between 3 and 7 letters
            length_required = random.randint(3, 8)
            print(
                f"Round {round_number}: Please enter a word of length "
                f"{length_required}. You have 15 seconds."
            )
            print("Type 'quit' to exit the game.")

            # Track the time when the player starts and finishes input
            start_time = time.time()
            word = input(f"Enter a word of length {length_required}: ")
            end_time = time.time()

            # Check if the player wants to quit
            if word.lower() == "quit":
                print("You have chosen to quit the game.")
                break

            # If the player took more than 15 seconds, they miss the round
            if end_time - start_time > 15:
                print("Time's up! You took too long.")
                round_number += 1
                continue

            # Ensure the input only contains alphabetic characters
            if not word.isalpha():
                print("Invalid input. Please enter only alphabets.")
                round_number += 1
                continue

            # Check if the word length matches the required length
            if not self.is_valid_length(word, length_required):
                print(
                    f"Invalid word length. Expected {length_required} letters."
                )
                round_number += 1
                continue

            # Ensure the word is a valid word from the dictionary
            if not self.is_valid_word(word):
                print(
                    "Invalid word. Please enter a valid word "
                    "from the dictionary."
                )

                round_number += 1
                continue

            # Calculate the score for the word
            score = self.calculate_score(word)
            # Give a time bonus for entering the word quickly
            time_bonus = max(0, 15 - int(end_time - start_time))
            total_score = score + time_bonus
            self.total_score += total_score
            print(
                f"Your score for this round is {score}, "
                f"with a time bonus of {time_bonus}. "
                f"Your total score is now {self.total_score}."
            )

            round_number += 1

        # End of the game: display the final score
        print(f"Game over! Your final total score is {self.total_score}.")


# To manually run the game
if __name__ == "__main__":
    game = ScrabbleGame()
    game.play()
