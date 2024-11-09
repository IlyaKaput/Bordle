import tkinter as tk
from tkinter.constants import BOTTOM, RIGHT

from PIL import Image, ImageTk

from Testing import weapon_info
from WeaponChecker import WeaponChecker

def change_size(label):
    global i
    image = Image.open('pictures/'+'_'.join(weapon_info.iloc[i]['Name'].split()).lower() + '.png')
    pic = ImageTk.PhotoImage(image)
    label.config(image=pic)
    label.image = pic
    label.pack()
    i += 1



i = 0
WeaponChecker.set_weapon(WeaponChecker.weapon_info.iloc[3])
root = tk.Tk()
root.title = "testName"
root.geometry("750x250")
root.resizable(True, True)
label = tk.Label()
button = tk.Button(text="check", command=lambda: change_size(label))
button.pack(anchor="ne")
label.pack(anchor="sw")

root.mainloop()
