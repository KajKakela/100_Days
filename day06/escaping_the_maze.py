#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if is_facing_north():
    while front_is_clear():
        move()
else:
    while not is_facing_north():
        turn_left()
        while front_is_clear():
            move()
turn_left()

while not at_goal():
    if not right_is_clear():
    
        if front_is_clear():
            move()
        else:
            turn_left()
    
    elif right_is_clear():
        turn_right()
        move()