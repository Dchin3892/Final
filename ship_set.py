class ship_set:

    def player_battleship_set(self):
        print('Choose a starting point for your Battleship. It is 4 squares long')
        print('First the X cooirdinate')
        self.first_x = input()
        print('Next the Y cooirdinate')
        self.first_y = input()
        print('Chose a direction. N, S, E, W.')
        self.p_battle_direction = input()

        self.player_battleship = {'health': 4, 'position': [], 'hits': 0, 'destroyed': False, 'type': 'Battleship'}
        self.player_battleship['position'].append(f'({self.first_x}, {self.first_y})')

        if self.p_battle_direction.lower() == 'n':
            for n in range(1,4):
                self.new_y = int(self.first_y) + n
                self.new_position = f'({self.first_x}, {self.new_y})'
                self.player_battleship['position'].append(self.new_position)

        if self.p_battle_direction.lower() == 'e':
            for n in range(1,4):
                self.new_x = int(self.first_x) + n
                self.new_position = f'({self.new_x}, {self.first_y})'
                self.player_battleship['position'].append(self.new_position)

        if self.p_battle_direction.lower() == 's':
            for n in range(1,4):
                self.new_y = int(self.first_y) - n
                self.new_position = f'({self.first_x}, {self.new_y})'
                self.player_battleship['position'].append(self.new_position)

        if self.p_battle_direction.lower() == 'w':
            for n in range(1,4):
                self.new_x = int(self.first_x) - n
                self.new_position = f'({self.new_x}, {self.first_y})'
                self.player_battleship['position'].append(self.new_position)

        return self.player_battleship

    def player_destroyer_set(self):
        print('Choose a starting point for your Destroyer. It is 3 squares long')
        print('First the X cooirdinate')
        self.first_x = input()
        print('Next the Y cooirdinate')
        self.first_y = input()
        print('Chose a direction. N, S, E, W.')
        self.p_dest_direction = input()

        self.player_destroyer = {'health': 3, 'position': [], 'hits': 0, 'destroyed': False, 'type': 'Destroyer'}
        self.player_destroyer['position'].append(f'({self.first_x}, {self.first_y})')

        if self.p_dest_direction.lower() == 'n':
            for n in range(1,3):
                self.new_y = int(self.first_y) + n
                self.new_position = f'({self.first_x}, {self.new_y})'
                self.player_destroyer['position'].append(self.new_position)

        if self.p_dest_direction.lower() == 'e':
            for n in range(1,3):
                self.new_x = int(self.first_x) + n
                self.new_position = f'({self.new_x}, {self.first_y})'
                self.player_destroyer['position'].append(self.new_position)

        if self.p_dest_direction.lower() == 's':
            for n in range(1,3):
                self.new_y = int(self.first_y) - n
                self.new_position = f'({self.first_x}, {self.new_y})'
                self.player_destroyer['position'].append(self.new_position)

        if self.p_dest_direction.lower() == 'w':
            for n in range(1,3):
                self.new_x = int(self.first_x) - n
                self.new_position = f'({self.new_x}, {self.first_y})'
                self.player_destroyer['position'].append(self.new_position)

        return self.player_destroyer

    def player_patrol_boat_set(self):
        print('Choose a starting point for your Patrol Boat. It is 2 squares long')
        print('First the X cooirdinate')
        self.first_x = input()
        print('Next the Y cooirdinate')
        self.first_y = input()
        print('Chose a direction. N, S, E, W.')
        self.p_patrol_direction = input()

        self.player_patrol_boat = {'health': 2, 'position': [], 'hits': 0, 'destroyed': False, 'type': 'Patrol Boat'}
        self.player_patrol_boat['position'].append(f'({self.first_x}, {self.first_y})')

        if self.p_patrol_direction.lower() == 'n':
            for n in range(1,2):
                self.new_y = int(self.first_y) + n
                self.new_position = f'({self.first_x}, {self.new_y})'
                self.player_patrol_boat['position'].append(self.new_position)
            print('North')

        if self.p_patrol_direction.lower() == 'e':
            for n in range(1,2):
                self.new_x = int(self.first_x) + n
                self.new_position = f'({self.new_x}, {self.first_y})'
                self.player_patrol_boat['position'].append(self.new_position)
            print('East')

        if self.p_patrol_direction.lower() == 's':
            for n in range(1,2):
                self.new_y = int(self.first_y) - n
                self.new_position = f'({self.first_x}, {self.new_y})'
                self.player_patrol_boat['position'].append(self.new_position)
            print('South')

        if self.p_patrol_direction.lower() == 'w':
            for n in range(1,2):
                self.new_x = int(self.first_x) - n
                self.new_position = f'({self.new_x}, {self.first_y})'
                self.player_patrol_boat['position'].append(self.new_position)
            print('West')
            
        return self.player_patrol_boat