from Tkinter import *
import random

def randomSelect():
    #put items in a list
    menu = ["Chili's Grill & Bar", "BJ's Restaurant & Brewhouse", "Ma's", "Panda Express", "Chipotle Mexican Grill", "MOD Pizza", "Gen Korean BBQ House", "Five Guys", "TOGO'S Sandwiches", "Baja Fresh Mexican Grill", "Rubio's Coastal Grill", "McDonald's", "Denny's", "Subway"]
    #get a random number
    randNum = random.randrange(0, 1000000001, 1)
    #pickup an item based on the random number
    itemNum = randNum % len(menu)
    label = Label(root, text= "Hey bro, this is what you will have:\n" + menu[itemNum])
    label.config(font=("Courier", 17))
    #this creates a new label to the GUI
    label.pack() 

root = Tk()
w = 600 # width for the Tk root
h = 300 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
button = Button(root, text="Get Me Food Bro", command=randomSelect) 
button.place(relx=0.5, rely=0.3, anchor=CENTER)
button.config(font=("Courier", 17))
root.mainloop() # starts the mainloop
