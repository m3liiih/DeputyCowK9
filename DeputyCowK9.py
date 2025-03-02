import random

player_health = 3
player_win = 0
comp_health = 3
comp_win = 0
current_round = 0

def health(player_health, comp_health, player_win, comp_win):
    player_health = max(0, player_health - comp_win)
    comp_health = max(0, comp_health - player_win)
    print("Player: " + "#" * player_health + "-" * (3 - player_health))
    print("Computer: " + "#" * comp_health + "-" * (3 - comp_health))
    if player_health == 0 or comp_health == 0:
        if player_health == 0:
            print("Computer wins the match. You Lost!")
        else:
            print("Player wins the match. Congrats!")
    return player_health, comp_health

def new_round():
    if current_round >= 1:
        health(player_health, comp_health, player_win, comp_win)
    print("Select K-9/Deputy/Cow or K/D/C:")
    player_input = input("-- ").upper()
    return player_input

def game_intro():
    print()
    health(player_health, comp_health, player_win, comp_win)
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
    return computer_move

def results(player_move, computer_move, player_win, comp_win):
    if player_move == "K-9":
        if computer_move == "Cow":
            player_win += 1
            print("Computer chose Cow. You Won!")
        elif computer_move == "Deputy":
            comp_win += 1
            print("Computer chose Deputy. You Lost!")
        else:
            print("Computer chose K-9. Draw!")
    
    if player_move == "Deputy":
        if computer_move == "K-9":
            player_win += 1
            print("Computer chose K-9. You Won!")
        elif computer_move == "Cow":
            comp_win += 1
            print("Computer chose Cow. You Lost!")
        else:
            print("Computer chose Deputy. Draw!")

    if player_move == "Cow":
        if computer_move == "Deputy":
            player_win += 1
            print("Computer chose Deputy. You Won!")
        elif computer_move == "K-9":
            comp_win += 1
            print("Computer chose K-9. You Lost!")
        else:
            print("Computer chose Cow. Draw!")
    return player_win, comp_win

while player_health != 0 or comp_health != 0:
    player_input = game_intro()
    computer_move = computer_turn()
    player_move = check_input(player_input)
    player_win, comp_win = results(player_move, computer_move, player_win, comp_win)