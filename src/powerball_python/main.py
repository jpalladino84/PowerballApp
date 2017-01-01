"""
Powerball app
=============

Usage:
------

PowerballApp().run()

Example output:
---------------

Welcome to Powerball!

Enter your first name: Jeff
Enter your last name: Palladino

Select 1st #: 1
Select 2nd number (1 thru 69 excluding 1): 2
Select 3rd number (1 thru 69 excluding 1, 2): 3
Select 4th number (1 thru 69 excluding 1, 2, 3): 4
Select 5th number (1 thru 69 excluding 1, 2, 3, 4): 5
Select Power Ball # (1 thru 26): 1

Would you like to add another entrant? (y/n): n

Jeff Palladino 1, 2, 3, 4, 5 Powerball: 1

Powerball winning numbers:

    4, 2, 5, 6, 8 Powerball 1

"""

from collections import Counter

from powerball_python import constants
from powerball_python.models import PowerBallEntrant, InvalidChoiceException


class PowerBallApp:
    """

    """
    entrants = []

    @staticmethod
    def get_first_name():
        """Get entrant first name"""
        first_name = input(constants.FIRST_NAME_MSG)
        while not first_name:
            # validate input
            # TODO (palladino): validate against wildcards.
            print(constants.INVALID_NAME_MSG)
            first_name = input(constants.FIRST_NAME_MSG)

        return first_name

    @staticmethod
    def get_last_name():
        """Get entrant last name"""
        last_name = input(constants.LAST_NAME_MSG)
        while not last_name:
            # validate input
            # TODO (palladino): validate against wildcards.
            print(constants.INVALID_NAME_MSG)
            last_name = input(constants.LAST_NAME_MSG)

        return last_name

    @staticmethod
    def set_favorite_numbers(entrant):
        """Set entrants favorite numbers"""
        i = 0
        while i < 5:
            try:
                number = input(constants.CHOICE_MESSAGES[i].format(", ".join(entrant.favorite_numbers)))
                entrant.set_favorite_number(number)
            except InvalidChoiceException as e:
                print(e)
            except ValueError:
                print(constants.INVALID_TYPE_MSG)
            else:
                i += 1

    @staticmethod
    def set_powerball_number(entrant):
        """Set entrants powerball number"""
        while True:
            try:
                number = input(constants.POWERBALL_MSG)
                entrant.set_powerball(number)
                break
            except InvalidChoiceException as e:
                print(e)
            except ValueError:
                print(constants.INVALID_TYPE_MSG)

    def print_winning_numbers(self):
        favorite_numbers = []  # favorite numbers of all entrants
        powerball_numbers = []  # powerball number of all entrants
        for entrant in self.entrants:
            favorite_numbers += entrant.favorite_numbers
            powerball_numbers.append(entrant.powerball_number)

            # list entrant's favorite numbers and powerball selections
            print(constants.ENTRANT_SELECTION_MSG.format(
                first_name=entrant.first_name,
                last_name=entrant.last_name,
                favorite_numbers=", ".join(entrant.favorite_numbers),
                powerball=entrant.powerball_number
            ))

        # Winning numbers are figured out based on count of each
        # entrant's favorite numbers provided
        print(constants.WINNING_NUMBER_MSG.format(
            winning_numbers=", ".join([x for x, y in Counter(favorite_numbers).most_common(5)]),
            powerball=", ".join([x for x, y in Counter(powerball_numbers).most_common(1)])
        ))

    def run(self):
        """
        1) Add entrants
        2) print winning numbers
        """
        print(constants.APP_START_MSG)
        while True:
            first_name = self.get_first_name()
            last_name = self.get_last_name()
            entrant = PowerBallEntrant(first_name, last_name)

            self.set_favorite_numbers(entrant)
            self.set_powerball_number(entrant)

            self.entrants.append(entrant)

            result = input(constants.ADD_ENTRANT_MSG)
            if result in constants.ACCEPTABLE_NO_INPUTS:
                break

        self.print_winning_numbers()

if __name__ == "__main__":
    PowerBallApp().run()
