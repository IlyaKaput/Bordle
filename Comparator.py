class Comparator:
    @staticmethod
    def get_integer_value_of_rarity(rarity):
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
        first_rarity_integer = Comparator.get_integer_value_of_rarity(str(rarity1).lower())
        second_rarity_integer = Comparator.get_integer_value_of_rarity(str(rarity2).lower())
        if first_rarity_integer > second_rarity_integer:
            return 1
        elif first_rarity_integer == second_rarity_integer:
            return 0
        return -1

    @staticmethod
    def compare_location(location1, dlc1, location2, dlc2):
        if location1 == location2:
            return 2
        elif dlc1 == dlc2:
            return 1
        return 0

    @staticmethod
    def compare_boolean(type1, type2):
        if str(type1).lower() == str(type2).lower():
            return 1
        return 0

    @staticmethod
    def compare_numbers(number1, number2):
        if number1 > number2:
            return 1
        elif number2 == number1:
            return 0
        return -1

    @staticmethod
    def compare_weapons(weapon1, weapon2):
        result_of_comparing_names = Comparator.compare_boolean(weapon1['Name'], weapon2['Name'])
        result_of_comparing_rarities = Comparator.compare_rarity(weapon1['Rarity'], weapon2['Rarity'])
        result_of_compating_locations = Comparator.compare_location(weapon1['Location'], weapon1['Add_on'],
                                                                    weapon2['Location'], weapon2['Add_on'])
        result_of_comparing_types = Comparator.compare_boolean(weapon1['Type'], weapon2['Type'])
        result_of_comparing_drop_chances = Comparator.compare_numbers(float(weapon1['Drop_chance']),
                                                                      float(weapon2['Drop_chance']))
        return [result_of_comparing_names, result_of_comparing_rarities, result_of_compating_locations,
                result_of_comparing_types, result_of_comparing_drop_chances]
