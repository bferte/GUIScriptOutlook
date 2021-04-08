import tkinter as tk


from PIL import Image, ImageTk
from tkinter import filedialog
import os

from utils.loadConfig import loadConfig
from utils.saveConfig import saveConfig


#import saved path
#tempdir = loadConfig()


root = tk.Tk()


#canvas = tk.Canvas(root, width=600, height=300)
#canvas.grid(columnspan=3, rowspan=3)


#Logo
logo = Image.open('OOLogo1.png')
#logo = logo.resize((422,142))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#Instructions
instructions = tk.Label(root, text="Choisissez le dossier à cibler", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("Chargement...")

    currdir = os.getcwd()


    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose %s" % tempdir)
        browse_text.set("Rechercher")
        saveConfig(tempdir)
        selectedR.set(tempdir)

        

#Selected Folder
selected_text = tk.Label(root, text="Le dossier ciblé à pour chemin : ", font="Raleway")
selected_text.config(font=("Raleway",20))
selected_text.grid(columnspan=2, column=0, row=3, ipady=20,sticky="n")     

# load saved path
tempdir = ""
tempdir = loadConfig()

selectedR = tk.StringVar()
if tempdir == "":
    selectedR.set("(aucun dossier sélectionné)")
else:
    selectedR.set(tempdir)

# selected Result
selectLabel = tk.Label(root, textvariable=selectedR,font="Raleway")
selectLabel.grid(columnspan=3, column=0,row=5)


#Brows Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font='Raleway',bg='#20bebe', fg="white", height=2, width=15)
browse_text.set("Rechercher")
browse_btn.grid(column=1, row=2)







canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3, rowspan=3)


root.mainloop()