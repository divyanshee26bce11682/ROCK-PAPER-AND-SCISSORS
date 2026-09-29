def get_player_choice():

    while True:

        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "rock"

        elif choice == "2":
            return "paper"

        elif choice == "3":
            return "scissors"

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")