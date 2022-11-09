from tkinter import *
from PIL import ImageTk, Image
import time

import random

root = Tk()
root.title("Colorgame")
root.geometry("800x500")

#function Roll dice
def roll_dice():

    #countdown
    sleeptime = time.sleep(3)

    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)
    d3 = random.choice(my_dice)

    dice_label1.config(text=d1.upper(), bg=d1)
    dice_label2.config(text=d2.upper(), bg=d2)
    dice_label3.config(text=d3.upper(), bg=d3)

# Create A Dice list
my_dice = ['red', 'blue', 'white', 'green', 'yellow', 'pink']

#Create a Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

#Create Dice Labels
dice_label1 = Label(my_frame, text='', font=("Noto Sans",50))
dice_label1.grid(row=0, column=0, padx=5)

dice_label2 = Label(my_frame, text='', font=("Noto Sans",50))
dice_label2.grid(row=0, column=1, padx=5)

dice_label3 = Label(my_frame, text='', font=("Noto Sans",50))
dice_label3.grid(row=0, column=3, padx=5)

#timer
time_label = Label(my_frame, text='Time', font=("Noto Sans",50))
time_label.grid(row=1, column=1, padx=5)

#Create Roll Button
my_button = Button(root, text="Taya para Manalo", command=roll_dice, bg='gold')
my_button.pack(pady=50)

frame = Frame(root, width=600, height=400)
frame.pack()
#frame.place(anchor='center', relx=0.5, rely=0.5)


# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("colorgame.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

root.mainloop()
