from computer import get_computer_choice
from game import determine_winner
from scoreboard import Scoreboard
from history import GameHistory
from utils import get_player_choice


def show_rules():
    print("========== RULES ==========")
    print("1. Rock beats Scissors.")
    print("2. Scissors beats Paper.")
    print("3. Paper beats Rock.")
    print("4. Same choices result in a Draw.")
    print("===========================")


def play_game(scoreboard, history):
    print("\n========== PLAY GAME ==========")

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    result = determine_winner(player_choice, computer_choice)

    print("\nYou chose      :", player_choice)
    print("Computer chose :", computer_choice)
    print("Result         :", result)

    scoreboard.update_score(result)

    history.save_game(
        player_choice,
        computer_choice,
        result
    )


def main():

    scoreboard = Scoreboard()
    history = GameHistory()

    while True:

        print("================================")
        print("      ROCK PAPER SCISSORS")
        print("================================")
        print("1. Play Game")
        print("2. View Scoreboard")
        print("3. View Game History")
        print("4. Rules")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            play_game(scoreboard, history)

        elif choice == "2":
            scoreboard.display_scoreboard()

        elif choice == "3":
            history.display_history()

        elif choice == "4":
            show_rules()

        elif choice == "5":
            print("Thank you for playing Rock Paper Scissors!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()