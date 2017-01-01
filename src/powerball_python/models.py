from powerball_python import constants


class InvalidChoiceException(BaseException):

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return constants.INVALID_CHOICE_MSG.format(self.number)


class PowerBallEntrant:
    """
    Describes a individual that wants to play the powerball.
    """

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.number_pool = set(range(1, 70))
        self.powerball_pool = set(range(1, 27))
        self.favorite_numbers = []
        self.powerball_number = None

    def set_favorite_number(self, number):
        """
        Adds a number to the entrants favorite number pool
        :param number:
        """
        if int(number) not in self.number_pool:
            # validate the selected number is in the accepted pool
            raise InvalidChoiceException(number)

        self.favorite_numbers.append(number)
        self.number_pool.remove(int(number))

    def set_powerball(self, number):
        if int(number) not in self.powerball_pool:
            # validate the selected number is in the accepted pool
            raise InvalidChoiceException(number)

        self.powerball_number = number
