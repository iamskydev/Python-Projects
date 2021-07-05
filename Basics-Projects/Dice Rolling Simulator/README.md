# Dice Rolling Simulator Python Project

We will use the Tkinter library to build a basic GUI for the dice simulation application, do not worry if you do not know Tkinter or haven't work on it, I will explain each and everything we will use, so first let's see the basic intuition about Tkinter.

#  What is Tkinter?

Python provides many packages to build GUI. Tkinter is the most common, fast, and object-oriented interface which is easy to use python package used to build GUI. Tkinter is a pre-installed package when you install python, so no need to install it separately. Also, when you develop an application, you can use it on any platform which reduces the need for amendments required to use it on Windows, Mac, or Linux.

# Dice Rolling Simulator in Python

We all know about dice, which is a cube-like structure numbered 1-6 written on its face. But what is simulation? Simulation is a computer model that rolls dice for us.
let's get started with code and understand each and every step.

## Step 1 : Importing the libraries required

We will import the following libraries
- Tkinter: we will use Tkinter to make our GUI.
- Image, ImageTk; imported from PIL i.e It is used to perform any task related to Image. we will use it to load and display images. you only import this package, no need to install it.
- Random: Imported to generate a different random number from 1-6.

**Code**
```py
import Tkinter
from PIL import Image, ImageTK
import random
```
## Step 2 : Building a Top-level widget to make the main window for our application

Developing a desktop-based application using Python Tkinter is not a complex task. an empty Tkinter top-level window can be created by using the following steps:
- Import Tkinter, we have already imported
- Create the main application window
- Add widgets like labels, buttons, check buttons, etc.
- Call the main loop so, that actions can take place on the user's computer screen.

**Code**
```py
#create top-level widget that represent window of application
    root = tkinter.Tk()    
    root.geometry('400x400')
    root.title('Crazy_Tech Dice Simulator')

    #call the mainloop to run the application
    root.mainloop()

```
## Step 3 : Designing a Heading and Image area

Now, we have to add a heading and image area with a button to make our main application. so let's create a label for heading after leaving one blank line to make a window look good.

**Code**
```py
blankLine = tkinter.label(root, text="")  
blankline.pack()  

#add a heading with font and formatting    
HeadingLabel = tkinter.label(root, text="Hello from Crazy_Tech", fg="red", bg="black", font="Helvetica 16 bold italic")    
HeadingLabel.pack()
```
Here, we will use the pack() method to arrange our widget in rows and columns. pack() method widget is used to organize widget in form of block.
- **root** : It is the name of our main window, to which we have to add a specified widget.
- text** : text to be displayed in the heading label.
- **fg** : font color of heading
- **bg** : background color of heading
- **.pack()** :used to pack the widget onto the main window(root).

## Step 4 : Form a list of Images to be randomly displayed

```py
 dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png'] 

#simulate a dice to generate a random number between 1 to 6. 
DiceImage = ImageTk.PhotoImage(Image.open(random.choose(dice)))
```
When our window opens with the button we have to display one default image of dice with any random number generated on it. here, dice is our list of 6 random image file names kept in the same python program directory. then, we have used a random module to pick any one image from the list, after that with help of the Image library we have opened the image, and using ImageTk we load the image in our window.
you can download all the images with the source code from the link given below at end of the article.

## Step 5 : Construct a label for Image, add a button and assign it a Functionality

Now, we have to provide a button to roll a dice and whenever a button is clicked, we have to generate a different number and update the particular image on our image window. and for this first, we will create a label for the image and display a default image, that we have created in the previous step.
```py
#construct a label widget for image 
ImageLabel = tkinter.Label(root, image=DiceImage) 
ImageLabel.pack(expand=True) 

#Function to roll a dice and generate different number 
def rolling_dice():
  DiceImage = ImageTk.PhotoImage(Image.open(random.choose(dice))) 
  #update the image  
  ImageLabel.configure(image=DiceImage) 
  #keep a refrence  
  ImageLabel.image = DiceImage 

#adding a button and cmd will use rolling_dice function 
button = tkinter.Button(root, text="Roll the Dice" fg="black", bg="light blue", command=rolling_dice) 
#pack a widget in parent window 
button.pack(expand=True) 
```
The parameter expand declares as True so that even if we resize the window the image remains in the center.

## Step 6 : Call the mainloop

Call the mainloop to run the application. It acts as the main function of our program.
```py
#call the mainloop 
root.mainloop() 
```
Here the source code the Rolling Dice Simulator Game in Python [Source Code]()
# Summary

We have successfully developed a cool application - Dice Simulator using Python. It's a lovely solution, hope you enjoyed it. Now you can simply click on a button and get your next number on dice. Thanks and cheers to python and its package Tkinter which has provided us such a function to make our work easy. As of now, we have an understanding of Python, Tkinter, and random.
