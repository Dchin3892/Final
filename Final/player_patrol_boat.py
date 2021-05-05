def player_patrol_boat_set(first_x, first_y):
    player_patrol_boat = {'health': 2, 'position': [], 'hits': 0, 'destroyed': False, 'type': 'Patrol Boat'}
    player_patrol_boat['position'].append(f'({first_x}, {first_y})')

    print('Chose a direction. N, S, E, W.')
    p_patrol_direction = input()

    if p_patrol_direction.lower() == 'n':
        for n in range(1,2):
            new_y = int(first_y) + n
            new_position = f'({first_x}, {new_y})'
            player_patrol_boat['position'].append(new_position)
        print('North')

    if p_patrol_direction.lower() == 'e':
        for n in range(1,2):
            new_x = int(first_x) + n
            new_position = f'({new_x}, {first_y})'
            player_patrol_boat['position'].append(new_position)
        print('East')

    if p_patrol_direction.lower() == 's':
        for n in range(1,2):
            new_y = int(first_y) - n
            new_position = f'({first_x}, {new_y})'
            player_patrol_boat['position'].append(new_position)
        print('South')

    if p_patrol_direction.lower() == 'w':
        for n in range(1,2):
            new_x = int(first_x) - n
            new_position = f'({new_x}, {first_y})'
            player_patrol_boat['position'].append(new_position)
        print('West')
    return player_patrol_boat