import os
import time
import random

from battleship_position import battleship_position
from destroyer_position import destroyer_position
from patrol_boat_position import patrol_boat_position
from print_board import create_board
from print_board import print_board
from print_board import add_to_board
from print_board import add_to_board2
from coordinate_chart import coordinate_chart
from ship_set import ship_set

game_start = True

while game_start == True:
  # Printing board
  #create_board()
  board = create_board()
  print_board(board)

  previous_shots = []
  full_map = []
  turn = 0
  game_running = False
  current_target = ''
  hits = 0
  destroyer_ok = False
  patrol_boat_ok = False
  player_destroyed = 0
  ai_destroyed = 0


  # Creating the coordinates for the AI to chose from
  for x in range(8):
    for y in range(8):
      full_map.append((x+1, y+1))

  # Creating random positions for AI boats
  ai_battleship = battleship_position(full_map)

  ai_destroyer = destroyer_position(full_map)

  ai_patrol_boat = patrol_boat_position(full_map)

  # Player sets boat positions
  ships = ship_set()
  player_battleship = ships.player_battleship_set()
  for b in player_battleship['position']:
    add_to_board2(board, b, 'B')
  os.system('cls')
  print_board(board)

  player_destroyer = ships.player_destroyer_set()
  for b in player_destroyer['position']:
    add_to_board2(board, b, 'D')
  os.system('cls')
  print_board(board)

  player_patrol_boat = ships.player_patrol_boat_set()
  for b in player_patrol_boat['position']:
    add_to_board2(board, b, 'P')
  os.system('cls')
  print_board(board)

  # For testing/presentation
  print(ai_battleship['position'])
  print(ai_destroyer['position'])
  print(ai_patrol_boat['position'])

  game_running = True

  # Game loop
  while game_running == True:
    
    # Player turn
    while turn == 0:

      print('Place your shots')
      print('Chose a X cooridinates')
      shot_x = input()
      print('Chose a Y cooridinates')
      shot_y = input()
      target = f'({shot_x}, {shot_y})'
      previous_shots.append(target)
      hit = False

      for h in ai_battleship['position']:
        if target == str(h):
            ai_battleship['health'] = ai_battleship['health'] - 1
            hit = True
            os.system('cls')
            add_to_board(board, target, 'X')
            print_board(board)
            print(target)
            print('HIT!')
            if ai_battleship['health'] == 0:
                player_destroyed += 1
                print('Battleship Destroyed!')
            turn = 1
            break

      for h in ai_destroyer['position']:
        if target == str(h):
            ai_destroyer['health'] = ai_destroyer['health'] - 1
            hit = True
            os.system('cls')
            add_to_board(board, target, 'X')
            print_board(board)
            print(target)
            print('HIT!')
            if ai_destroyer['health'] == 0:
                player_destroyed += 1
                print('Destroyer Destroyed!')
            turn = 1
            break
      
      for h in ai_patrol_boat['position']:
        if target == str(h):
            ai_patrol_boat['health'] = ai_patrol_boat['health'] - 1
            hit = True
            os.system('cls')
            add_to_board(board, target, 'X')
            print_board(board)
            print(target)
            print('HIT!')
            if ai_patrol_boat['health'] == 0:
                player_destroyed += 1
                print('Patrol Boat Destroyed!')
            turn = 1
            break
      if hit == False:
        os.system('cls')
        add_to_board(board, target, '0')
        turn = 1
        print_board(board)
        print(target)
        print('MISS')

    if player_destroyed == 3:
      break

    # AI turn
    while turn == 1:
      # No target, random shooting
      while (current_target == '') & (turn == 1) & (hits == 0):
        print('1')
        time.sleep(2)
        print("AI's turn")
        print("Choosing target")
        time.sleep(2)
        ai_shot = random.choice(full_map)
        ai_shot_add = f'({ai_shot[0]}, {ai_shot[1]})'
        full_map.remove(ai_shot)
        hit = False

        for h in player_battleship['position']:
          if str(ai_shot) == str(h):
              hit = True
              player_battleship['health'] = player_battleship['health'] - 1
              player_battleship['hits'] = player_battleship['hits'] + 1
              os.system('cls')
              add_to_board2(board, ai_shot_add, 'X')
              print_board(board)
              print(ai_shot)
              print('HIT!')
              first_hit = ai_shot
              second_shots = [(first_hit[0], first_hit[1]+1), (first_hit[0], first_hit[1]-1), (first_hit[0]+1, first_hit[1]), (first_hit[0]-1, first_hit[1])]
              current_target = player_battleship
              turn = 0
              hits += 1
              break

        for h in player_destroyer['position']:
          if str(ai_shot) == str(h):
              hit = True
              player_destroyer['health'] = player_destroyer['health'] - 1
              player_destroyer['hits'] = player_destroyer['hits'] + 1
              os.system('cls')
              add_to_board2(board, ai_shot_add, 'X')
              print_board(board)
              print(ai_shot)
              print('HIT!')
              first_hit = ai_shot
              second_shots = [(first_hit[0], first_hit[1]+1), (first_hit[0], first_hit[1]-1), (first_hit[0]+1, first_hit[1]), (first_hit[0]-1, first_hit[1])]
              current_target = player_destroyer
              turn = 0
              hits += 1
              break

        for h in player_patrol_boat['position']:
          if str(ai_shot) == str(h):
              hit = True
              player_patrol_boat['health'] = player_patrol_boat['health'] - 1
              player_patrol_boat['hits'] = player_patrol_boat['hits'] + 1
              os.system('cls')
              add_to_board2(board, ai_shot_add, 'X')
              print_board(board)
              print(ai_shot)
              print('HIT!')
              first_hit = ai_shot
              second_shots = [(first_hit[0], first_hit[1]+1), (first_hit[0], first_hit[1]-1), (first_hit[0]+1, first_hit[1]), (first_hit[0]-1, first_hit[1])]
              current_target = player_patrol_boat
              turn = 0
              hits += 1
              break

        if hit == False:
          os.system('cls')
          add_to_board2(board, ai_shot_add, '0')
          print_board(board)
          print(ai_shot)
          print('MISS')
          turn = 0

      # has a target, shooting around the first hit
      while (current_target != '') & (turn == 1) & (hits == 1):
        for a in second_shots:
          if a not in full_map:
            second_shots.remove(a)
        print('2')
        print(current_target['type'])
        print(current_target['position'])
        time.sleep(2)
        print("AI's turn")
        print("Choosing target")
        time.sleep(2)
        ai_shot = random.choice(second_shots)
        ai_shot_add = f'({ai_shot[0]}, {ai_shot[1]})'
        second_shots.remove(ai_shot)
        full_map.remove(ai_shot)
        hit = False

        for h in current_target['position']:
          if str(ai_shot) == str(h):
            hit = True
            current_target['health'] = current_target['health'] - 1
            current_target['hits'] = current_target['hits'] + 1
            os.system('cls')
            add_to_board2(board, ai_shot_add, 'X')
            print_board(board)
            print(ai_shot)
            print('HIT!')
            second_hit = ai_shot

            more_shots_W = [(second_hit[0]-1, second_hit[1]), (second_hit[0]-2, second_hit[1])]
            more_shots_E = [(first_hit[0]+1, first_hit[1]), (first_hit[0]+2, first_hit[1])]
            more_shots_N = [(second_hit[0], second_hit[1]+1), (second_hit[0], second_hit[1]+2)]
            more_shots_S = [(first_hit[0], first_hit[1]-1), (first_hit[0], first_hit[1]-2)]

            if (first_hit[0] - second_hit[0]) == 1:
              fire_direction = 'W'
            
            elif (first_hit[0] - second_hit[0] == -1):
              fire_direction = 'E'
            
            elif (first_hit[1] - second_hit[1] == 1):
              fire_direction = 'S'

            elif (first_hit[1] - second_hit[1] == -1):
              fire_direction = 'N'

            for b in more_shots_W:
              if b not in full_map:
                more_shots_W.remove(b)
            if len(more_shots_W) == 0:
              fire_direction = 'E'

            for b in more_shots_E:
              if b not in full_map:
                more_shots_E.remove(b)
            if len(more_shots_E) == 0:
              fire_direction = 'W'

            for b in more_shots_N:
              if b not in full_map:
                more_shots_N.remove(b)
            if len(more_shots_N) == 0:
              fire_direction = 'S'

            for b in more_shots_S:
              if b not in full_map:
                more_shots_S.remove(b)
            if len(more_shots_S) == 0:
              fire_direction = 'N'

            if current_target['health'] == 0:
                ai_destroyed += 1
                name = current_target['type']
                print(f'Your {name} was Destroyed!')
                current_target['hits'] = 0
                current_target = ''
                turn = 0
                hits = 0
                break
            hits += 1
            turn = 0
            break

        if hit == False:
          os.system('cls')
          add_to_board2(board, ai_shot_add, '0')
          turn = 0
          print_board(board)
          print(second_shots)
          print(ai_shot)
          print('MISS')

      # Continueing shots past the first 2 hits
      while (current_target != '') & (turn == 1) & (hits >= 2):
        print('3')
        time.sleep(2)
        print("AI's turn")
        print("Choosing target")
        time.sleep(2)
        hit = False

        if len(more_shots_W) == 0:
            fire_direction = 'E'
        if len(more_shots_E) == 0:
            fire_direction = 'W'
        if len(more_shots_S) == 0:
            fire_direction = 'N'
        if len(more_shots_N) == 0:
            fire_direction = 'S'

        if fire_direction == 'W':
          # Left
          ai_shot = more_shots_W[0]
          ai_shot_add = f'({ai_shot[0]}, {ai_shot[1]})'
          print(ai_shot)
          full_map.remove(ai_shot)
          more_shots_W.remove(ai_shot)
        
        elif fire_direction == 'E':
          # Right
          ai_shot = more_shots_E[0]
          ai_shot_add = f'({ai_shot[0]}, {ai_shot[1]})'
          print(ai_shot)
          full_map.remove(ai_shot)
          more_shots_E.remove(ai_shot)

        elif fire_direction == 'S':
          # down
          ai_shot = more_shots_S[0]
          ai_shot_add = f'({ai_shot[0]}, {ai_shot[1]})'
          print(ai_shot)
          full_map.remove(ai_shot)
          more_shots_S.remove(ai_shot)

        elif fire_direction == 'N':
          # up
          ai_shot = more_shots_N[0]
          ai_shot_add = f'({ai_shot[0]}, {ai_shot[1]})'
          print(ai_shot)
          full_map.remove(ai_shot)
          more_shots_N.remove(ai_shot)

        for h in current_target['position']:
          if str(ai_shot) == str(h):
              current_target['health'] = current_target['health'] - 1
              current_target['hits'] = current_target['hits'] + 1
              os.system('cls')
              add_to_board2(board, ai_shot_add, 'X')
              print_board(board)
              print(ai_shot)
              print('HIT!')
              if current_target['health'] == 0:
                  ai_destroyed += 1
                  name = current_target['type']
                  print(f'Your {name} was Destroyed!')
                  current_target = ''
                  hits = 0
              turn = 0
              hit = True
              break
            
        if hit == False:
          if fire_direction == 'W':
            fire_direction = 'E'
        
          elif fire_direction == 'E':
            fire_direction = 'W'

          elif fire_direction == 'S':
            fire_direction = 'N'

          elif fire_direction == 'N':
            fire_direction = 'S'

          os.system('cls')
          add_to_board2(board, ai_shot_add, '0')
          turn = 0
          print_board(board)
          print(ai_shot)
          print('MISS')

    if ai_destroyed == 3:
      print('Game Over, You Lose')
      game_running == False
      break

    if player_destroyed == 3:
      print('Game Over, You Win')
      game_running == False
      break
  print('Would you like to play again? Y/N')
  answer = input()
  if answer.lower() == 'y':
    game_start = True
  elif answer.lower() == 'n':
    game_start = False
