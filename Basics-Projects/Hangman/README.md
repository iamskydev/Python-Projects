# Hangman Project

## What is Hangman?

It is a pen and paper game based on guessing, played between two or more players. The number of guesses is limited. One person picks a word, and the other players try to guess that letter by letter, within the limited number of guesses. If they successfully spell out the word in the given number of guesses, they win, or else they lose.

# Implementation

###  Step 1 : Importing Modules

First, we will import **random** and **time** modules. The **choice()** method from the **random**  module will be used to pick random words from our word lists and the **sleep()** method from the time module will be used to introduce delays where needed.
```py
import random
import time
```
### Step 2 : Create word/lists and variables

Next, we will create our word **list(s)** that will be used by the program to pick words randomly for the players to guess. I created two lists in this program: **the first one has fruit names and the second one consists of superhero names**. The two lists were created to give the players the option of picking the category for the word they would like to guess. You can make one or more word lists depending on the number of categories you want to add in the game.
```py
fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya'] 
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', ‘aquaman']
```
We will create a few variables to store the game statistics:
```py
userGuesslist = []
userGuesses = []
playGame = True
category = ""
continueGame = “Y"
```
### Step 3 : Game/Info

We will prompt the player for their name and store it in a variable. Before starting the game, we display some details about the game. Here we are using the time module’s **sleep()** method to pause for a few seconds between the displays.
```py
name = input("Enter your name: ")
print("Hello", name.capitalize(), "let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let the fun begin!")
time.sleep(1)
```
### Step 4 : Choosing a random word from the desired category

Next, we will add the logic to allow the program to **choose a random word from the desired category**. This is how the code looks like.
```py
while True:
    if category.upper() == 'S':
        secretWord = random.choice(superHeroes)
        break
    elif category.upper() == 'F':
        secretWord = random.choice(fruits)
        break
    else:
        category = input("Please select a valid category: F for Fruits / S for Super-Heroes; X to exit")

    if category.upper() == 'X':
        print("Bye. See you next time!")
        playGame = False
        break
```
<p>Here we will make use of the **while loop** and **if/elif/else conditionals** to pick the random word. The players are given an option to choose a category **(Fruits / Superheroes)** for the word they would like to guess. An option to exit the game is also provided, in case they decide not to play.<br>
The if block of the code will be executed if the player chooses ’S’ indicating that they want to play the game with words from the **superhero** category. In this case, a word from the **superHeroes** list will be picked randomly using the **random.choice** from **random** module. The word will then be stored in the **secretWord** variable.<br>
The **elif (else if) block** of the code will be executed if the player chooses **F** indicating that they want to play the game with words from the **fruit** category. In this case, a word from the **fruits** list will be picked randomly using the **random.choice** from the **random** module and stored in the **secretWord** variable.</p>
------
<p>If the player chooses any other letter apart from **S** / **F**, the player will be prompted to select a valid category (**S** or **F**) or **X** to exit. Note the use of **upper()** for converting the input to upper case before validating the category. Since we want to force the player to select a correct option or exit the game, we will wrap our **if/elif/else block** inside a **while** **True (forever loop) block**. We are using the keyword **break** to break out of the loop once the right option is chosen.<br>
The **else block** will be executed if the player chooses **X** indicating a desire to quit the game. In this case, the rest of the program will not be executed and the game will end.<br>
We are using a boolean variable **playGame** to facilitate this. A value of **True** will allow the players to continue playing the game and a value of **False** will allow them to quit the game. This variable **is initialized** with the value **True** at the beginning of the game assuming that the players invoke the program with a desire to play the game.<br>
If the player opts to quit the game by choosing **X**, the boolean **playGame** is set to **False** which results in bypassing the portion of the program containing the game logic and the game ends.</p>

### Step 5 : Showing blank lines for every letter in the chosen word
<p>This step is executed once the player selects a category for the word list. After the random word is chosen by the program we want to show the player placeholders (we are using blank lines in this program) for every letter in the chosen word. **The number of placeholders indicates the length of the word to be guessed**.  Here’s how we will accomplish it:<br>
Note that this part of the program will run only if the player chooses the right category for the word list. We also need to ensure that this part of the code is not executed if the player wants to quit the game. If the player selects a correct category and does not want to quit the game, the boolean **playGame** will have a value **True**. We check the value of this variable using an **if condition**.<br>
We will first convert our **secretWord** to a list and store it in a variable called **secretWordList**.</p>
```py
if playGame:
    secretWordList = list(secretWord)
```
<p>In order to make the game interesting, we are also **limiting the number of allowed attempts dynamically based on the secret word**. In this program, the number of attempts allowed is being limited to two more than the number of letters in the secret word. In order to achieve this, we **need to keep track of the length of the secret word** as well as **the number of attempts** the player took to guess the word. The length property is used to find the length of the **secretWord** variable. The **number of allowed attempts is set by adding 2 to this length** and stored it in the variable **attempts**. This variable will be used to track the number of attempts remaining as the game progresses.</p>
```py
attempts = (len(secretWord) + 2)
```
<p>Every time the player makes a guess the number of attempts will be reduced by 1 (**attempts -= 1**) till the player guesses the correct word or there aren’t any more attempts left (**attempts == 0**)<br>
Now, we will work on showing the **placeholders** for the secret word. For this, we will first create a variable called **userGuesslist**. We will initiate this variable with an **empty list**.</p>
```py
userGuesslist = []
```
Next,  we will loop through our **secretWordList** list and for each element in the list we will append an **_**  to our **userGuesslist** list.
```py
#Adding blank lines to User List to create the blank secret work
    for n in secretWordList: 
        userGuesslist.append(‘_') 
    printGuessedLetter()
```
To display our **userGuesslist** we will create a function **printGuessedLetter()** and use it every time we want to print our list.
```py
#Utility function to print User Guess List
def printGuessedLetter():
    print("Your Secret word is: " + ''.join(userGuesslist))

print("The number of allowed guesses for this word is:", attempts)
```
### Step 6 : Logic to ask for a letter and display it in the placeholder
<p>Next, we will work on the logic of asking the player to enter a letter until they guess the word correctly or run out of allowed attempts. If the letter is in the chosen word, we will add the letter to the correct position in our **userGuesslist** list and then display the list.<br>
We will start by creating a **while loop** to keep asking for letter input from the player.</p>
```py
#starting the game
while True: 

    print("Guess a letter:")
    letter = input()
```
Next, we will check if the letter input by the player has already been entered. We will create an **empty userGuesses list** and every time the player enters a letter we will append that to the **userGuesses** list. If the letter exists in the **userGuesses** list, we will ask the player to choose another letter.
```py
if letter in userGuesses:
    print("You already guessed this letter, try something else.")

else:
    attempts -= 1
    userGuesses.append(letter)
    if letter in secretWordList:
        print("Nice guess!")
        if attempts > 0:
            print("You have ", attempts, 'guess left!’)
```
Otherwise, the program will loop through our **secretWordList** , get the index of the letter input and in the same index number, add the letter in the **userGuesslist** list.
```py
for i in range(len(secretWordList)):
    if letter == secretWordList[i]:
        letterIndex = i
        userGuesslist[letterIndex] = letter.upper()
        printGuessedLetter()

    else:
        print("Oops! Try again.")
        if attempts > 0:
            print("You have ", attempts, 'guess left!')
            printGuessedLetter()
```
### Step 7 : Win/Loss Logic

We are almost at the end of our game. Here we will work on our **win / loss** logic.<br>
We will join the **userGuesslist** variable and store it in the variable **joinedList**.
```py
joinedList = ‘'.join(userGuesslist)
```
To determine **win / loss** we will compare the **secretWord** (the computer chosen word) with the **joinedList** variable. If they both match, the player will win. As mentioned earlier, after each guess, we will also track the number of attempts remaining to check if it equals **0** , in which case the player will **lose**.
```py
if joinedList.upper() == secretWord.upper():
    print("Yay! you won.")
    break
elif attempts == 0:
    print("Too many Guesses!, Sorry better luck next time.")
    print("The secret word was: "+ secretWord.upper())
    break
```
### Step 8 : Play/Again Logic

<p>Last but not least we will work on the **Play Again** logic for the game. We prompt the player to check if they want to play again and will store the response in a variable.<br>
If the player wants to play again, we will prompt the word category thereby allowing the player to change it from their previous selection. We will also empty the ‘userGuessList’ list and the **userGuesses** list to reset them so that the new game is tracked properly. We will also set the **playGame** boolean variable to **True**.<br>
If the player chooses not to play again, we will **break out of the loop in the else block**.</p>
```py
continueGame = input("Do you want to play again? Y to continue, any other key to quit")
if continueGame.upper() == 'Y':
    category = input("Please select a valid categary: F for Fruits / S for Super-Heroes")
    userGuesslist = []
    userGuesses = []
    playGame = True
else:
    print("Thank You for playing. See you next time!")
    break
```
## Here is the complete code for the game: [Source Code]()

# Summary

<p>You will write a program using the python language to create a simple console game of the word guessing game called hangman. Your program should read from a file containing a list of words, choose a random word, and allow the user to guess letters. The game should only allow the user to guess wrong 6 times before they lose, drawing more of the man each time. If the user guess the full word without guessing wrong 6 times, they win!</p>
