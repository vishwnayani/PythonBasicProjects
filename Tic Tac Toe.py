from tkinter import *
import random
def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column].config(text = player)
            if check_winner() is False:
                player = players[1]
                label.config(text="player:{}".format(players[1]))
            elif check_winner() is True:
                label.config(text="winner is : " + players[0])
            elif check_winner() == 'Tie':
                label.config(text = 'Tie')
        else:
            buttons[row][column].config(text = player)
            if check_winner() is False:
                player = players[0]
                label.config(text="player:{}".format(players[0]))
            elif check_winner() is True:
                label.config(text = 'winner is : ' + players[1])
            elif check_winner() == 'Tie':
                label.config(text = 'Tie')
def restart():
    global player
    player = random.choice(players)
    label.config(text="player:{}".format(player))
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg = 'white')


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg = 'green')
            buttons[row][1].config(bg = 'green')
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg = 'green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg = 'green')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    elif check_empty() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return "Tie"
    return False
def check_empty():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else: return True
window = Tk()
window.title('Tic Tac Toe game')
window.geometry("700x700")
players = ["x", "o"]
buttons = [[0,0,0],[0,0,0],[0,0,0]]
player = random.choice(players)
label = Label(window, text="Player:{}".format(player), width = 20, height = 3, font = ('consolas', 25))
label.pack()
Restart = Button(window, text="Restart", command=restart)
Restart.pack()
frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", width = 9, height=4, font=("consolas", 20), command = lambda row = row, column = column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
