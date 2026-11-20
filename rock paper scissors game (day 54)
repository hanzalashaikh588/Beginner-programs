#rock paper scissors game.
#Rock-Paper, Paper-Rock, Rock-Scissors, Scissors-Rock, Paper-Scissors, Scissors-Paper.
def function_game():
    import random
    choices = ["rock", "paper" , "scissors"]
    print("welcome to rps game!")
    play = input("do you wish to play?(Yes/No) : ").capitalize()
    if (play == "Yes"):
        player_choice = input("choose between rock , paper and scissors : ").lower()
        python_choice = random.choice(["paper","rock","scissors"])
        print(f"python chose {python_choice}")
    else:
        print("goodbye")
        return

    beats = {
        "rock":"scissors",
        "paper": "rock",
        "scissors":"paper"
    }

    if (player_choice == python_choice):
            print("Draw")
    elif beats[player_choice] == python_choice:
        print("You Win!")
    else:
        print("You Lose")
    return
function_game()
