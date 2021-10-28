import random

GAME_CHOICES = ['Rock', 'Paper', 'Scissor']


def RPSgame(user_input):
    computer = random.choice(GAME_CHOICES)

    if user_input == computer:
        print("It's a draw.")

    elif user_input == "Rock" and computer == "Scissor":
        print("Computer choose Scissor \nYou wins")

    elif user_input == "Paper" and computer == "Rock":
        print("Computer choose Rock \nYou wins")

    elif user_input == "Scissor" and computer == "Paper":
        print("Computer choose Paper \nYou wins")

    elif user_input == "Paper" and computer == "Scissor":
        print("Computer choose Scissor \nYou lost")

    elif user_input == "Scissor" and computer == "Rock":
        print("Computer choose Rock \nYou lost")

    elif user_input == "Rock" and computer == "Paper":
        print("Computer choose Paper \nYou lost")

    else:
        print(f'Invalid input.')
    
while True:
    user_input = str(input("Enter your choice (Rock, Paper, Scissor): "))
    RPSgame(user_input)

    play_again = input("Do you wanna continue?? (y): ")
    if play_again.lower() != 'y' :
        break

