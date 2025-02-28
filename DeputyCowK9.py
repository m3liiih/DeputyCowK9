import random

def new_round():
    print("Select K-9/Deputy/Cow or K/D/C:")
    player_input = input("-- ").upper()
    return player_input

def game_intro():
    print("K-9 bites Cow, Deputy tases K-9, Cow kicks Deputy")
    return new_round()

def check_input(player_input):
    if player_input in ["K", "K-9", "K9"]:
        player_move = "K-9"
    elif player_input in ["D", "DEPUTY"]:
        player_move = "Deputy"
    elif player_input in ["C", "COW"]:
        player_move = "Cow"
    else:
        print("Unregistered input. Please try again...\n")
        new_round()
    return player_move

def computer_turn(move_options = ["K-9", "Deputy", "Cow"]):
    computer_move = random.choice(move_options)