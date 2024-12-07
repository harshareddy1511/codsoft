import random

def play_round():
    # Choices for the game
    choices = ["rock", "paper", "scissors"]
    
    # Get user choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please select rock, paper, or scissors.")
        return None, None

    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
        return 0, 0  # No points awarded
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        return 1, 0  # User wins
    else:
        print("Computer wins this round!")
        return 0, 1  # Computer wins

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Choose rock, paper, or scissors. Rock beats scissors, scissors beats paper, and paper beats rock.")
    
    user_score = 0
    computer_score = 0

    while True:
        # Play a round
        user_points, computer_points = play_round()
        if user_points is None:  # Invalid input
            continue

        # Update scores
        user_score += user_points
        computer_score += computer_points

        # Display current scores
        print(f"\nScores:\nYou: {user_score} | Computer: {computer_score}\n")

        # Ask if the user wants to play another round
        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != "y":
            break

    # Final scores
    print("\nFinal Scores:")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game! 🎉")
    elif user_score < computer_score:
        print("Better luck next time! The computer won this time.")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    play_game()
