# Rock/Paper/Scissors Game

In this article, we will learn to develop a simple game of rock paper scissors using python.

## At first let us understand the rules of Rock/Paper/Scissors Game

Rock paper scissors is a hand game played between at least two people, where different gestures indicate either of the three: rock, paper, or scissors.

The rules are that:
	- Rock beats scissors
	- Scissors beats papers
	- Paper beats rock
Note : If both the players choose the same gesture, then the game is tied.

In this article we will develop the game of rock paper scissors which will be played by a single player against the computer.

## Perquisites for developing rock/paper/scissors game

The develop the game of rock paper scissors in python following tow modules are required:
	- Tkinter : Easy to use the library of python, used to develop GUI application
	- Random : Module in python that generates **random** numbers

Now we will start doing our code step by step

## Installing the packages

```terminal
iamskydev@github-$ pip install tkinter
imaskydev@github-$ pip install random
```
Using pip one can install any package in python. If the package is already installed it displays the message “Package already exists” otherwise it will install the specific package. 

## Imporing the libraries
```py
from tkinter import *
import random
```
After the package’s installation is complete, we will move on to import the libraries required for our program. Once a library is installed, we can access all the functions available in that library.

After the package’s installation is complete, we will move on to import the libraries required for our program. Once a library is installed, we can access all the functions available in that library.

The random module generates random numbers.

The random module generates random numbers.

## Desinging the window for Rock/Paper/Scissors Game
```py
win = Tk()
win.geometry('400x400')
win.title('Rock-Paper-Scissors')
win.config(bg ='#80dfff')
Label(win, text = 'Rock, Paper ,Scissors' ).pack()
```
In this part, we have basically designed what our output screen will look like.
	- Tk() – initializes the Tkinter
	- geometry() – gives dimension to the output window
	- title() – used to give a title to the window
	- config() – helps in customizing the window. Here we have used it to set a background color
	- Label() – it is basically a widget that contains text which the user can’t modify
## User Input

```py
choices = StringVar()
Label(win, text = 'Rock-Paper-Scissors!!! Choose One!!' ).place(x = 20,y=70)
Entry(win, textvariable = choices ).place(x=90 , y = 130)
```
Here, choices is a string type variable which will store the value entered by the user (rock, paper or scissors)
	- Entry() – another widget used to create input field
	- place() – places the widget at a specified position
## Computer input Rock/Paper/Scissors Game
```py
computer = random.randint(1,3)
if computer == 1:
    computer = 'rock'
elif computer ==2:
    computer = 'paper'
else:
    computer = 'scissors'
```
For computer input, we have to use the random.randint() function, which will choose a random value among 1,2, or 3 and will take the input corresponding to the integer.
	- rock
	- paper
	- scissors
## Desing the game of Rock/Paper/Scissors Game
```py
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
```
In this part, we have used the if-elif-else statement to check various conditions as per the rock paper scissor rules and display the output message accordingly.

## Deffining different functions

**Reset Function :**
```py
def Reset():
    Result.set("") 
    choices.set("")
```
This function will reset the Result value and the choices value for next round

**Exit Function :** 
```py
def Reset():
    Result.set("") 
    choices.set("")
```
This function will terminate the game window.

## Define Buttons
```py
Entry(win, textvariable = Result,width = 50,).place(x=25, y = 250)
Button(win, text = 'PLAY'  ,padx =5, command = play).place(x=150,y=190)
Button(win, text = 'RESET' ,padx =5, command = Reset).place(x=70,y=310)
Button(win, text = 'EXIT'  ,padx =5, command = Exit).place(x=230,y=310)
win.mainloop()
```
This part will create clickable buttons which will carry out different functions
	- Button() – creates buttons
	- command – calls a specific function
	- mainloop() – runs the program continually till the exit button is clicked
## Output : 
![rock_paper_scissors](https://user-images.githubusercontent.com/84164009/124337546-c13cc880-db68-11eb-97f5-7bbe290d88a1.png)

# Summary

<p>So, this was an easy and fun way to create a rock paper scissors game. It is customizable, as per a developer’s personal preference. Not just rock paper scissors, but many more games can be developed easily in Python using various tools and libraries available.</p>
