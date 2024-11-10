import pandas as pd
from random import randint

from src.Comparator import Comparator


class WeaponChecker:
    """
    Class that checks if weapon is the same as one being chosen for a game
    If not it has access to all information that matched and that did not
    """
    chosen_weapon = None
    weapon_info = pd.read_csv('../assets/WeaponInfo.csv', sep=';')

    @staticmethod
    def set_weapon(weapon):
        """
        Sets weapon chosen for a game

        :param weapon: all weapon info is contained in WeaponChecker.chosen_weapon
        """
        WeaponChecker.chosen_weapon = weapon

    @staticmethod
    def choose_random_weapon():
        """
        Choosing random weapon and setting it
        """
        weapon_index = randint(0, round(WeaponChecker.weapon_info.size / WeaponChecker.weapon_info.iloc[0].size))
        WeaponChecker.set_weapon(WeaponChecker.weapon_info.iloc[weapon_index])

    @staticmethod
    def check_weapon_with_given_weapon(weapon):
        """
        Fully checking what is same between given weapon and chosen one

        :param weapon: weapon comparing to chosen weapon
        :return: result of comparing weapons in a list of integers
        """
        return Comparator.compare_weapons(weapon, WeaponChecker.chosen_weapon)

    @staticmethod
    def find_weapon_index(weapon_name):
        """
        Finding weapon info according to name of a weapon

        :param weapon_name: string that is a weapon name regardless of register and/or switching spaces and underscores
        :return: index of weapon if it is in weapon_info or -1 if it isn't
        """
        for i in range(round(WeaponChecker.weapon_info.size / WeaponChecker.weapon_info.iloc[0].size)):
            if Comparator.compare_boolean(WeaponChecker.weapon_info.iloc[i]['Name'], weapon_name):
                return i
        return -1

    @staticmethod
    def check_weapon(weapon_name):
        """
        Fully checking what is same between given weapon and chosen one with having only name of a weapon

        :param weapon_name: name of a weapon needed to be checked
        :return: result of comparing weapons in a list of integers
        """
        weapon_index = WeaponChecker.find_weapon_index(weapon_name)
        if weapon_index == -1:
            return -1
        return WeaponChecker.check_weapon_with_given_weapon(WeaponChecker.weapon_info.iloc[weapon_index])

    @staticmethod
    def get_weapon(weapon_name):
        """
        Getting weapon with all the information needed for its name if it is in weapon_info

        :param weapon_name: name of a weapon for information gathering
        :return: weapon with all information needed to analyze it
        """
        return WeaponChecker.weapon_info.iloc[WeaponChecker.find_weapon_index(weapon_name)]
