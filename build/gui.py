import random
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label

#global variables
player_win = 0
comp_win = 0
player_health = 3
comp_health = 3
fixed_hp = 3

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#calculates and update health
def update_health():
    global player_health, comp_health
    player_health = max(0, fixed_hp - comp_win)
    comp_health = max(0, fixed_hp - player_win)

    player_health_label.config(text="Player: " + "#" * player_health + "-" * (fixed_hp - player_health))
    comp_health_label.config(text="Comp: " + "#" * comp_health + "-" * (fixed_hp - comp_health))

    if player_health == 0:
        result_label.config(text="Computer wins the match. You Lost!")
    elif comp_health == 0:
        result_label.config(text="Player wins the match. Congrats!")
    else:
        result_label.config(text="")

    #enables buttons after updating health
    enable_buttons()


def disable_buttons():
    button_k9.config(state="disabled")
    button_deputy.config(state="disabled")
    button_cow.config(state="disabled")


def enable_buttons():
    button_k9.config(state="normal")
    button_deputy.config(state="normal")
    button_cow.config(state="normal")


#displays countdown
def countdown_display(player_move, computer_move):
    result_label.config(text="3")
    window.after(500, lambda: result_label.config(text="2"))
    window.after(1000, lambda: result_label.config(text="1"))
    window.after(1500, lambda: display_choices(player_move, computer_move))


#displays player and computer choices
def display_choices(player_move, computer_move):
    result_label.config(text=f"You chose {player_move}          Computer chose {computer_move}")
    window.after(1500, lambda: check_winner(player_move, computer_move))


#new round
def new_round(player_move):
    if player_health > 0 and comp_health > 0:
        disable_buttons()
        computer_move = computer_turn()
        countdown_display(player_move, computer_move)


# Function to determine the computer's move
def computer_turn():
    return random.choice(["K-9", "Deputy", "Cow"])


# Function to check the winner and update results
def check_winner(player_move, computer_move):
    global player_win, comp_win

    if player_move == "K-9":
        if computer_move == "Cow":
            player_win += 1
            result_label.config(text="K-9 bites Cow dealing Computer 1 damage!")
        elif computer_move == "Deputy":
            comp_win += 1
            result_label.config(text="Deputy tases K-9. Dealing you 1 damage!")
        else:
            result_label.config(text="It's a draw!")

    elif player_move == "Deputy":
        if computer_move == "K-9":
            player_win += 1
            result_label.config(text="Deputy tases K-9 dealing Computer 1 damage!")
        elif computer_move == "Cow":
            comp_win += 1
            result_label.config(text="Cow kicks Deputy. Dealing you 1 damage!")
        else:
            result_label.config(text="It's a draw!")

    elif player_move == "Cow":
        if computer_move == "Deputy":
            player_win += 1
            result_label.config(text="Cow kicks Deputy dealing Computer 1 damage!")
        elif computer_move == "K-9":
            comp_win += 1
            result_label.config(text="K-9 bites Cow. Dealing you 1 damage!")
        else:
            result_label.config(text="It's a draw!")

    window.after(2300, update_health)


#window setup
window = Tk()
window.geometry("720x450")
window.configure(bg="#626262")

#background canvas
canvas = Canvas(
    window,
    bg="#626262",
    height=450,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))

button_k9 = Button(
    image=button_image_3,
    borderwidth=0,
    bg="#626262",
    activebackground="#626262",
    highlightthickness=0,
    command=lambda: new_round("K-9"),
    relief="flat"
)
button_k9.place(x=175, y=279, width=135, height=170)

button_deputy = Button(
    image=button_image_1,
    borderwidth=0,
    bg="#626262",
    activebackground="#626262",
    highlightthickness=0,
    command=lambda: new_round("Deputy"),
    relief="flat"
)
button_deputy.place(x=310, y=274, width=100, height=150)

button_cow = Button(
    image=button_image_2,
    borderwidth=0,
    bg="#626262",
    activebackground="#626262",
    highlightthickness=0,
    command=lambda: new_round("Cow"),
    relief="flat"
)
button_cow.place(x=410, y=279, width=135, height=170)

#health bars
player_health_label = Label(window, text="Player: ###", fg="black", bg="#D9D9D9", font=("Small Fonts", 13))
player_health_label.place(x=23, y=18)

comp_health_label = Label(window, text="Comp: ###", fg="black", bg="#D9D9D9", font=("Small Fonts", 13))
comp_health_label.place(x=603, y=18)

info_label = Label(window, text="K-9 bites Cow, Deputy tases K-9, Cow kicks Deputy", fg="black", bg="#D9D9D9", font=("Small Fonts", 12), wraplength=400)
info_label.place(x=170, y=18)

result_label = Label(window, text="", fg="white", bg="#626262", font=("Small Fonts", 14))
result_label.place(x=360, y=200, anchor="center")

#top ui elements
canvas.create_rectangle(0, 0, 720, 61, fill="#363636", outline="")
canvas.create_rectangle(144, 16, 575, 46, fill="#D9D9D9", outline="")
canvas.create_rectangle(12, 10, 127, 50, fill="#D9D9D9", outline="")
canvas.create_rectangle(592, 10, 707, 50, fill="#D9D9D9", outline="")

window.resizable(False, False)
window.mainloop()