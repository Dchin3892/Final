def patrol_boat_position(map):
    import random
    ai_patrol_boat = {'health': 2, 'position': []}
    ai_patrol_boat['position'].append(random.choice(map))
    patrol_x = ai_patrol_boat['position'][0][0]
    patrol_y = ai_patrol_boat['position'][0][1]

    if (patrol_x < 2) & (patrol_y < 2):
        directions = [1,2]
        direction = random.choice(directions)# 2,3

    elif (patrol_x < 2) & (patrol_y in [2,3,4,5,6,7]):
        directions = [1,2,3]
        direction = random.choice(directions)# 1,2,3

    elif (patrol_x < 2) & (patrol_y > 7):
        directions = [2,3]
        direction = random.choice(directions)# 1,2

    elif (patrol_x in [2,3,4,5,6,7]) & (patrol_y < 2):
        directions = [1,2,4]
        direction = random.choice(directions)# 2,3,4

    elif (patrol_x in [2,3,4,5,6,7]) & (patrol_y in [2,3,4,5,6,7]):
        directions = [1,2,3,4]
        direction = random.choice(directions)

    elif (patrol_x in [2,3,4,5,6,7]) & (patrol_y > 7):
        directions = [2,3,4]
        direction = random.choice(directions)# 1,2,4

    elif (patrol_x > 7) & (patrol_y < 2):
        directions = [1,4]
        direction = random.choice(directions)# 3,4

    elif (patrol_x > 7) & (patrol_y in [2,3,4,5,6,7]):
        directions = [1,3,4]
        direction = random.choice(directions)# 1,3,4

    elif (patrol_x > 7) & (patrol_y > 7):
        directions = [3,4]
        direction = random.choice(directions)# 1,4

    # Setting the end point in chosen direction
    if direction == 1:
        for n in range(1,2):
            new_y = patrol_y + n
            new_position = (patrol_x, new_y)
            ai_patrol_boat['position'].append(new_position)

    if direction == 2:
        for n in range(1,2):
            new_x = patrol_x + n
            new_position = (new_x, patrol_y)
            ai_patrol_boat['position'].append(new_position)

    if direction == 3:
        for n in range(1,2):
            new_y = patrol_y - n
            new_position = (patrol_x, new_y)
            ai_patrol_boat['position'].append(new_position)

    if direction == 4:
        for n in range(1,2):
            new_x = patrol_x - n
            new_position = (new_x, patrol_y)
            ai_patrol_boat['position'].append(new_position)
    return ai_patrol_boat