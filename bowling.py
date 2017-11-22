def score(game):
    result = 0
    frame = 1
    first_roll_in_round = True
    for current_roll in range(len(game)):
        result += get_value(game[current_roll])
        if frame < 10 and get_value(game[current_roll]) == 10:
            if game[current_roll] == '/':
                result += get_value(game[current_roll + 1]) - get_value(game[current_roll-1])
            elif game[current_roll] == 'X' or game[current_roll] == 'x':
                result += get_value(game[current_roll + 1])
                if game[current_roll + 2] == '/':
                    result += 10 - get_value(game[current_roll + 1])
                else:
                    result += get_value(game[current_roll + 2])
            
        if first_roll_in_round is True:
            first_roll_in_round = False
        else:
            frame += 1
            first_roll_in_round = True
        if game[current_roll] == 'X' or game[current_roll] == 'x':
            first_roll_in_round = True
            frame += 1
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
