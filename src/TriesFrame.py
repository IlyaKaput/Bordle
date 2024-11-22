from tkinter import Frame, Label, Scrollbar
from tkinter.constants import BOTTOM, SOLID, LEFT, RIGHT, Y
from PIL import Image, ImageTk


class TriesFrame(Frame):
    """Frame with methods to work with weapon visualisation easier"""
    WRONG = "#FF6666" #color of wrong answer
    RIGHT = "#66FF66" #color of right answer
    SEMI_RIGHT = "#FFFF66" #color of answer that is close to right
    def __init__(self,master, height=0, width=0):
        super().__init__(master, height=height, width=width)
        self.scrollbar = None
        self.frames = list()
        self.game_is_over = False

    @staticmethod
    def resize(image):
        """
        resizing image for correct display

        :param image: image needed to be changed
        :return: image with correct size
        """
        width, height = image.size
        if width >= height * 4:
            return image.resize((200, int(height * 200 / width)))
        else:
            return image.resize((int(width * 50 / height), 50))

    def add_weapon_try(self, check_results, weapon):
        """
        Display of all information of weapon being checked

        :param check_results: results of checking a weapon
        :param weapon: weapon information
        :return: nothing
        """
        #frame to display weapon info
        frame = Frame(self, width=1200, height=50, borderwidth=2, relief=SOLID)
        #consequent calls of Visualisation methods
        self.add_weapon_picture(weapon, frame)
        self.add_weapon_name(check_results, weapon, frame)
        self.add_weapon_rarity(check_results, weapon, frame)
        self.add_weapon_manufacturer(check_results, weapon, frame)
        self.add_weapon_location(check_results, weapon, frame)
        self.add_weapon_type(check_results, weapon, frame)
        self.add_weapon_drop_chance(check_results, weapon, frame)
        frame.pack(side=BOTTOM)
        self.check_game_over(check_results)
        self.update_idletasks()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def add_weapon_picture(self, weapon, frame):
        """

        Displaying weapon picture

        :param weapon: weapon information
        :param frame: frame to be used for displaying
        """
        img = Image.open('../assets/pictures/' + '_'.join(weapon['Name'].lower().split()) + '.png')
        img = TriesFrame.resize(img)
        image = ImageTk.PhotoImage(img)
        label = Label(frame, width=200, height=50, image=image)
        label.photo = image
        label.pack(side=LEFT)

    # Добавление имени оружия
    def add_weapon_name(self, check_results, weapon, frame):
        """
        Displaying weapon name

        :param check_results: results of checking a weapon
        :param weapon: weapon information
        :param frame: frame to be displayed
        :return: nothing
        """
        bg_color = TriesFrame.WRONG
        if check_results[0]:
            bg_color = TriesFrame.RIGHT
        label = Label(frame, text=weapon['Name'], bg=bg_color, font=("Arial", 10), width=20, height=3)
        label.pack(side=LEFT)

    # Добавление редкости оружия на экран
    def add_weapon_rarity(self, check_results, weapon, frame):
        """
        Displaying weapon rarity and "↓" or "↑" if weapon is more or less rare than needed respectively

        :param check_results: results of checking a weapon
        :param weapon: weapon information
        :param frame: frame to be displayed
        :return: nothing
        """
        text = weapon['Rarity']
        if check_results[1] == 1:
            text += '↓'
        elif check_results[1] == -1:
            text += '↑'
        bg_color = TriesFrame.WRONG
        if check_results[1] == 0:
            bg_color = TriesFrame.RIGHT
        label = Label(frame, text=f"Rarity:\n {text}", bg=bg_color, font=("Arial", 10), width=20, height=3)
        label.pack(side=LEFT)

    # Добавление редкости оружия
    def add_weapon_location(self, check_results, weapon, frame):
        """
        Displaying weapon location in red if it is not close to right one or in yellow if it can be reached from it

        :param check_results: results of checking a weapon
        :param weapon: weapon information
        :param frame: frame to be displayed
        :return: nothing
        """
        bg_color = TriesFrame.WRONG
        if check_results[2] == 2:
            bg_color = TriesFrame.RIGHT
        elif check_results[2] == 1:
            bg_color = TriesFrame.SEMI_RIGHT
        label = Label(frame, text=f"Location:\n {weapon['Location']}", bg=bg_color, font=("Arial", 10), width=20,
                      height=3)
        label.pack(side=LEFT)

    # Добавление типа оружия
    def add_weapon_type(self, check_results, weapon, frame):
        """
        Displaying weapon type in red if it does not match with right one or in green if it is

        :param check_results: results of checking a weapon
        :param weapon: weapon information
        :param frame: frame to be displayed
        :return: nothing
        """
        bg_color = TriesFrame.WRONG
        if check_results[3]:
            bg_color = TriesFrame.RIGHT
        label = Label(frame, text=weapon['Type'], background=bg_color, width=20, height=3)
        label.pack(side=LEFT)

    # Добавление шанса выпадения оружия
    def add_weapon_drop_chance(self, check_results, weapon, frame):
        """
        Displaying weapon rarity and "↓" or "↑" if weapon drops more or less frequently than needed, respectively

        :param check_results: results of checking a weapon
        :param weapon: weapon information
        :param frame: frame to be displayed
        :return: nothing
        """
        text = str(weapon['Drop_chance'])
        if check_results[4] == 1:
            text = text + '↓'
        elif check_results[4] == -1:
            text = text + '↑'
        bg_color = TriesFrame.WRONG
        if check_results[4] == 0:
            bg_color = TriesFrame.RIGHT
        label = Label(frame, text=f"Drop chance:\n {text}", background=bg_color, width=20, height=3)
        label.pack(side=LEFT)

    def add_weapon_manufacturer(self, check_results, weapon, frame):
        """
                Displaying weapon manufacturer in red if it does not match with right one or in green if it is

                :param check_results: results of checking a weapon
                :param weapon: weapon information
                :param frame: frame to be displayed
                :return: nothing
                """
        bg_color = TriesFrame.WRONG
        if check_results[5]:
            bg_color = TriesFrame.RIGHT
        label = Label(frame, text=weapon['Manufacturer'], background=bg_color, width=20, height=3)
        label.pack(side=LEFT)

    def check_game_over(self, test_results):
        if test_results[0]:
            self.game_over()

    def game_over(self):
        self.game_is_over = True
        frame = Frame(self, width=1200, height=50, borderwidth=2, relief=SOLID)
        label = Label(frame, text="You WIN!!!", bg=TriesFrame.RIGHT, font=("Arial", 10), width=20, height=3)
        label.pack(fill='both')
        frame.pack(side=BOTTOM)



