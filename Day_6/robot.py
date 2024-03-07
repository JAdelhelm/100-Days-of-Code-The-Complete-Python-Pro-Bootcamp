while at_goal() == False:
    while front_is_clear() and at_goal() == False:
        move()
        if right_is_clear() and not front_is_clear() and at_goal() == False:
            turn_left()
            turn_left()
            turn_left()
    if wall_in_front() and at_goal() == False:
        turn_left()

           
  
