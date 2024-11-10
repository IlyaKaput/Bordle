from TriesFrame import TriesFrame
from WeaponChecker import WeaponChecker
from tkinter import Entry, Button, Tk


def check_weapon(entry, tries_frame):
    weapon_name_to_check = entry.get()
    if WeaponChecker.check_weapon(weapon_name_to_check) == -1:
        entry.delete(0, len(weapon_name_to_check))
        return
    tries_frame.add_weapon_try(WeaponChecker.check_weapon(weapon_name_to_check),
                               WeaponChecker.get_weapon(weapon_name_to_check))
    entry.delete(0, len(weapon_name_to_check))


def main():
    WeaponChecker.choose_random_weapon()
    root = Tk()
    root.geometry("1000x500")
    root.resizable(False, False)
    entry = Entry()
    entry.pack(anchor='nw')
    button = Button(text='check', command=lambda: check_weapon(entry, tries_frame))
    button.pack(anchor='ne')
    tries_frame = TriesFrame(height=100, width=100)
    tries_frame.pack(anchor='sw')
    root.mainloop()


if __name__ == "__main__":
    main()
