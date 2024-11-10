from tkinter import Frame, Label, PhotoImage
from tkinter.constants import BOTTOM, SOLID, LEFT
from PIL import Image, ImageTk


class TriesFrame(Frame):
    WRONG = "#FF6666"
    RIGHT = "#66FF66"
    SEMI_RIGHT = "#FFFF66"
    @staticmethod
    def resize(image):
        width, height = image.size
        if width >= height*4:
            return image.resize((200, int(height*200/width)))
        else:
            return image.resize((int(width*50/height), 50))

    #Добавление всей информации об оружии на главный экран
    def add_weapon_try(self, check_results, weapon):
        frame = Frame(self, width=1500, height=10, borderwidth=1, relief=SOLID)
        self.add_weapon_picture(weapon, frame)
        self.add_weapon_name(check_results, weapon, frame)
        self.add_weapon_rarity(check_results, weapon, frame)
        self.add_weapon_location(check_results, weapon, frame)
        self.add_weapon_type(check_results, weapon, frame)
        self.add_weapon_drop_chance(check_results, weapon, frame)
        frame.pack(side=BOTTOM)

    # Поиск и добавление картинки оружия
    def add_weapon_picture(self, weapon, frame):
        img = Image.open('pictures/' + '_'.join(weapon['Name'].lower().split()) + '.png')
        img = TriesFrame.resize(img)
        image = ImageTk.PhotoImage(img)
        label = Label(frame, width=200, height=50, image=image)
        label.photo = image
        label.pack(side=LEFT)

    # Добавление имени оружия
    def add_weapon_name(self,check_results, weapon, frame):
        bg_color = TriesFrame.WRONG
        if check_results[0]:
            bg_color = TriesFrame.RIGHT
        label = Label(frame, text=weapon['Name'], bg=bg_color, font=("Arial", 10), width=20, height=3)
        label.pack(side=LEFT)

    # Добавление редкости оружия на экран
    def add_weapon_rarity(self, check_results, weapon, frame):
        text = weapon['Rarity']
        if check_results[1] == 1:
            text += '↓'
        elif check_results[1] == -1:
            text += '↑'
        bg_color = TriesFrame.WRONG
        if check_results[1] == 0:
            bg_color = TriesFrame.RIGHT
        label = Label(frame,  text=f"Rarity:\n {text}", bg=bg_color, font=("Arial", 10), width=20, height=3)
        label.pack(side=LEFT)

    # Добавление редкости оружия
    def add_weapon_location(self, check_results, weapon, frame):
        bg_color = TriesFrame.WRONG
        if check_results[2] == 2:
            bg_color = TriesFrame.RIGHT
        elif check_results[2] == 1:
            bg_color = TriesFrame.SEMI_RIGHT
        label = Label(frame, text=f"Location:\n {weapon['Location']}", bg=bg_color, font=("Arial", 10), width=20, height=3)
        label.pack(side=LEFT)

    # Добавление типа оружия
    def add_weapon_type(self, check_results, weapon, frame):
        bg_color = TriesFrame.WRONG
        if check_results[3]:
            bg_color = TriesFrame.RIGHT
        label = Label(frame, text=weapon['Type'], background=bg_color, width=20, height=3)
        label.pack(side=LEFT)

    # Добавление шанса выпадения оружия
    def add_weapon_drop_chance(self, check_results, weapon, frame):
        text = str(weapon['Drop_chance'])
        if check_results[-1] == 1:
            text = text + '↓'
        elif check_results[-1] == -1:
            text = text + '↑'
        bg_color = TriesFrame.WRONG
        if check_results[-1] == 0:
            bg_color = TriesFrame.RIGHT
        label = Label(frame, text=f"Drop chance:\n {text}", background=bg_color, width=20, height=3)
        label.pack(side=LEFT)
