import sys
import getpass
import random
from random import randint
import time


def b_start(multiplayer=True):
    blue = '\033[34m'
    red = '\033[31m'
    yellow = '\033[33m'
    white = '\033[0m'
    column_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    row_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    directions = ["h", "v"]
    Rows = input("Please choose how many rows do you want (5-10)!")
    while Rows not in row_names[4:]:
        Rows = input("Please choose how many rows do you want (5-10)!")
    Rows = int(Rows)
    Columns = input("Please choose how many columns do you want (5-10)!")
    while Columns not in row_names[4:]:
        Columns = input("Please choose how many columns do you want (5-10)!")
    Columns = int(Columns)
    p1_score = 0
    p2_score = 0

    def create_grid_p1(Rows, Columns):
        #  creates grid for player 1
        grid_p1 = []
        for row in range(Rows):
            row = []
            for col in range(Columns):
                row.append(' ')
            grid_p1.append(row)
        return grid_p1

    def create_grid_p2(Rows, Columns):
        #  creates grid for player 2
        grid_p2 = []
        for row in range(Rows):
            row = []
            for col in range(Columns):
                row.append(' ')
            grid_p2.append(row)
        return grid_p2

    def display_grid_p1(grid_p1, Columns):
        #  shows grid of player 1
        print(
            blue +
            "\n╔═╗╦  ╔═╗╦ ╦╔═╗╦═╗" +
            white +
            "┌─┐┬" +
            blue +
            "\n╠═╝║  ╠═╣╚╦╝║╣ ╠╦╝" +
            white +
            "│ ││" +
            blue +
            "\n╩  ╩═╝╩ ╩ ╩ ╚═╝╩╚═" +
            white +
            "└─┘┴")
        column_names = 'ABCDEFGHIJ'[:Columns]
        print('   | ' + ' | '.join(column_names) + ' |')
        for number, row in enumerate(grid_p1):
            if number < 9:
                print(number + 1, ' | ' + ' | '.join(row) + ' |')
            else:
                print(number + 1, '| ' + ' | '.join(row) + ' |')

    def display_grid_p2(grid_p2, Columns):
        #  shows grid of p2
        print(
            blue +
            "\n╔═╗╦  ╔═╗╦ ╦╔═╗╦═╗" +
            white +
            "┌─┐┌─┐" +
            blue +
            "\n╠═╝║  ╠═╣╚╦╝║╣ ╠╦╝" +
            white +
            "│ │┌─┘" +
            blue +
            "\n╩  ╩═╝╩ ╩ ╩ ╚═╝╩╚═" +
            white +
            "└─┘└─┘")
        column_names = 'ABCDEFGHIJ'[:Columns]
        print('   | ' + ' | '.join(column_names) + ' |')
        for number, row in enumerate(grid_p2):
            if number < 9:
                print(number + 1, ' | ' + ' | '.join(row) + ' |')
            else:
                print(number + 1, '| ' + ' | '.join(row) + ' |')

    grid_p1 = create_grid_p1(Rows, Columns)
    grid_p2 = create_grid_p2(Rows, Columns)
    grid_p1 = create_grid_p1(Rows, Columns)
    display_grid_p1(grid_p1, Columns)
    grid_p2 = create_grid_p2(Rows, Columns)
    display_grid_p2(grid_p2, Columns)

    def update_gridHit_p1(grid_p1, guess_row, guess_column):
        grid_p1[int(guess_row) - 1][column_names.index(guess_column)] = (red + 'O' + white)

    def update_gridMiss_p1(grid_p1, guess_row, guess_column):
        grid_p1[int(guess_row) - 1][column_names.index(guess_column)] = (blue + 'X' + white)

    def update_gridHit_p2(grid_p2, guess_row, guess_column):
        grid_p2[int(guess_row) - 1][column_names.index(guess_column)] = (red + 'O' + white)

    def update_gridMiss_p2(grid_p2, guess_row, guess_column):
        grid_p2[int(guess_row) - 1][column_names.index(guess_column)] = (blue + 'X' + white)

    def ship_placement_AI(shiptype):  # ship placement
        while True:
            ship_x = random.choice(column_names[0:Columns])
            column_index = column_names.index(ship_x)
            ship_y = str(randint(1, Columns))
            direction = random.choice(directions)
            if shiptype == "destroyer":
                if ship_x not in column_names[0:(Columns -
                                                 1)] and direction == "h" or int(ship_y) > (Rows -
                                                                                            1) and direction == "v":
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y, ship_x + str(int(ship_y) + 1)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y, column_names[(column_index + 1)] + ship_y]
                    return ship
            if shiptype == "cruiser" or shiptype == "submarine":
                if ship_x not in column_names[0:(Columns -
                                                 2)] and direction == "h" or int(ship_y) > (Rows -
                                                                                            2) and direction == "v":
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y,
                            ship_x + str(int(ship_y) + 1),
                            ship_x + str(int(ship_y) + 2)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y,
                            column_names[(column_index + 1)] + ship_y,
                            column_names[(column_index + 2)] + ship_y]
                    return ship
            if shiptype == "battleship":
                if ship_x not in column_names[0:(Columns -
                                                 3)] and direction == "h" or int(ship_y) > (Rows -
                                                                                            3) and direction == "v":
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y,
                            ship_x + str(int(ship_y) + 1),
                            ship_x + str(int(ship_y) + 2),
                            ship_x + str(int(ship_y) + 3)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y,
                            column_names[(column_index + 1)] + ship_y,
                            column_names[(column_index + 2)] + ship_y,
                            column_names[(column_index + 3)] + ship_y]
                    return ship
            if shiptype == "carrier":
                if ship_x not in column_names[0:(Columns -
                                                 4)] and direction == "h" or int(ship_y) > (Rows -
                                                                                            4) and direction == "v":
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
                            column_names[(column_index + 1)] + ship_y,
                            column_names[(column_index + 2)] + ship_y,
                            column_names[(column_index + 3)] + ship_y,
                            column_names[(column_index + 4)] + ship_y]
                    return ship

    def ship_placement_human(shiptype):  # ship placement
        while True:
            ship_x = getpass.getpass("Please select a column for " + shiptype + ": ").upper()
            if ship_x not in column_names[0:Columns]:
                quit_question = input("Are you sure you want to quit?\n").lower()
                if quit_question == "yes":
                    sys.exit()
                print("Invalid position! Please try again!")
                continue
            column_index = column_names.index(ship_x)
            ship_y = getpass.getpass("Please select a row for " + shiptype + ": ")
            if ship_y not in row_names[0:Rows]:
                quit_question = input("Are you sure you want to quit?\n").lower()
                if quit_question == "yes":
                    sys.exit()
                print("Invalid position! Please try again!")
                continue
            direction = getpass.getpass("[H]orizontal or [V]ertical?").lower()
            while direction not in directions:
                print("Please enter a valid direction!")
                direction = getpass.getpass("[H]orizontal or [V]ertical?").lower()
            if shiptype == "destroyer":
                if ship_x not in column_names[0:(Columns -
                                                 1)] and direction == "h" or int(ship_y) > (Rows -
                                                                                            1) and direction == "v":
                    print("No room for your ship there! Please replace!")
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y, ship_x + str(int(ship_y) + 1)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y, column_names[(column_index + 1)] + ship_y]
                    return ship
            if shiptype == "cruiser" or shiptype == "submarine":
                if ship_x not in column_names[0:(Columns -
                                                 2)] and direction == "h" or int(ship_y) > (Rows -
                                                                                            2) and direction == "v":
                    print("No room for your ship there! Please replace!")
                    continue
                elif direction == "v":
                    ship = [ship_x + ship_y,
                            ship_x + str(int(ship_y) + 1),
                            ship_x + str(int(ship_y) + 2)]
                    return ship
                elif direction == "h":
                    ship = [ship_x + ship_y,
                            column_names[(column_index + 1)] + ship_y,
                            column_names[(column_index + 2)] + ship_y]
                    return ship
            if shiptype == "battleship":
                if ship_x not in column_names[0:(Columns -
                                                 3)] and direction == "h" or int(ship_y) > (Rows -
                                                                                            3) and direction == "v":
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
                            column_names[(column_index + 1)] + ship_y,
                            column_names[(column_index + 2)] + ship_y,
                            column_names[(column_index + 3)] + ship_y]
                    return ship
            if shiptype == "carrier":
                if ship_x not in column_names[0:(Columns -
                                                 4)] and direction == "h" or int(ship_y) > (Rows -
                                                                                            4) and direction == "v":
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
                            column_names[(column_index + 1)] + ship_y,
                            column_names[(column_index + 2)] + ship_y,
                            column_names[(column_index + 3)] + ship_y,
                            column_names[(column_index + 4)] + ship_y]
                    return ship

    def shipcheck(ai=False):  # checking if ships are placed proper and puts coordinates in a list
        if ai is True:
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
            if Columns > 7 and Rows > 7:
                ship5 = ship_placement_AI("carrier")
                while (bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3))
                       or bool(set(ship1) & set(ship4)) or bool(set(ship2) & set(ship3))
                       or bool(set(ship2) & set(ship4)) or bool(set(ship3) & set(ship4))
                       or bool(set(ship5) & set(ship1)) or bool(set(ship5) & set(ship2))
                       or bool(set(ship5) & set(ship3)) or bool(set(ship5) & set(ship4))):
                    ship5 = ship_placement_AI("carrier")
                ships = [ship1, ship2, ship3, ship4, ship5]
            else:
                ships = [ship1, ship2, ship3, ship4, []]
            return ships
        if ai is False:
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
            if Columns > 7 and Rows > 7:
                ship5 = ship_placement_human("carrier")
                while (bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3))
                       or bool(set(ship1) & set(ship4)) or bool(set(ship2) & set(ship3))
                       or bool(set(ship2) & set(ship4)) or bool(set(ship3) & set(ship4))
                       or bool(set(ship5) & set(ship1)) or bool(set(ship5) & set(ship2))
                       or bool(set(ship5) & set(ship3)) or bool(set(ship5) & set(ship4))):
                    print("Ships cannot collide! Please replace your battleship!")
                    ship5 = ship_placement_human("carrier")
                ships = [ship1, ship2, ship3, ship4, ship5]
            else:
                ships = [ship1, ship2, ship3, ship4, []]
            return ships

    if multiplayer is True:
        print("Player 1 place your ships!")
        p1_ships = shipcheck()
        print("Player 2 place your ships!")
        p2_ships = shipcheck()

        player = 1  # battle phase
        while player == 1:
            print("\nPLAYER 01:")
            guess_column = input("Which column do you guess? \n").upper()
            if guess_column not in column_names[0:Columns]:
                quit_question = input("Are you sure you want to quit?\n").lower()
                if quit_question == "yes":
                    sys.exit()
                else:
                    continue
            guess_row = input("Which row do you guess? \n")
            if guess_row not in row_names[0:Rows]:
                quit_question = input("Are you sure you want to quit?\n").lower()
                if quit_question == "yes":
                    sys.exit()
                else:
                    continue
            guess = [guess_column + guess_row]

            if bool(
                set(guess) & set(
                    p2_ships[0]) or set(guess) & set(
                    p2_ships[1]) or set(guess) & set(
                    p2_ships[2]) or set(guess) & set(
                    p2_ships[3]) or set(guess) & set(
                    p2_ships[4])):
                if (grid_p2[int(guess_row) - 1][column_names.index(guess_column)] == (red + 'O' + white)):
                    yellow = '\033[33m'  # ascii
                    white = '\033[0m'  # normal
                    print(yellow + "You guessed that already!" + white)
                else:
                    blue = '\033[34m'  # water
                    red = '\033[31m'  # logo
                    yellow = '\033[33m'  # ascii
                    white = '\033[0m'  # normal
                    update_gridHit_p2(grid_p2, guess_row, guess_column)
                    display_grid_p2(grid_p2, Columns)
                    print(
                        red+" __________ /)  you have hit\n(__________((>    an enemy\n            \)     vessel"
                        + white)
                    p1_score += 1
                    if p1_score == 17 and (Rows * Columns) > 63 or p1_score == 12 and (Rows * Columns) < 64:
                        print(yellow + "\n" +
                              "               )\n" +
                              "            ( /(       )\n" +
                              "            )\())(  ( /(\n" +
                              "           ((_)\ )\ )\())\n" +
                              "             ((_|(_|_))/\n" + " " + red +
                              "            | ¤   ¤   ¤ | __\n" +
                              "    \----|----------------||--/\n" +
                              "     \   o   o   o   o   o   /\n" + " " + blue +
                              "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n" +
                              "\nPlayer 1, you are victorious!\nCongratulations!" + white)
                        sys.exit("Program ended")
                    player = 2

            else:
                if (int(guess_row) < 0 or int(guess_row) > int(Rows)) or guess_column not in column_names:
                    print("Outside the set grid. Please pick a number within it your Rows and Columns.")

                elif (grid_p2[int(guess_row) - 1][column_names.index(guess_column)+1] == (blue + 'X' + white)):
                    yellow = '\033[33m'  # ascii
                    white = '\033[0m'  # normal
                    print(yellow + "You guessed that already." + white)

                else:
                    # Updates the grid with an "X" saying that you missed the ship
                    blue = '\033[34m'  # water
                    white = '\033[0m'  # normal
                    update_gridMiss_p2(grid_p2, guess_row, guess_column)
                    display_grid_p2(grid_p2, Columns)
                    print(blue + "You missed!" + white)
                    player = 2

            # checks quesses of p1
            while player == 2:
                print("\nPLAYER 02:")
                guess_column = input("Which column do you guess? \n").upper()
                if guess_column not in column_names[0:Columns]:
                    quit_question = input("Are you sure you want to quit?\n").lower()
                    if quit_question == "yes":
                        sys.exit()
                    else:
                        continue
                guess_row = input("Which row do you guess? \n")
                if guess_row not in row_names[0:Rows]:
                    quit_question = input("Are you sure you want to quit?\n").lower()
                    if quit_question == "yes":
                        sys.exit()
                    else:
                        continue
                guess = [guess_column + guess_row]

                if bool(
                    set(guess) & set(
                        p1_ships[0]) or set(guess) & set(
                        p1_ships[1]) or set(guess) & set(
                        p1_ships[2]) or set(guess) & set(
                        p1_ships[3]) or set(guess) & set(
                        p1_ships[4])):
                    if grid_p1[int(guess_row) - 1][column_names.index(guess_column)] == (red + 'O' + white):
                        yellow = '\033[33m'  # ascii
                        white = '\033[0m'  # normal
                        print(yellow + "You guessed that already!" + white)
                    else:
                        blue = '\033[34m'  # water
                        red = '\033[31m'  # logo
                        yellow = '\033[33m'  # ascii
                        white = '\033[0m'  # normal
                        update_gridHit_p1(grid_p1, guess_row, guess_column)
                        display_grid_p1(grid_p1, Columns)
                        print(
                            red+" __________ /)  you have hit\n(__________((>    an enemy\n            \)     vessel"
                            + white)
                        p2_score += 1
                        if p2_score == 17 and (Rows * Columns) > 63 or p2_score == 12 and (Rows * Columns) < 64:
                            print(yellow + "\n" +
                                  "               )\n" +
                                  "            ( /(       )\n" +
                                  "            )\())(  ( /(\n" +
                                  "           ((_)\ )\ )\())\n" +
                                  "             ((_|(_|_))/\n" + " " + red +
                                  "            | ¤   ¤   ¤ | __\n" +
                                  "    \----|----------------||--/\n" +
                                  "     \   o   o   o   o   o   /\n" + " " + blue +
                                  "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n" +
                                  "\nPlayer 1, you are victorious!\nCongratulations!" + white)
                            sys.exit("Program ended")
                        player = 1

                else:
                    if (int(guess_row) < 1 or int(guess_row) > int(Rows)) or guess_column not in column_names:
                        print("Outside the set grid. Please pick a number within it your Rows and Columns.")

                    elif grid_p1[int(guess_row) - 1][column_names.index(guess_column)] == (blue + 'X' + white):
                        yellow = '\033[33m'  # ascii
                        white = '\033[0m'  # normal
                        print(yellow + "You guessed that already." + white)

                    else:
                        # Updates the grid with an "X" saying that you missed the ship
                        blue = '\033[34m'  # water
                        white = '\033[0m'  # normal
                        update_gridMiss_p1(grid_p1, guess_row, guess_column)
                        display_grid_p1(grid_p1, Columns)
                        print(blue + "You missed!" + white)
                        player = 1

    if multiplayer is False:
        print("Player 1 place your ships!")
        p1_ships = shipcheck()
        p2_ships = shipcheck(True)

        player = 1  # battle phase
        while True:
            # checks quesses of p1
            while player == 1:
                print("\nPLAYER 01:")
                guess_column = input("Which column do you guess? \n").upper()
                if guess_column not in column_names[0:Columns]:
                    quit_question = input("Are you sure you want to quit?\n").lower()
                    if quit_question == "yes":
                        sys.exit()
                    else:
                        continue
                guess_row = input("Which row do you guess? \n").upper()
                if guess_row not in row_names[0:Rows]:
                    quit_question = input("Are you sure you want to quit?\n")
                    if quit_question == "Yes":
                        sys.exit()
                    else:
                        continue
                guess = [guess_column + guess_row]

                if bool(
                    set(guess) & set(
                        p2_ships[0]) or set(guess) & set(
                        p2_ships[1]) or set(guess) & set(
                        p2_ships[2]) or set(guess) & set(
                        p2_ships[3]) or set(guess) & set(
                        p2_ships[4])):
                    if grid_p2[int(guess_row) - 1][column_names.index(guess_column)] == (red + 'O' + white):
                        print(yellow + "You guessed that already!" + white)
                    else:
                        update_gridHit_p2(grid_p2, guess_row, guess_column)
                        display_grid_p2(grid_p2, Columns)
                        print(
                            red+" __________ /)  you have hit\n(__________((>    an enemy\n            \)     vessel"
                            + white)
                        p1_score += 1
                        if p1_score == 17 and (Rows * Columns) > 63 or p1_score == 12 and (Rows * Columns) < 64:
                            print(yellow + "\n" +
                                  "               )\n" +
                                  "            ( /(       )\n" +
                                  "            )\())(  ( /(\n" +
                                  "           ((_)\ )\ )\())\n" +
                                  "             ((_|(_|_))/\n" + " " + red +
                                  "            | ¤   ¤   ¤ | __\n" +
                                  "    \----|----------------||--/\n" +
                                  "     \   o   o   o   o   o   /\n" + " " + blue +
                                  "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n" +
                                  "\nPlayer 1, you are victorious!\nCongratulations!" + white)
                            sys.exit("Program ended")
                        time.sleep(0.5)
                        print("\nArtificial Unintelligence is thinking...")
                        time.sleep(0.5)
                        player = 2

                else:
                    if (int(guess_row) < 0 or int(guess_row) > int(Rows)) or guess_column not in column_names:
                        print("Outside the set grid. Please pick a number within it your Rows and Columns.")

                    elif grid_p2[int(guess_row) - 1][column_names.index(guess_column)] == (blue + 'X' + white):
                        yellow = '\033[33m'  # ascii
                        white = '\033[0m'  # normal
                        print(yellow + "You guessed that already." + white)

                    else:
                        # Updates the grid with an "X" saying that you missed the ship
                        blue = '\033[34m'  # water
                        white = '\033[0m'  # normal
                        update_gridMiss_p2(grid_p2, guess_row, guess_column)
                        display_grid_p2(grid_p2, Columns)
                        print(blue + "You missed!" + white)
                        time.sleep(0.5)
                        print("\nArtificial Unintelligence is thinking...")
                        time.sleep(0.5)
                        player = 2

            # checks quesses of p1
            while player == 2:
                guess_column = random.choice(column_names[0:Columns])
                if guess_column not in column_names:
                    sys.exit()
                guess_row = str(randint(1, Rows))
                guess = [guess_column + guess_row]

                if bool(
                    set(guess) & set(
                        p1_ships[0]) or set(guess) & set(
                        p1_ships[1]) or set(guess) & set(
                        p1_ships[2]) or set(guess) & set(
                        p1_ships[3]) or set(guess) & set(
                        p1_ships[4])):
                    if (grid_p1[int(guess_row) - 1][column_names.index(guess_column)] == (red + 'O' + white)):
                        continue
                    else:
                        update_gridHit_p1(grid_p1, guess_row, guess_column)
                        display_grid_p1(grid_p1, Columns)
                        p2_score += 1
                        if p2_score == 17 and (Rows * Columns) > 63 or p2_score == 12 and (Rows * Columns) < 64:
                            print(yellow + "\n" +
                                  "               )\n" +
                                  "            ( /(       )\n" +
                                  "            )\())(  ( /(\n" +
                                  "           ((_)\ )\ )\())\n" +
                                  "             ((_|(_|_))/\n" + " " + red +
                                  "            | ¤   ¤   ¤ | __\n" +
                                  "    \----|----------------||--/\n" +
                                  "     \   o   o   o   o   o   /\n" + " " + blue +
                                  "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n" +
                                  "\nPlayer 1, you are victorious!\nCongratulations!" + white)
                            sys.exit("Program ended")
                        player = 1

                else:
                    if grid_p1[int(guess_row) - 1][column_names.index(guess_column)] == (blue + 'X' + white):
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
          "-You have four vessels, their lengths are marked by their names\n" +
          "-You can't place your vessels on top of each other\n" +
          "-During input, your coordinates will be hidden\n" +
          "-Destroy all enemy vessels by guessing their locations, to win\n" +
          "-X marks a miss, O marks a hit\n" +
          "-If you guess right, or miss, your turn ends\n" +
          "-If you try to hit the same coordinates again, you can try again")


def game_init():
    blue = '\033[34m'  # water
    red = '\033[31m'  # logo
    yellow = '\033[33m'  # ascii
    white = '\033[0m'  # normal
    print("\nWELCOME TO")
    print(
        blue +
        "\n╔╗ ╔═╗╔╦╗╔╦╗╦  ╔═╗╔═╗╦ ╦╦╔═╗\n" +
        white +
        "╠╩╗╠═╣ ║  ║ ║  ║╣ ╚═╗╠═╣║╠═╝\n" +
        blue +
        "╚═╝╩ ╩ ╩  ╩ ╩═╝╚═╝╚═╝╩ ╩╩╩ " +
        white)
    while True:
        start = input("\nPress P to play, H for help or Q to exit!\n")
        if start.lower() == "p":
            game_players = input("[S]ingle Player or [M]ultiplayer?").lower()
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
