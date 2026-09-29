def determine_winner(player_choice, computer_choice):

    if player_choice == computer_choice:
        return "Draw"

    elif player_choice == "rock" and computer_choice == "scissors":
        return "Win"

    elif player_choice == "paper" and computer_choice == "rock":
        return "Win"

    elif player_choice == "scissors" and computer_choice == "paper":
        return "Win"

    else:
        return "Loss"