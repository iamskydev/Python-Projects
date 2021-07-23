# Importing all modules
from tkinter import *
from PIL import Image, ImageTk

# First Mad Lib - titled "The Gold"
def first_madlib(win, logo: PhotoImage):
	def finish_madlib(tl: Toplevel, animal='Pig', parent='Mum', month='January', path='grass', movement='walked',
	                  num=12):

		text = f'''
There was once a {animal}. He was always getting told off. One day while his {parent} was sitting in the garden in
{month}, he sneaked out. He did not mean to go far but he saw a glittery thing on the {path} and {movement} over to 
it. He found out it was gold and became rich because he had {num} pieces of gold.'''

		tl.geometry(newGeometry='375x550')

		Label(tl, text='Your Story:', font=("Times", 13, 'bold'), background='Gold', wraplength=tl.winfo_width()).place(x=130, y=310)
		Label(tl, text=text, font=("Times", 13), background='Gold', wraplength=tl.winfo_width()).place(x=0, y=330)

	# Creating the top level widget for the first mad lib game
	ml1_wn = Toplevel(win, bg='Gold')
	ml1_wn.title("The Gold")
	ml1_wn.geometry('375x500')
	ml1_wn.resizable(False, False)
	ml1_wn.iconphoto(False, logo)

	# Creating the labels that will display the text on the screen, with background as "Gold" and font as 20-point Helvetica
	Label(ml1_wn, text='The Gold - Mad Libs', font=("Helvetica", 20, 'bold'), bg='Gold').place(x=60, y=0)

	Label(ml1_wn, text='An animal:', font=("Times", 15), bg='Gold').place(x=0, y=35)
	Label(ml1_wn, text='Choose a parent:', font=("Times", 15), bg='Gold').place(x=0, y=70)
	Label(ml1_wn, text='Choose a month:', font=("Times", 15), bg='Gold').place(x=0, y=110)
	Label(ml1_wn, text='Choose a path:', font=("Times", 15), bg='Gold').place(x=0, y=150)
	Label(ml1_wn, text='Choose a movement type:', font=("Times", 15), bg='Gold').place(x=0, y=190)
	Label(ml1_wn, text='A number:', font=("Times", 15), bg='Gold').place(x=0, y=230)

	#Creating the text input boxes to enter the data in for the user
	animal_entry = Entry(ml1_wn, width=17)
	animal_entry.place(x=250, y=35)
	num_entry = Entry(ml1_wn, width=17)
	num_entry.place(x=250, y=230)

	# Creating an option menu that lists all the days for our user to choose from
	parents = ['Mum', "Dad"]
	months = ['January', 'February', 'March', 'April', 'May', 'June',
	          'July', 'August', 'September', 'October', 'November', 'December']
	movements = ['walked', 'ran']
	paths = ['grass', 'concrete']

	# Variable name was 'strvar' because it is a contraction of "StringVar"
	parent_opt = StringVar(ml1_wn)
	parent_opt.set(parents[0])
	OptionMenu(ml1_wn, parent_opt, *parents).place(x=270, y=70)

	month_opt = StringVar(ml1_wn)
	month_opt.set(months[0])
	OptionMenu(ml1_wn, month_opt, *months).place(x=255, y=110)

	path_opt = StringVar(ml1_wn)
	path_opt.set(paths[0])
	OptionMenu(ml1_wn, path_opt, *paths).place(x=270, y=150)

	movement_opt = StringVar(ml1_wn)
	movement_opt.set(movements[0])
	OptionMenu(ml1_wn, movement_opt, *movements).place(x=265, y=190)

	# Creating a 'Submit' button to add all the inputs to the final story
	submit_btn = Button(ml1_wn, text="Submit", background="SteelBlue", font=('Times', 12),
	                    command=lambda:finish_madlib(ml1_wn, animal_entry.get(), parent_opt.get(), month_opt.get(),
	                                                  path_opt.get(), movement_opt.get(), num_entry.get()))
	submit_btn.place(x=150, y=270)

	ml1_wn.mainloop()


# Second Mad Lib - titled "One Dark, Stormy Night"
def second_madlib(win, logo: PhotoImage):
	def finish_madlib(tl: Toplevel, boy, cloth_article, creature, adj, village, exclamation, fav_thing):
		text = f'''
On one dark, stormy night, {boy} came along. He was wearing nothing but a {cloth_article}. He went into the woods   
and there he found a {creature}! It was {adj}. In fright he ran into a nearby village called {village} screaming, 
"{exclamation}!" The footsteps of the {creature} behind him became louder and louder. The villagers screamed, 
"It's a {adj} {creature}!" 
Taking no prisoners the {creature} demolished the entire village leaving only the trace of someone's {fav_thing}.  
Then it went back into the woods and waited for its next victim to emerge.'''

		tl.geometry(newGeometry='375x700')

		Label(tl, text='Your Story:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='RoyalBlue2').place(x=130, y=335)
		Label(tl, text=text, font=("Times", 13), wraplength=tl.winfo_width(), bg='RoyalBlue2').place(x=0, y=360)

	# Creating the top level widget for the second mad lib game
	ml2_wn = Toplevel(win, bg='RoyalBlue2')
	ml2_wn.title("One Dark, Stormy Night")
	ml2_wn.geometry('375x600')
	ml2_wn.resizable(False, False)
	ml2_wn.iconphoto(False, logo)

	# Creating the labels that will display the text on the screen, with background as "Pink" and font as 20-point Times
	Label(ml2_wn, text='One Dark, Stormy Night - Mad Libs', font=("Times", 17, 'bold'), bg='RoyalBlue2').place(
		x=10, y=0)

	Label(ml2_wn, text='A boy\'s name:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=35)
	Label(ml2_wn, text='An article of clothing:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=70)
	Label(ml2_wn, text='A creature:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=110)
	Label(ml2_wn, text='An adjective:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=150)
	Label(ml2_wn, text='A village name:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=190)
	Label(ml2_wn, text='An exclamation:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=230)
	Label(ml2_wn, text='A favorite thing for yours:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=270)

	# Creating the text input boxes to enter the data in for the user
	boy_name_entry = Entry(ml2_wn, width=19)
	boy_name_entry.place(x=255, y=35)

	cloth_entry = Entry(ml2_wn, width=19)
	cloth_entry.place(x=255, y=70)

	creature_entry = Entry(ml2_wn, width=19)
	creature_entry.place(x=255, y=110)

	adj_entry = Entry(ml2_wn, width=19)
	adj_entry.place(x=255, y=150)

	village_entry = Entry(ml2_wn, width=19)
	village_entry.place(x=255, y=190)

	exclamation_entry = Entry(ml2_wn, width=19)
	exclamation_entry.place(x=255, y=230)

	fav_thing_entry = Entry(ml2_wn, width=19)
	fav_thing_entry.place(x=255, y=270)

	# Creating a 'Submit' button to add all the inputs to the final story
	submit_btn = Button(ml2_wn, text="Submit", background="SteelBlue", font=('Times', 12),
	                    command=lambda: finish_madlib(ml2_wn, boy_name_entry.get(), cloth_entry.get(),
	                            creature_entry.get(), adj_entry.get(), village_entry.get(), exclamation_entry.get(), fav_thing_entry.get()))
	submit_btn.place(x=150, y=300)

	ml2_wn.mainloop()


# Third Mad Lib - titled "Cliff Hanger"
def third_madlib(win, logo: PhotoImage):
	def finish_madlib(tl: Toplevel, boy1, boy2, girl1, girl2, animal, exclamation):
		text = f'''
Once upon a time, two people, {girl1} and {boy1} were walking in the park. They were talking about his {animal}. Then
{boy1} exclaimed, "{exclamation}!" "What is it, {boy1}?" cried {girl1}. "I just remembered something, I have this 
ring in my pocket." said {boy1}. "Why would you have that?" asked {girl1}. "Will you marry me?" {boy1} asked. 
{girl1} replied, "Ummmmmmm... Yes, I Love You, {boy1}!" So they left on {boy1}'s {animal} to their kingdom and had 2 
children named {girl2} and {boy2} and they lived happily ever after as every story should end!'''

		tl.geometry(newGeometry='375x700')

		Label(tl, text='Your Story:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='DarkOrange').place(
			x=130, y=305)
		Label(tl, text=text, font=("Times", 13), wraplength=tl.winfo_width(), bg='DarkOrange').place(x=0, y=330)

	# Creating the top level widget for the second mad lib game
	ml3_wn = Toplevel(win, bg='DarkOrange')
	ml3_wn.title("The Ring")
	ml3_wn.geometry('375x550')
	ml3_wn.resizable(False, False)
	ml3_wn.iconphoto(False, logo)

	# Creating the labels that will display the text on the screen, with background as "Pink" and font as 20-point Times
	Label(ml3_wn, text='The Ring - Mad Libs', font=("Times", 17, 'bold'), bg='DarkOrange').place(
		x=85, y=0)

	Label(ml3_wn, text='A boy\'s name:', font=("Times", 15), bg='DarkOrange').place(x=0, y=35)
	Label(ml3_wn, text='Another boy\'s name:', font=("Times", 15), bg='DarkOrange').place(x=0, y=70)
	Label(ml3_wn, text='A girl\'s name:', font=("Times", 15), bg='DarkOrange').place(x=0, y=110)
	Label(ml3_wn, text='Another girl\'s name:', font=("Times", 15), bg='DarkOrange').place(x=0, y=150)
	Label(ml3_wn, text='An animal:', font=("Times", 15), bg='DarkOrange').place(x=0, y=190)
	Label(ml3_wn, text='An exclamation:', font=("Times", 15), bg='DarkOrange').place(x=0, y=230)

	# Creating the text input boxes to enter the data in for the user
	boy1_name_entry = Entry(ml3_wn, width=19)
	boy1_name_entry.place(x=255, y=35)

	boy2_name_entry = Entry(ml3_wn, width=19)
	boy2_name_entry.place(x=255, y=70)

	girl1_name_entry = Entry(ml3_wn, width=19)
	girl1_name_entry.place(x=255, y=110)

	girl2_name_entry = Entry(ml3_wn, width=19)
	girl2_name_entry.place(x=255, y=150)

	animal_entry = Entry(ml3_wn, width=19)
	animal_entry.place(x=255, y=190)

	exclamation_entry = Entry(ml3_wn, width=19)
	exclamation_entry.place(x=255, y=230)

	# Creating a 'Submit' button to add all the inputs to the final story
	submit_btn = Button(ml3_wn, text="Submit", background="SteelBlue", font=('Times', 12),
	                    command=lambda: finish_madlib(ml3_wn, boy1_name_entry.get(), boy2_name_entry.get(),
	                                                  girl1_name_entry.get(), girl2_name_entry.get(),
	                                                  animal_entry.get(), exclamation_entry.get()))
	submit_btn.place(x=150, y=270)

	ml3_wn.mainloop()


# Creating a GUI master window and placing all its components
root = Tk()
root.title("Projectiamskydevl Mad Libs Generator")
root.geometry('360x300')
root.background='Gainsboro'
root.resizable(False, False)

# Adding an icon to the main window
photo = ImageTk.PhotoImage(Image.open('youricon.png'))
root.iconphoto(False, photo)

Label(root, font=("Comic Sans MS", 16), text='Project Gurukul Mad Libs Generator').place(x=0, y=0)
Label(root, font=("Comic Sans MS", 16), text='Have fun!').place(x=130, y=35)

ml1 = Button(root, text='The Gold', font=("Comic Sans MS", 16), command=lambda: first_madlib(root, photo),
             bg='LightSkyBlue')
ml1.place(x=125, y=90)

ml2 = Button(root, text='One Dark, Stormy Night', font=("Comic Sans MS", 16), command=lambda: second_madlib(root, photo) ,
             bg='LightSkyBlue')
ml2.place(x=50, y=150)

ml3 = Button(root, text='The Ring', font=("Comic Sans MS", 16), command=lambda: third_madlib(root, photo),
             bg='LightSkyBlue')
ml3.place(x=125, y=210)

root.update()
root.mainloop()