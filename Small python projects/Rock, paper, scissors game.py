import random
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]
    while True:
        print("\nChoose one of the following options:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_choice = input("Enter your choice (1-3): ")
        if user_choice not in ["1", "2", "3"]:
            print("Invalid input. Please try again.")
            continue
        user_choice = options[int(user_choice) - 1]
        computer_choice = random.choice(options)
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    print("\nThanks for playing!")
if __name__ == "__main__":
    play_game()