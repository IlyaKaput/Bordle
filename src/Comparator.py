class Comparator:
    """
    Class that contains all methods to compare two weapons
    """
    @staticmethod
    def get_integer_value_of_rarity(rarity):
        """
        Giving an integer value to every rarity in Borderlands 2

        :param rarity: rarity naming
        :return: integer, corresponding to that rarity
        """
        if rarity == 'common':
            return 0
        elif rarity == 'uncommon':
            return 1
        elif rarity == 'rare':
            return 2
        elif rarity == 'epic':
            return 3
        elif rarity == 'e-tech':
            return 4
        elif rarity == 'legendary':
            return 5
        elif rarity == 'seraph':
            return 6
        elif rarity == 'pearlescent':
            return 7
        return 8

    @staticmethod
    def compare_rarity(rarity1, rarity2):
        """
        Comparing rarities of weapons

        :param rarity1: rarity of weapon being checked
        :param rarity2: rarity of chosen weapon
        :return: -1 if rarity is lower than needed, 0 if rarities match and 1 if checked rarity is higher
        """
        first_rarity_integer = Comparator.get_integer_value_of_rarity(str(rarity1).lower())
        second_rarity_integer = Comparator.get_integer_value_of_rarity(str(rarity2).lower())
        if first_rarity_integer > second_rarity_integer:
            return 1
        elif first_rarity_integer == second_rarity_integer:
            return 0
        return -1

    @staticmethod
    def compare_location(location1, dlc1, location2, dlc2):
        """
        comparing locations of weapons

        :param location1: location of drop for weapon being checked
        :param dlc1: dlc of drop for weapon being checked
        :param location2: location of drop for chosen weapon
        :param dlc2: dlc of drop for chosen weapon
        :return: 2 if locations match, 1 if dlcs match otherwise. 0 if not
        """
        if location1 == location2:
            return 2
        elif dlc1 == dlc2:
            return 1
        return 0

    @staticmethod
    def compare_boolean(type1, type2):
        """
        Comparing weapon properties that can only match or not
        If they cannot be ordered or be considered close

        :param type1: property of a weapon being checked
        :param type2: property of a chosen weapon
        :return: 1 if they match, 0 otherwise
        """
        if str(type1).lower() == str(type2).lower():
            return 1
        return 0

    @staticmethod
    def compare_numbers(number1, number2):
        """
        Compared two objects from ordered set that can be compared with ">"

        :param number1: number corresponding to weapon being checked
        :param number2: number corresponding ot chosen weapon
        :return: 1, 0 or -1 if number1 is larger, equal to or less than number2, respectively
        """
        if number1 > number2:
            return 1
        elif number2 == number1:
            return 0
        return -1

    @staticmethod
    def compare_weapons(weapon1, weapon2):
        """
        Comparing two weapons entirely

        :param weapon1: first weapon as a line from csv
        :param weapon2: second weapon as a line from csv
        :return: list of integers containing result of comparing names, rarities, locations, types and drop chances in that order
        """
        result_of_comparing_names = Comparator.compare_boolean(weapon1['Name'], weapon2['Name'])
        result_of_comparing_rarities = Comparator.compare_rarity(weapon1['Rarity'], weapon2['Rarity'])
        result_of_comparing_locations = Comparator.compare_location(weapon1['Location'], weapon1['Add_on'],
                                                                    weapon2['Location'], weapon2['Add_on'])
        result_of_comparing_types = Comparator.compare_boolean(weapon1['Type'], weapon2['Type'])
        result_of_comparing_drop_chances = Comparator.compare_numbers(float(weapon1['Drop_chance']),
                                                                      float(weapon2['Drop_chance']))
        result_of_comparing_manufacturers = Comparator.compare_boolean(weapon1['Manufacturer'], weapon2['Manufacturer'])
        return [result_of_comparing_names, result_of_comparing_rarities, result_of_comparing_locations,
                result_of_comparing_types, result_of_comparing_drop_chances, result_of_comparing_manufacturers]
