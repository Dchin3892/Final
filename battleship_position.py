def battleship_position(map):
    import random
    ai_battleship = {'health': 4, 'position': []}
    ai_battleship['position'].append(random.choice(map))
    battle_x = ai_battleship['position'][0][0]
    battle_y = ai_battleship['position'][0][1]

    if (battle_x < 4) & (battle_y < 4):
        directions = [1,2]
        direction = random.choice(directions)# 2,3

    elif (battle_x < 4) & (battle_y in [4,5]):
        directions = [1,2,3]
        direction = random.choice(directions)# 1,2,3

    elif (battle_x < 4) & (battle_y > 5):
        directions = [2,3]
        direction = random.choice(directions)# 1,2

    elif (battle_x in [4,5]) & (battle_y < 4):
        directions = [1,2,4]
        direction = random.choice(directions)# 2,3,4

    elif (battle_x in [4,5]) & (battle_y in [4,5]):
        directions = [1,2,3,4]
        direction = random.choice(directions)

    elif (battle_x in [4,5]) & (battle_y > 5):
        directions = [2,3,4]
        direction = random.choice(directions)# 1,2,4

    elif (battle_x > 5) & (battle_y < 4):
        directions = [1,4]
        direction = random.choice(directions)# 3,4

    elif (battle_x > 5) & (battle_y in [4,5]):
        directions = [1,3,4]
        direction = random.choice(directions)# 1,3,4

    elif (battle_x > 5) & (battle_y > 5):
        directions = [3,4]
        direction = random.choice(directions)# 1,4

    # Setting the end point in chosen direction
    if direction == 1:
        for n in range(1,4):
            new_y = battle_y + n
            new_position = (battle_x, new_y)
            ai_battleship['position'].append(new_position)

    if direction == 2:
        for n in range(1,4):
            new_x = battle_x + n
            new_position = (new_x, battle_y)
            ai_battleship['position'].append(new_position)

    if direction == 3:
        for n in range(1,4):
            new_y = battle_y - n
            new_position = (battle_x, new_y)
            ai_battleship['position'].append(new_position)

    if direction == 4:
        for n in range(1,4):
            new_x = battle_x - n
            new_position = (new_x, battle_y)
            ai_battleship['position'].append(new_position)
    return ai_battleship