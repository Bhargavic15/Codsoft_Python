import random

def get_user_choice():
    """
    Prompt the user to choose rock, paper, or scissors.
    Returns the user's choice as a string.
    """
    choices = ['rock', 'paper', 'scissors']
    user_choice = ''
    while user_choice not in choices:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose again.")
    return user_choice

def get_computer_choice():
    """
    Generate a random choice for the computer (rock, paper, or scissors).
    Returns the computer's choice as a string.
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user's and computer's choices.
    Returns a string indicating the result: 'win', 'lose', or 'tie'.
    """
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_result(user_choice, computer_choice, result):
    """
    Display the user's choice, the computer's choice, and the result of the game.
    """
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == 'win':
        print("You win!")
    elif result == 'lose':
        print("You lose.")
    else:
        print("It's a tie.")

def play_again():
    """
    Ask the user if they want to play another round.
    Returns True if the user wants to play again, otherwise False.
    """
    play_again_choice = input("Do you want to play again? (yes/no): ").lower()
    return play_again_choice == 'yes'

def main():
    print("Welcome to the Rock-Paper-Scissors Game!")
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        rounds += 1
        print(f"\nRound {rounds}")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
