import random

#initial win counter
player_win = 0
comp_win = 0

#game mode selection
def game_mode():
    print("\nSelect game mode: 1 - single life, 2 - three life, 3 - endless")
    mode_code = input("-- ")
    global player_health
    global comp_health
    global fixed_hp
    if mode_code != "1" and mode_code != "2" and mode_code != "3":
        print("Invalid game mode. Please try again.")
        game_mode()
    elif mode_code == "1":
        player_health = 1
        comp_health = 1
        fixed_hp = 1
    elif mode_code == "2":
        player_health = 3
        comp_health = 3
        fixed_hp = 3
    elif mode_code == "3":
        player_health = 999
        comp_health = 999
        fixed_hp = 999
    return mode_code
game_mode()

#takes user input for each round
def new_round():
    print("Select K-9/Deputy/Cow or K/D/C:")
    player_input = input("-- ").upper()
    return player_input

#calculates and prints out current health
def health(player_win, comp_win):
    global player_health
    global comp_health
    print()
    player_health = max(0, fixed_hp - comp_win)
    comp_health = max(0, fixed_hp - player_win)
    print("Player: " + "#" * player_health + "-" * (fixed_hp - player_health))
    print("Computer: " + "#" * comp_health + "-" * (fixed_hp - comp_health))
    if player_health == 0 or comp_health == 0:
        if player_health == 0:
            print("Computer wins the match. You Lost!")
        else:
            print("Player wins the match. Congrats!")
    return player_health, comp_health

#brief introduction to game mechanics
#uses health function and updates global value
#takes user input via nested new_round function
def game_intro():
    if comp_health > 0 and player_health > 0:
        print("K-9 bites Cow, Deputy tases K-9, Cow kicks Deputy")
        return new_round()

#checks input and assigns proper move
def check_input(player_input):
    if player_input in ["K", "K-9", "K9"]:
        player_move = "K-9"
    elif player_input in ["D", "DEPUTY"]:
        player_move = "Deputy"
    elif player_input in ["C", "COW"]:
        player_move = "Cow"
    else:
        print("Unregistered input. Please try again...")
        player_move = 404
    return player_move

def computer_turn(move_options = ["K-9", "Deputy", "Cow"]):
    computer_move = random.choice(move_options)
    return computer_move

#outputs proper message based on player-computer moves
def results(player_move, computer_move, player_win, comp_win):
    if player_move == "K-9":
        if computer_move == "Cow":
            player_win += 1
            print("Your K-9 bites Computer's Cow dealing 1 damage!")
        elif computer_move == "Deputy":
            comp_win += 1
            print("Computer's Deputy tases your K-9. Dealing you 1 damage!")
        else:
            print("Computer chose K-9. Draw!")
    
    if player_move == "Deputy":
        if computer_move == "K-9":
            player_win += 1
            print("Your Deputy tases Computer's K-9 dealing 1 damage!")
        elif computer_move == "Cow":
            comp_win += 1
            print("Computer's Cow kicks your Deputy. Dealing you 1 damage!")
        else:
            print("Computer chose Deputy. Draw!")

    if player_move == "Cow":
        if computer_move == "Deputy":
            player_win += 1
            print("Your Cow kicks Computer's Deputy dealing 1 damage!")
        elif computer_move == "K-9":
            comp_win += 1
            print("Computer's K-9 bites your Cow. Dealing you 1 damage!")
        else:
            print("Computer chose Cow. Draw!")
    return player_win, comp_win

while True:
    if player_health != 999:
        health(player_win, comp_win)
    else:
        print()
        print(f"Player: {player_win}")
        print(f"Computer: {comp_win}")
    player_input = game_intro()
    if player_health > 0 and comp_health > 0:
        computer_move = computer_turn()
        player_move = check_input(player_input)
        player_win, comp_win = results(player_move, computer_move, player_win, comp_win)
    else:
        break