import sys
import getpass
import random
from random import randint


def b_start(multiplayer = True):
    column_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    directions = ["h", "v"]
    Rows = 10
    Columns = 10
    p1_score = 0
    p2_score = 0

    def create_grid_p1(Rows, Columns):
        #  creates grid for p1
        grid_p1 = []
        for row in range(Rows):
            row = []
            for col in range(Columns):
                row.append(' ')
            grid_p1.append(row)
        return grid_p1

    def create_grid_p2(Rows, Columns):
        #  creates grid for p2
        grid_p2 = []
        for row in range(Rows):
            row = []
            for col in range(Columns):
                row.append(' ')
            grid_p2.append(row)
        return grid_p2

    grid_p1 = create_grid_p1(Rows, Columns)
    grid_p2 = create_grid_p2(Rows, Columns)

    def display_grid_p1(grid_p1, Columns):
        #  shows grid of p1
        print("\nBOARD OF PLAYER 01:")
        column_names = 'ABCDEFGHIJ'[:Columns]
        print('  | ' + ' | '.join(column_names) + ' |')
        for number, row in enumerate(grid_p1):
            print(number + 1, '| ' + ' | '.join(row) + ' |')

    grid_p1 = create_grid_p1(Rows, Columns)
    display_grid_p1(grid_p1, Columns)

    def display_grid_p2(grid_p2, Columns):
        #  shows grid of p2
        print("\nBOARD OF PLAYER 02:")
        column_names = 'ABCDEFGHIJ'[:Columns]
        print('  | ' + ' | '.join(column_names) + ' |')
        for number, row in enumerate(grid_p2):
            print(number + 1, '| ' + ' | '.join(row) + ' |')

    grid_p2 = create_grid_p2(Rows, Columns)
    display_grid_p2(grid_p2, Columns)

    def update_gridHit_p1(grid_p1, guess_row, guess_column):
        grid_p1[int(guess_row)-1][column_names.index(guess_column)] = 'O'

    def update_gridMiss_p1(grid_p1, guess_row, guess_column):
        grid_p1[int(guess_row)-1][column_names.index(guess_column)] = 'X'

    def update_gridHit_p2(grid_p2, guess_row, guess_column):
        grid_p2[int(guess_row)-1][column_names.index(guess_column)] = 'O'

    def update_gridMiss_p2(grid_p2, guess_row, guess_column):
        grid_p2[int(guess_row)-1][column_names.index(guess_column)] = 'X'

    def ship_placement_AI(shiptype):  # ship placement
        while True:
            ship_x = random.choice(column_names)
            column_index = column_names.index(ship_x)
            ship_y = str(randint(1, 10))
            direction = random.choice(directions)
            if shiptype == "destroyer":
                if ship_x not in column_names[0:9] and direction == "h" or int(ship_y) > 9 and direction == "v":
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y, ship_x + str(int(ship_y) + 1)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y, column_names[(column_index+1)] + ship_y]
                    return ship
            if shiptype == "cruiser" or shiptype == "submarine":
                if ship_x not in column_names[0:8] and direction == "h" or int(ship_y) > 8 and direction == "v":
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y,
                            ship_x + str(int(ship_y) + 1),
                            ship_x + str(int(ship_y) + 2)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y,
                            column_names[(column_index+1)] + ship_y,
                            column_names[(column_index+2)] + ship_y]
                    return ship
            if shiptype == "battleship":
                if ship_x not in column_names[0:7] and direction == "h" or int(ship_y) > 7 and direction == "v":
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y,
                            ship_x + str(int(ship_y) + 1),
                            ship_x + str(int(ship_y) + 2),
                            ship_x + str(int(ship_y) + 3)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y,
                            column_names[(column_index+1)] + ship_y,
                            column_names[(column_index+2)] + ship_y,
                            column_names[(column_index+3)] + ship_y]
                    return ship
            if shiptype == "carrier":
                if ship_x not in column_names[0:6] and direction == "h" or int(ship_y) > 6 and direction == "v":
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y,
                            ship_x + str(int(ship_y) + 1),
                            ship_x + str(int(ship_y) + 2),
                            ship_x + str(int(ship_y) + 3),
                            ship_x + str(int(ship_y) + 4)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y,
                            column_names[(column_index+1)] + ship_y,
                            column_names[(column_index+2)] + ship_y,
                            column_names[(column_index+3)] + ship_y,
                            column_names[(column_index+4)] + ship_y]
                    return ship

    def ship_placement_human(shiptype):  # ship placement
        while True:
            try:  # exit during placement, see below at except
                ship_x = getpass.getpass("Please select a column for "+shiptype+": ").upper()
                column_index = column_names.index(ship_x)
                if ship_x not in column_names:
                    print("Invalid position! Please try again!")
                    continue
                ship_y = getpass.getpass("Please select a row for "+shiptype+": ")
                if int(ship_y) < 1 or int(ship_y) > 10:
                    print("Invalid position! Please try again!")
                    continue
                direction = getpass.getpass("[H]orizontal or [V]ertical?").lower()
                while direction not in directions:
                    print("Please enter a valid direction!")
                    direction = getpass.getpass("[H]orizontal or [V]ertical?").lower()
                if shiptype == "destroyer":
                    if ship_x not in column_names[0:9] and direction == "h" or int(ship_y) > 9 and direction == "v":
                        print("No room for your ship there! Please replace!")
                        continue
                    elif direction == "v":
                        ship = [ship_x + ship_y, ship_x + str(int(ship_y) + 1)]
                        return ship
                    elif direction == "h":
                        ship = [ship_x + ship_y, column_names[(column_index+1)] + ship_y]
                        return ship
                if shiptype == "cruiser" or shiptype == "submarine":
                    if ship_x not in column_names[0:8] and direction == "h" or int(ship_y) > 8 and direction == "v":
                        print("No room for your ship there! Please replace!")
                        continue
                    elif direction == "v":
                        ship = [ship_x + ship_y,
                                ship_x + str(int(ship_y) + 1),
                                ship_x + str(int(ship_y) + 2)]
                        return ship
                    elif direction == "h":
                        ship = [ship_x + ship_y,
                                column_names[(column_index+1)] + ship_y,
                                column_names[(column_index+2)] + ship_y]
                        return ship
                if shiptype == "battleship":
                    if ship_x not in column_names[0:7] and direction == "h" or int(ship_y) > 7 and direction == "v":
                        print("No room for your ship there! Please replace!")
                        continue
                    elif direction == "v":
                        ship = [ship_x + ship_y,
                                ship_x + str(int(ship_y) + 1),
                                ship_x + str(int(ship_y) + 2),
                                ship_x + str(int(ship_y) + 3)]
                        return ship
                    elif direction == "h":
                        ship = [ship_x + ship_y,
                                column_names[(column_index+1)] + ship_y,
                                column_names[(column_index+2)] + ship_y,
                                column_names[(column_index+3)] + ship_y]
                        return ship
                if shiptype == "carrier":
                    if ship_x not in column_names[0:6] and direction == "h" or int(ship_y) > 6 and direction == "v":
                        print("No room for your ship there! Please replace!")
                        continue
                    elif direction == "v":
                        ship = [ship_x + ship_y,
                                ship_x + str(int(ship_y) + 1),
                                ship_x + str(int(ship_y) + 2),
                                ship_x + str(int(ship_y) + 3),
                                ship_x + str(int(ship_y) + 4)]
                        return ship
                    elif direction == "h":
                        ship = [ship_x + ship_y,
                                column_names[(column_index+1)] + ship_y,
                                column_names[(column_index+2)] + ship_y,
                                column_names[(column_index+3)] + ship_y,
                                column_names[(column_index+4)] + ship_y]
                        return ship
            except BaseException:
                sys.exit("Program stopped")

    def shipcheck(ai=False):  # checking if ships are placed proper and puts coordinates in a list
        if ai == True:
            ship1 = ship_placement_AI("destroyer")
            ship2 = ship_placement_AI("cruiser")
            while bool(set(ship1) & set(ship2)):
                ship2 = ship_placement_AI("cruiser")
            ship3 = ship_placement_AI("submarine")
            while bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3)) or bool(set(ship2) & set(ship3)):
                ship3 = ship_placement_AI("submarine")
            ship4 = ship_placement_AI("battleship")
            while (bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3))
                   or bool(set(ship1) & set(ship4)) or bool(set(ship2) & set(ship3))
                   or bool(set(ship2) & set(ship4))or bool(set(ship3) & set(ship4))):
                ship4 = ship_placement_AI("battleship")
            ship5 = ship_placement_AI("carrier")
            while (bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3))
                   or bool(set(ship1) & set(ship4)) or bool(set(ship2) & set(ship3))
                   or bool(set(ship2) & set(ship4)) or bool(set(ship3) & set(ship4))
                   or bool(set(ship5) & set(ship1)) or bool(set(ship5) & set(ship2))
                   or bool(set(ship5) & set(ship3)) or bool(set(ship5) & set(ship4))):
                ship5 = ship_placement_AI("carrier")
            ships = [ship1, ship2, ship3, ship4, ship5]
            return ships
        if ai == False:
            ship1 = ship_placement_human("destroyer")
            ship2 = ship_placement_human("cruiser")
            while bool(set(ship1) & set(ship2)):
                print("Ships cannot collide! Please replace your cruiser!")
                ship2 = ship_placement_human("cruiser")
            ship3 = ship_placement_human("submarine")
            while bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3)) or bool(set(ship2) & set(ship3)):
                print("Ships cannot collide! Please replace your submarine!")
                ship3 = ship_placement_human("submarine")
            ship4 = ship_placement_human("battleship")
            while (bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3))
                   or bool(set(ship1) & set(ship4)) or bool(set(ship2) & set(ship3))
                   or bool(set(ship2) & set(ship4))or bool(set(ship3) & set(ship4))):
                print("Ships cannot collide! Please replace your battleship!")
                ship4 = ship_placement_human("battleship")
            ship5 = ship_placement_human("carrier")
            while (bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3))
                   or bool(set(ship1) & set(ship4)) or bool(set(ship2) & set(ship3))
                   or bool(set(ship2) & set(ship4)) or bool(set(ship3) & set(ship4))
                   or bool(set(ship5) & set(ship1)) or bool(set(ship5) & set(ship2))
                   or bool(set(ship5) & set(ship3)) or bool(set(ship5) & set(ship4))):
                print("Ships cannot collide! Please replace your battleship!")
                ship5 = ship_placement_human("carrier")
            ships = [ship1, ship2, ship3, ship4, ship5]
            return ships

    if multiplayer == True:
        print("Player 1 place your ships!")
        p1_ships = shipcheck()
        print("Player 2 place your ships!")
        p2_ships = shipcheck()

        player = 1  # battle phase
        while True:
            # checks quesses of p1
            while player == 1:
                print("\nPLAYER 01:")
                guess_column = input("Which column do you guess? \n").upper()
                if guess_column not in column_names:
                    sys.exit()
                guess_row = input("Which row do you guess? \n")
                try:
                    t = int(guess_row)
                except BaseException:
                    sys.exit("Program ended")
                guess = [guess_column + guess_row]

                if bool(
                    set(guess) & set(
                        p2_ships[0]) or set(guess) & set(
                        p2_ships[1]) or set(guess) & set(
                        p2_ships[2]) or set(guess) & set(
                        p2_ships[3]) or set(guess) & set(
                        p2_ships[4])):
                    if (grid_p2[int(guess_row) - 1][column_names.index(guess_column) ] == "O"):
                        print("You guessed that already!")
                    else:
                        update_gridHit_p2(grid_p2, guess_row, guess_column)
                        display_grid_p2(grid_p2, Columns)
                        print("You've hit an enemy vessel!")
                        p1_score += 1
                        if p1_score == 17:
                            print("\n" +
                                  "               )\n" +
                                  "            ( /(       )\n" +
                                  "            )\())(  ( /(\n" +
                                  "           ((_)\ )\ )\())\n" +
                                  "             ((_|(_|_))/\n" +
                                  "            | ¤   ¤   ¤ | __\n" +
                                  "    \----|----------------||--/\n" +
                                  "     \   o   o   o   o   o   /\n" +
                                  "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n" +
                                  "\nPlayer 1, you are victorious!\nCongratulations!")
                            sys.exit("Program ended")
                        player = 2

                else:
                    if (int(guess_row) < 0 or int(guess_row) > int(Rows)) or guess_column not in column_names:
                        print("Outside the set grid. Please pick a number within it your Rows and Columns.")

                    elif (grid_p2[int(guess_row) - 1][column_names.index(guess_column) ] == "X"):
                        print("You guessed that already.")

                    else:
                        # Updates the grid with an "X" saying that you missed the ship
                        print("You missed!")
                        update_gridMiss_p2(grid_p2, guess_row, guess_column)
                        display_grid_p2(grid_p2, Columns)
                        player = 2

            # checks quesses of p1
            while player == 2:
                print("\nPLAYER 02:")
                guess_column = input("Which column do you guess? \n").upper()
                if guess_column not in column_names:
                    sys.exit()
                guess_row = input("Which row do you guess? \n")
                try:
                    t = int(guess_row)
                except BaseException:
                    sys.exit("Program ended")
                guess = [guess_column + guess_row]

                if bool(
                    set(guess) & set(
                        p2_ships[0]) or set(guess) & set(
                        p2_ships[1]) or set(guess) & set(
                        p2_ships[2]) or set(guess) & set(
                        p2_ships[3]) or set(guess) & set(
                        p2_ships[4])):
                    if (grid_p1[int(guess_row) - 1][column_names.index(guess_column) ] == "O"):
                        print("You guessed that already!")
                    else:
                        update_gridHit_p1(grid_p1, guess_row, guess_column)
                        display_grid_p1(grid_p1, Columns)
                        print("You've hit an enemy vessel!")
                        p2_score += 1
                        if p2_score == 17:
                            print("\n" +
                                  "               )\n" +
                                  "            ( /(       )\n" +
                                  "            )\())(  ( /(\n" +
                                  "           ((_)\ )\ )\())\n" +
                                  "             ((_|(_|_))/\n" +
                                  "            | ¤   ¤   ¤ | __\n" +
                                  "    \----|----------------||--/\n" +
                                  "     \   o   o   o   o   o   /\n" +
                                  "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n" +
                                  "\nPlayer 2, you are victorious!\nCongratulations!")
                            sys.exit("Program ended")
                        player = 1

                else:
                    if (int(guess_row) < 1 or int(guess_row) > int(Rows)) or guess_column not in column_names:
                        print("Outside the set grid. Please pick a number within it your Rows and Columns.")

                    elif grid_p1[int(guess_row) - 1][column_names.index(guess_column)] == "X":
                        print("You guessed that already.")

                    else:
                        # Updates the grid with an "X" saying that you missed the ship
                        print("You missed!")
                        update_gridMiss_p1(grid_p1, guess_row, guess_column)
                        display_grid_p1(grid_p1, Columns)
                        player = 1

    if multiplayer == False:
        print("Player 1 place your ships!")
        p1_ships = shipcheck()
        p2_ships = shipcheck(True)

        player = 1  # battle phase
        while True:
            # checks quesses of p1
            while player == 1:
                print("\nPLAYER 01:")
                guess_column = input("Which column do you guess? \n").upper()
                if guess_column not in column_names:
                    sys.exit()
                guess_row = input("Which row do you guess? \n")
                try:
                    t = int(guess_row)
                except BaseException:
                    sys.exit("Program ended")
                guess = [guess_column + guess_row]

                if bool(
                    set(guess) & set(
                        p2_ships[0]) or set(guess) & set(
                        p2_ships[1]) or set(guess) & set(
                        p2_ships[2]) or set(guess) & set(
                        p2_ships[3]) or set(guess) & set(
                        p2_ships[4])):
                    if (grid_p2[int(guess_row) - 1][column_names.index(guess_column) ] == "O"):
                        print("You guessed that already!")
                    else:
                        update_gridHit_p2(grid_p2, guess_row, guess_column)
                        display_grid_p2(grid_p2, Columns)
                        print("You've hit an enemy vessel!")
                        p1_score += 1
                        if p1_score == 17:
                            print("\n" +
                                  "               )\n" +
                                  "            ( /(       )\n" +
                                  "            )\())(  ( /(\n" +
                                  "           ((_)\ )\ )\())\n" +
                                  "             ((_|(_|_))/\n" +
                                  "            | ¤   ¤   ¤ | __\n" +
                                  "    \----|----------------||--/\n" +
                                  "     \   o   o   o   o   o   /\n" +
                                  "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n" +
                                  "\nPlayer 1, you are victorious!\nCongratulations!")
                            sys.exit("Program ended")
                        player = 2

                else:
                    if (int(guess_row) < 0 or int(guess_row) > int(Rows)) or guess_column not in column_names:
                        print("Outside the set grid. Please pick a number within it your Rows and Columns.")

                    elif (grid_p2[int(guess_row) - 1][column_names.index(guess_column) ] == "X"):
                        print("You guessed that already.")

                    else:
                        # Updates the grid with an "X" saying that you missed the ship
                        print("You missed!")
                        update_gridMiss_p2(grid_p2, guess_row, guess_column)
                        display_grid_p2(grid_p2, Columns)
                        player = 2

            # checks quesses of p1
            while player == 2:
                guess_column = random.choice(column_names)
                if guess_column not in column_names:
                    sys.exit()
                guess_row = str(randint(1, 10))
                guess = [guess_column + guess_row]

                if bool(
                    set(guess) & set(
                        p2_ships[0]) or set(guess) & set(
                        p2_ships[1]) or set(guess) & set(
                        p2_ships[2]) or set(guess) & set(
                        p2_ships[3]) or set(guess) & set(
                        p2_ships[4])):
                    if (grid_p1[int(guess_row) - 1][column_names.index(guess_column) ] == "O"):
                        continue
                    else:
                        update_gridHit_p1(grid_p1, guess_row, guess_column)
                        display_grid_p1(grid_p1, Columns)
                        p2_score += 1
                        if p2_score == 17:
                            print("\n" +
                                  "               )\n" +
                                  "            ( /(       )\n" +
                                  "            )\())(  ( /(\n" +
                                  "           ((_)\ )\ )\())\n" +
                                  "             ((_|(_|_))/\n" +
                                  "            | ¤   ¤   ¤ | __\n" +
                                  "    \----|----------------||--/\n" +
                                  "     \   o   o   o   o   o   /\n" +
                                  "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n" +
                                  "\nPlayer 2, you are victorious!\nCongratulations!")
                            sys.exit("Program ended")
                        player = 1

                else:
                    if grid_p1[int(guess_row) - 1][column_names.index(guess_column)] == "X":
                        continue

                    else:
                        # Updates the grid with an "X" saying that you missed the ship
                        update_gridMiss_p1(grid_p1, guess_row, guess_column)
                        display_grid_p1(grid_p1, Columns)
                        player = 1


def b_help():
    print("\nHow to play:\n" +
          "-Abort any time during the game by entering a letter\n" +
          "-Use numbers to set the coordinates of the starting position of your vessels\n" +
          "-The size of the grid is 10 by 10\n" +
          "-You have four vessels, their lengths are marked by their names\n" +
          "-You can't place your vessels on top of each other\n" +
          "-During input, your coordinates will be hidden\n" +
          "-Destroy all enemy vessels by guessing their locations, to win\n" +
          "-X marks a miss, O marks a hit\n" +
          "-If you guess right, or miss, your turn ends\n" +
          "-If you try to hit the same coordinates again, you can try again")


def game_init():
    print("\nWELCOME TO\n╔╗ ╔═╗╔╦╗╔╦╗╦  ╔═╗╔═╗╦ ╦╦╔═╗\n╠╩╗╠═╣ ║  ║ ║  ║╣ ╚═╗╠═╣║╠═╝\n╚═╝╩ ╩ ╩  ╩ ╩═╝╚═╝╚═╝╩ ╩╩╩ ")
    while True:
        start = input("\nPress P to play, H for help or Q to exit!\n")
        if start.lower() == "p":
            game_players = input("Single Player or Multiplayer?").lower()
            if game_players == "s":
                b_start(False)
            elif game_players == "m":
                b_start()
        elif start.lower() == "h":
            b_help()
            continue
        elif start.lower() == "q":
            print("Program ended")
            break
        else:
            print("Please enter a valid command!")


game_init()
