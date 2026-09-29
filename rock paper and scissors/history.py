import os


class GameHistory:

    def __init__(self, filename="data/game_history.txt"):
        self.filename = filename

        # Create the data folder if it does not exist
        folder = os.path.dirname(self.filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

    def save_game(self, player_choice, computer_choice, result):

        with open(self.filename, "a") as file:
            file.write(
                f"Player: {player_choice} | "
                f"Computer: {computer_choice} | "
                f"Result: {result}\n"
            )

    def display_history(self):

        try:
            with open(self.filename, "r") as file:
                history = file.readlines()

            if len(history) == 0:
                print("\nNo games played yet.")
                return

            print("\n========== GAME HISTORY ==========")

            for number, game in enumerate(history, start=1):
                print(f"{number}. {game.strip()}")

            print("==================================")

        except FileNotFoundError:
            print("\nNo games played yet.")