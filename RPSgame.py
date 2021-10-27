import random
Game_choice = ['Rock', 'Paper', 'Scissor']

cpu = random.choice(Game_choice)

print("\nWelcome To Rock Paper Scissor Game\n")

user_input = str(input('Rock \nPaper \nScissor \nEnter your choice: '))

if user_input == cpu:
    print("It's a draw")

elif user_input == "Rock" and cpu == "Scissor":
    print("Rock wins")

elif user_input == "Paper" and cpu == "Rock":
    print("Paper wins")

elif user_input == "Scissor" and cpu == "Paper":
    print("Scissor wins")

elif user_input == "Paper" and cpu == "Scissor":
    print("Scissor wins")

elif user_input == "Scissor" and cpu == "Rock":
    print("Rock wins")

elif user_input == "Rock" and cpu == "Paper":
    print("Paper wins")

print("\nWanna play again??")