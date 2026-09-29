import unittest
from game import determine_winner


class TestDetermineWinner(unittest.TestCase):

    def test_rock_beats_scissors(self):
        self.assertEqual(
            determine_winner("rock", "scissors"),
            "Win"
        )

    def test_paper_beats_rock(self):
        self.assertEqual(
            determine_winner("paper", "rock"),
            "Win"
        )

    def test_scissors_beats_paper(self):
        self.assertEqual(
            determine_winner("scissors", "paper"),
            "Win"
        )

    def test_rock_loses_to_paper(self):
        self.assertEqual(
            determine_winner("rock", "paper"),
            "Loss"
        )

    def test_paper_loses_to_scissors(self):
        self.assertEqual(
            determine_winner("paper", "scissors"),
            "Loss"
        )

    def test_scissors_loses_to_rock(self):
        self.assertEqual(
            determine_winner("scissors", "rock"),
            "Loss"
        )

    def test_rock_draw(self):
        self.assertEqual(
            determine_winner("rock", "rock"),
            "Draw"
        )

    def test_paper_draw(self):
        self.assertEqual(
            determine_winner("paper", "paper"),
            "Draw"
        )

    def test_scissors_draw(self):
        self.assertEqual(
            determine_winner("scissors", "scissors"),
            "Draw"
        )


if __name__ == "__main__":
    unittest.main()