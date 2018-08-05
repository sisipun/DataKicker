from util.constant import PLAYERS_COUNT


def is_number(number):
    try:
        number = int(number)
    except ValueError:
        return False
    return 1 <= number <= PLAYERS_COUNT
