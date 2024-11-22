from tkinter.constants import LEFT, RIGHT, BOTTOM, Y, BOTH
from tkinter import Canvas, Label, Scrollbar, Frame
from TriesFrame import TriesFrame
from WeaponChecker import WeaponChecker
from tkinter import Entry, Button, Tk



def check_weapon(entry, tries_frame, button, root_name):
    weapon_name_to_check = entry.get()
    if WeaponChecker.check_weapon(weapon_name_to_check) == -1:
        entry.delete(0, len(weapon_name_to_check))
        return
    tries_frame.add_weapon_try(WeaponChecker.check_weapon(weapon_name_to_check),
                               WeaponChecker.get_weapon(weapon_name_to_check))
    entry.delete(0, len(weapon_name_to_check))
    if tries_frame.game_is_over:
        button['state'] = 'disabled'
        button2 = Button(text='new game', command=lambda: new_game(root_name))
        button2.pack(anchor='ne')

def new_game(current_window):
    current_window.destroy()  # Закрываем текущее окно
    main()


def main():
    WeaponChecker.choose_random_weapon()
    root = Tk()
    root.geometry("1140x500")
    root.resizable(False, False)
    entry = Entry()
    entry.pack(anchor='nw')
    button = Button(text='check', command=lambda: check_weapon(entry, tries_frame, button, root))
    button.pack(anchor='ne')

    canvas = Canvas(root)
    tries_frame = TriesFrame(canvas, width=1200, height=500)
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((-600, 900), window=tries_frame, anchor="nw")
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(fill=BOTH, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()