import tkinter as tk
from tkinter import Entry
from tkinter.constants import BOTTOM, RIGHT

from WeaponChecker import WeaponChecker


def changeSize():
    print(WeaponChecker.check_weapon(entry.get()))
    print()


WeaponChecker.set_weapon(WeaponChecker.weapon_info.iloc[3])
root = tk.Tk()
root.title = "testName"
root.geometry("250x250")
root.resizable(False, False)
button = tk.Button(text="check", command=changeSize)
button.pack(anchor="ne")
entry = tk.Entry()
entry.pack(anchor="nw")

root.mainloop()
