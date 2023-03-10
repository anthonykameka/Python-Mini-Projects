#Number Guessing Game 

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

logo = """
 .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____  _____  | || | _____  _____ | || | ____    ____ | || |   ______     | || |  _________   | || |  _______     | | | |    ______    | || | _____  _____ | || |  _________   | || |    _______   | || |    _______   | || |     _____    | || | ____  _____  | || |    ______    | |
| ||_   \|_   _| | || ||_   _||_   _|| || ||_   \  /   _|| || |  |_   _ \    | || | |_   ___  |  | || | |_   __ \    | | | |  .' ___  |   | || ||_   _||_   _|| || | |_   ___  |  | || |   /  ___  |  | || |   /  ___  |  | || |    |_   _|   | || ||_   \|_   _| | || |  .' ___  |   | |
| |  |   \ | |   | || |  | |    | |  | || |  |   \/   |  | || |    | |_) |   | || |   | |_  \_|  | || |   | |__) |   | | | | / .'   \_|   | || |  | |    | |  | || |   | |_  \_|  | || |  |  (__ \_|  | || |  |  (__ \_|  | || |      | |     | || |  |   \ | |   | || | / .'   \_|   | |
| |  | |\ \| |   | || |  | '    ' |  | || |  | |\  /| |  | || |    |  __'.   | || |   |  _|  _   | || |   |  __ /    | | | | | |    ____  | || |  | '    ' |  | || |   |  _|  _   | || |   '.___`-.   | || |   '.___`-.   | || |      | |     | || |  | |\ \| |   | || | | |    ____  | |
| | _| |_\   |_  | || |   \ `--' /   | || | _| |_\/_| |_ | || |   _| |__) |  | || |  _| |___/ |  | || |  _| |  \ \_  | | | | \ `.___]  _| | || |   \ `--' /   | || |  _| |___/ |  | || |  |`\____) |  | || |  |`\____) |  | || |     _| |_    | || | _| |_\   |_  | || | \ `.___]  _| | |
| ||_____|\____| | || |    `.__.'    | || ||_____||_____|| || |  |_______/   | || | |_________|  | || | |____| |___| | | | |  `._____.'   | || |    `.__.'    | || | |_________|  | || |  |_______.'  | || |  |_______.'  | || |    |_____|   | || ||_____|\____| | || |  `._____.'   | |
| |              | || |              | || |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

"""


        

def play_game():
    print(logo)
    print("Welcome to AK's Crazy Number Guessing Game!!!")
    print("I'm thinking of a number between 1-100")
    attempts = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
    if difficulty.lower() == 'easy':
        attempts = 10
    elif difficulty.lower() == 'hard':
        attempts = 5

    winning_number = random.randint(1, 100)

    while attempts > 0:
        guess = int(input("Guess a number: \n"))
        if guess == winning_number:
            print("You won! That was the right number")
            return
        elif guess > winning_number:
            print("Too high!")
            attempts -= 1
        else:
            print("Too Low!")
            attempts -= 1
        
    print(f"You ran out of guesses.. the answer was {winning_number}")

play_game()




