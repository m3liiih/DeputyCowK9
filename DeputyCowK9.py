import random

def game_intro():
    print("K-9 bites Cow, Deputy tases K-9, Cow kicks Deputy\n"
    "Select K-9/Deputy/Cow or K/D/C:")
    player_input = input("-- ")
game_intro()

def new_round():
    print("Select K-9/Deputy/Cow or K/D/C:")
    player_input = input("-- ")

def computer_turn(move_options = ["K-9", "Deputy", "Cow"]):
    computer_move = random.choice(move_options)