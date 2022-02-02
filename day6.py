#https://reeborg.ca/ MAZE COMPLETED
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() == 0:
    while wall_on_right() == 1:
        if wall_in_front() == 1:
            turn_left()
            if wall_in_front() == 1:
                turn_left()
        move()
    while front_is_clear() == 1:
        move()
        if right_is_clear() == 1:
            turn_left()
            if wall_in_front() == 1:
                turn_around()
            else:
                turn_right()

    if wall_in_front() == 1 and right_is_clear() == 1:
        turn_right()