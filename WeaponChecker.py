import pandas as pd
from random import randint
from Comparator import Comparator

class WeaponChecker:
    chosen_weapon = None
    weapon_info = pd.read_csv('WeaponInfo.csv', sep=';')

    @staticmethod
    def set_weapon(weapon):
        WeaponChecker.chosen_weapon = weapon
        print(weapon['Name'])

    @staticmethod
    def choose_random_weapon():
        weapon_index = randint(0, round(WeaponChecker.weapon_info.size/WeaponChecker.weapon_info.iloc[0].size))
        WeaponChecker.set_weapon(WeaponChecker.weapon_info.iloc[weapon_index])

    @staticmethod
    def check_weapon_with_given_weapon(weapon):
        return Comparator.compare_weapons(weapon, WeaponChecker.chosen_weapon)

    @staticmethod
    def find_weapon_index(weapon_name):
        for i in range(round(WeaponChecker.weapon_info.size/WeaponChecker.weapon_info.iloc[0].size)):
            if Comparator.compare_boolean(WeaponChecker.weapon_info.iloc[i]['Name'], weapon_name):
                return i
        return -1

    @staticmethod
    def check_weapon(weapon_name):
        weapon_index = WeaponChecker.find_weapon_index(weapon_name)
        if weapon_index == -1:
            return -1
        return WeaponChecker.check_weapon_with_given_weapon(WeaponChecker.weapon_info.iloc[weapon_index])

    @staticmethod
    def get_file_name(weapon_name):
        return "pictures/"+'_'.join(weapon_name.lower().split()) + '.png'

    @staticmethod
    def get_weapon(weapon_name):
        return WeaponChecker.weapon_info.iloc[WeaponChecker.find_weapon_index(weapon_name)]