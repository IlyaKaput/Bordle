from tkinter.constants import LEFT, RIGHT, BOTTOM, Y, BOTH, SOLID
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
        global game_over_window
        button['state'] = 'disabled'
        game_over_window = Tk()
        frame = Frame(game_over_window, width=1200, height=50, borderwidth=2, relief=SOLID)
        label = Label(frame, text="You WIN!!!", bg=TriesFrame.RIGHT, font=("Arial", 10), width=20, height=3)
        label.pack(fill='both')
        frame.pack(side=BOTTOM)
        button2 = Button(game_over_window, text='new game', command=lambda: new_game(root_name))
        button2.pack(anchor='ne')
        game_over_window.mainloop()

def new_game(current_window):
    global game_over_window
    current_window.destroy()
    game_over_window.destroy()# Закрываем текущее окно
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