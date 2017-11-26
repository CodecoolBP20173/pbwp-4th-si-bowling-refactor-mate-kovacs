def score(game):
    """Calculates the score of a player in a 10 round bowling game from a list of characters, that \
    represent each roll.\n
    Argument: game - a string (list of characters) where digits represent the number of knocked pins, \
    "/" represents a spare, "X" or "x" represent a strike and "-" represents a miss.\n
    Return: an integer number of the total score that the series of rolls worth.\n
    Logic of the calculation:\n
    For every roll the point value of the current roll is added to the score. Then if spare or strike \
    happened, the program makes the necessary corrections. Except for the last frame, because of the \
    extra rolls, that are handled by simple rolls and their value is just added to the score (see \
    before). Important to note that this could be a major design flaw in the program, since this \
    logic does not stricktly follow the way to calculate the score in a bowling game, but the two \
    results merely coincide."""
    GAME_LENGTH = 10
    result = 0
    frame = 1
    first_roll_in_frame = True
    for current_roll in range(len(game)):
        result += get_value(game[current_roll])
        if is_spare(game[current_roll]) or is_strike(game[current_roll]):
            result += correction_for_spare_and_strike(frame, game, current_roll, GAME_LENGTH)
        if not first_roll_in_frame or is_strike(game[current_roll]):
            frame += 1
            first_roll_in_frame = True
        else:
            first_roll_in_frame = False
    return result


def correction_for_spare_and_strike(frame, game, current_roll, game_length):
    correction = 0
    if not extra_roll(game_length, frame):
        if is_spare(game[current_roll]):
            correction += spare_correction(game, current_roll)
        elif is_strike(game[current_roll]):
            correction += strike_correction(game, current_roll)
    return correction


def strike_correction(game, current_roll):
    partial_correction = get_value(game[current_roll + 1])
    if is_spare(game[current_roll + 2]):
        partial_correction += get_value(game[current_roll]) - get_value(game[current_roll + 1])
    else:
        partial_correction += get_value(game[current_roll + 2])
    return partial_correction


def spare_correction(game, current_roll):
    return get_value(game[current_roll + 1]) - get_value(game[current_roll - 1])


def get_value(roll_value):
    if is_normal_hit(roll_value):
        return int(roll_value)
    elif is_strike(roll_value) or is_spare(roll_value):
        return 10
    elif is_miss(roll_value):
        return 0
    else:
        raise ValueError()


def is_normal_hit(roll_value_sign):
    if roll_value_sign.isdigit():
        return True
    else:
        return False


def is_spare(roll_value_sign):
    if roll_value_sign == '/':
        return True
    else:
        return False


def is_strike(roll_value_sign):
    if roll_value_sign.lower() == 'x':
        return True
    else:
        return False


def is_miss(roll_value_sign):
    if roll_value_sign == '-':
        return True
    else:
        return False


def extra_roll(game_length, frame):
    if game_length <= frame:
        return True
    else:
        return False
