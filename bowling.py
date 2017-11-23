def score(game):
    MAX_FRAME = 10
    result = 0
    frame = 1
    first_roll_in_round = True
    for current_roll in range(len(game)):
        result += get_value(game[current_roll])
        result = multi_roll_corrections(frame, game, current_roll, result, MAX_FRAME)

        if first_roll_in_round:
            first_roll_in_round = False
        else:
            frame += 1
            first_roll_in_round = True
        if is_strike(game[current_roll]):
            first_roll_in_round = True
            frame += 1
    return result


def multi_roll_corrections(frame, game, current_roll, result, game_length):
    if frame < game_length and get_value(game[current_roll]) == 10:
        if game[current_roll] == '/':
            result += get_value(game[current_roll + 1]) - get_value(game[current_roll - 1])
        elif is_strike(game[current_roll]):
            result += get_value(game[current_roll + 1])
            if game[current_roll + 2] == '/':
                result += get_value(game[current_roll]) - get_value(game[current_roll + 1])
            else:
                result += get_value(game[current_roll + 2])
    return result


def get_value(roll_value):
    if roll_value == '1' or roll_value == '2' or roll_value == '3' or \
       roll_value == '4' or roll_value == '5' or roll_value == '6' or \
       roll_value == '7' or roll_value == '8' or roll_value == '9':
        return int(roll_value)
    elif is_strike(roll_value):
        return 10
    elif roll_value == '/':
        return 10
    elif roll_value == '-':
        return 0
    else:
        raise ValueError()


def is_strike(roll_value_sign):
    if roll_value_sign.lower() == 'x':
        return True
    else:
        return False
