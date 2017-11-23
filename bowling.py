def score(game):
    GAME_LENGTH = 10
    result = 0
    frame = 1
    first_roll_in_frame = True
    for current_roll in range(len(game)):
        result += get_value(game[current_roll])
        if is_spare(game[current_roll]) or is_strike(game[current_roll]):
            result += correction_for_spare_and_strike(frame, game, current_roll, GAME_LENGTH)

        if first_roll_in_frame:
            first_roll_in_frame = False
        else:
            frame += 1
            first_roll_in_frame = True
        if is_strike(game[current_roll]):
            first_roll_in_frame = True
            frame += 1
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
