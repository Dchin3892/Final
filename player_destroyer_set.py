def player_destroyer_set(first_x, first_y):
    player_destroyer = {'health': 3, 'position': [], 'hits': 0, 'destroyed': False, 'type': 'Destroyer'}
    player_destroyer['position'].append(f'({first_x}, {first_y})')

    print('Chose a direction. N, S, E, W.')
    p_dest_direction = input()

    if p_dest_direction.lower() == 'n':
        for n in range(1,3):
            new_y = int(first_y) + n
            new_position = f'({first_x}, {new_y})'
            player_destroyer['position'].append(new_position)
        print('North')

    if p_dest_direction.lower() == 'e':
        for n in range(1,3):
            new_x = int(first_x) + n
            new_position = f'({new_x}, {first_y})'
            player_destroyer['position'].append(new_position)
        print('East')

    if p_dest_direction.lower() == 's':
        for n in range(1,3):
            new_y = int(first_y) - n
            new_position = f'({first_x}, {new_y})'
            player_destroyer['position'].append(new_position)
        print('South')

    if p_dest_direction.lower() == 'w':
        for n in range(1,3):
            new_x = int(first_x) - n
            new_position = f'({new_x}, {first_y})'
            player_destroyer['position'].append(new_position)
        print('West')
    return player_destroyer