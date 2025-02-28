import random

def new_round():
    print("Select K-9/Deputy/Cow or K/D/C:")
    global player_input
    player_input = input("-- ").upper()
    return player_input

def game_intro():
    print("K-9 bites Cow, Deputy tases K-9, Cow kicks Deputy")
    new_round()
game_intro()

def new_round():
    print("Select K-9/Deputy/Cow or K/D/C:")
    player_input = input("-- ")

def computer_turn(move_options = ["K-9", "Deputy", "Cow"]):
    computer_move = random.choice(move_options)