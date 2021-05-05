def destroyer_position(map):
    import random
    ai_destroyer = {'health': 3, 'position': []}
    ai_destroyer['position'].append(random.choice(map))
    dest_x = ai_destroyer['position'][0][0]
    dest_y = ai_destroyer['position'][0][1]

    if (dest_x < 3) & (dest_y < 3):
        directions = [1,2]
        direction = random.choice(directions)# 2,3

    elif (dest_x < 3) & (dest_y in [3,4,5,6]):
        directions = [1,2,3]
        direction = random.choice(directions)# 1,2,3

    elif (dest_x < 3) & (dest_y > 6):
        directions = [2,3]
        direction = random.choice(directions)# 1,2

    elif (dest_x in [3,4,5,6]) & (dest_y < 3):
        directions = [1,2,4]
        direction = random.choice(directions)# 2,3,4

    elif (dest_x in [3,4,5,6]) & (dest_y in [3,4,5,6]):
        directions = [1,2,3,4]
        direction = random.choice(directions)

    elif (dest_x in [3,4,5,6]) & (dest_y > 6):
        directions = [2,3,4]
        direction = random.choice(directions)# 1,2,4

    elif (dest_x > 6) & (dest_y < 3):
        directions = [1,4]
        direction = random.choice(directions)# 3,4

    elif (dest_x > 6) & (dest_y in [3,4,5,6]):
        directions = [1,3,4]
        direction = random.choice(directions)# 1,3,4

    elif (dest_x > 6) & (dest_y > 6):
        directions = [3,4]
        direction = random.choice(directions)# 1,4

    # Setting the end point in chosen direction
    if direction == 1:
        for n in range(1,3):
            new_y = dest_y + n
            new_position = (dest_x, new_y)
            ai_destroyer['position'].append(new_position)

    if direction == 2:
        for n in range(1,3):
            new_x = dest_x + n
            new_position = (new_x, dest_y)
            ai_destroyer['position'].append(new_position)

    if direction == 3:
        for n in range(1,3):
            new_y = dest_y - n
            new_position = (dest_x, new_y)
            ai_destroyer['position'].append(new_position)

    if direction == 4:
        for n in range(1,3):
            new_x = dest_x - n
            new_position = (new_x, dest_y)
            ai_destroyer['position'].append(new_position)
    return ai_destroyer