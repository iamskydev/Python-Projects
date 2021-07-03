# Importing Libraries
from tkinter import *
import random

#Desinging the window
win = Tk()
win.geometry('400x400')
win.title('Rock-Paper-Scissors')
win.config(bg ='#80dfff')
Label(win, text = 'Rock, Paper ,Scissors' ).pack()

# User input
choices = StringVar()
Label(win, text = 'Rock-Paper-Scissors!!! Choose One!!' ).place(x = 20,y=70)
Entry(win, textvariable = choices ).place(x=90 , y = 130)

# Computer Input
computer = random.randint(1,3)
if computer == 1:
    computer = 'rock'
elif computer ==2:
    computer = 'paper'
else:
    computer = 'scissors'

# Desing Game
Result = StringVar()
def play():
    ch = choices.get()
    if ch == computer:
        Result.set('Its a Tie')
    elif ch == 'paper' and computer == 'rock':
        Result.set('Computer selected Rock!!You Win!!')
    elif ch == 'paper' and computer == 'scissors':
        Result.set('Computer selected Scissors!!You Lose!!')
    elif ch == 'rock' and computer == 'paper':
        Result.set('Computer selected Paper!! You Lose!!')
    elif ch == 'rock' and computer == 'scissors':
        Result.set('Computer selected Scissors!!You Win!!')
    elif ch == 'scissors' and computer == 'rock':
        Result.set('Computer selected Rock!!You Lose!!')
    elif ch == 'scissors' and computer == 'paper':
        Result.set('Computer selected Paper!!You Win!!')
    else:
        Result.set('Invalid Entry: Choose: rock, paper, scissors')

# Reset Function
def Reset():
    Result.set("") 
    choices.set("")

# Exit Function
def Exit():
    win.destroy()

# Define buttons
Entry(win, textvariable = Result,width = 50,).place(x=25, y = 250)
Button(win, text = 'PLAY'  ,padx =5, command = play).place(x=150,y=190)
Button(win, text = 'RESET' ,padx =5, command = Reset).place(x=70,y=310)
Button(win, text = 'EXIT'  ,padx =5, command = Exit).place(x=230,y=310)
win.mainloop()
