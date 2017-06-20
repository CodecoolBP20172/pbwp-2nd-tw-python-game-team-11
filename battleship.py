import sys
import getpass

directions = ["h", "v"]
Rows = 6
Columns = 6


def b_start():
    p1score = 0
    p2score = 0

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
        column_names = '123456'[:Columns]
        print('  | ' + ' | '.join(column_names) + ' |')
        for number, row in enumerate(grid_p1):
            print(number + 1, '| ' + ' | '.join(row) + ' |')

    grid_p1 = create_grid_p1(Rows, Columns)
    display_grid_p1(grid_p1, Columns)

    def display_grid_p2(grid_p2, Columns):
        #  shows grid of p2
        print("\nBOARD OF PLAYER 02:")
        column_names = '123456'[:Columns]
        print('  | ' + ' | '.join(column_names) + ' |')
        for number, row in enumerate(grid_p2):
            print(number + 1, '| ' + ' | '.join(row) + ' |')

    grid_p2 = create_grid_p2(Rows, Columns)
    display_grid_p2(grid_p2, Columns)

    def update_gridHit_p1(grid_p1, GuessRow, GuessColumn):
        grid_p1[int(GuessRow) - 1][int(GuessColumn) - 1] = 'O'

    def update_gridMiss_p1(grid_p1, GuessRow, GuessColumn):
        grid_p1[int(GuessRow) - 1][int(GuessColumn) - 1] = 'X'

    def update_gridHit_p2(grid_p2, GuessRow, GuessColumn):
        grid_p2[int(GuessRow) - 1][int(GuessColumn) - 1] = 'O'

    def update_gridMiss_p2(grid_p2, GuessRow, GuessColumn):
        grid_p2[int(GuessRow) - 1][int(GuessColumn) - 1] = 'X'

    def ship(length):  # ship placement
        while True:
            try:  # exit during placement, see below at except
                shipx = getpass.getpass("Column of ship " + str(length) + ": ")
                if int(shipx) < 1 or int(shipx) > 6:
                    print("Invalid position! Please try again!")
                    continue
                shipy = getpass.getpass("Row of ship " + str(length) + ": ")
                if int(shipy) < 1 or int(shipy) > 6:
                    print("Invalid position! Please try again!")
                    continue
                direction = getpass.getpass("[H]orizontal or [V]ertical?").lower()
                while direction not in directions:
                    print("Please enter a valid direction!")
                    direction = getpass.getpass("[H]orizontal or [V]ertical?").lower()
                if length == 1:
                    if direction == "v":
                        ship = [shipx + " " + shipy]
                        return ship
                    elif direction == "h":
                        ship = [shipx + " " + shipy]
                        return ship
                if length == 2:
                    if int(shipx) > 5 and direction == "h" or int(shipy) > 5 and direction == "v":
                        print("No room for your ship there! Please replace!")
                        continue
                    elif direction == "v":
                        ship = [shipx + " " + shipy, shipx + " " + str(int(shipy) + 1)]
                        return ship
                    elif direction == "h":
                        ship = [shipx + " " + shipy, str(int(shipx) + 1) + " " + shipy]
                        return ship
                if length == 3:
                    if int(shipx) > 4 and direction == "h" or int(shipy) > 4 and direction == "v":
                        print("No room for your ship there! Please replace!")
                        continue
                    elif direction == "v":
                        ship = [shipx + " " + shipy,
                                shipx + " " + str(int(shipy) + 1),
                                shipx + " " + str(int(shipy) + 2)]
                        return ship
                    elif direction == "h":
                        ship = [shipx + " " + shipy, str(int(shipx) + 1) + " " + shipy,
                                str(int(shipx) + 2) + " " + shipy]
                        return ship
                if length == 4:
                    if int(shipx) > 3 and direction == "h" or int(shipy) > 3 and direction == "v":
                        print("No room for your ship there! Please replace!")
                        continue
                    elif direction == "v":
                        ship = [shipx + " " + shipy,
                                shipx + " " + str(int(shipy) + 1),
                                shipx + " " + str(int(shipy) + 2),
                                shipx + " " + str(int(shipy) + 3)]
                        return ship
                    elif direction == "h":
                        ship = [shipx + " " + shipy,
                                str(int(shipx) + 1) + " " + shipy,
                                str(int(shipx) + 2) + " " + shipy,
                                str(int(shipx) + 3) + " " + shipy]
                        return ship
            except BaseException:
                sys.exit("Program stopped")

    def shipcheck():  # checking if ships are placed proper and puts coordinates in a list
        ship1 = ship(1)
        ship2 = ship(2)
        while bool(set(ship1) & set(ship2)):
            print("Ships cannot collide! Please replace ship 2!")
            ship2 = ship(2)
        ship3 = ship(3)
        while bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3)) or bool(set(ship2) & set(ship3)):
            print("Ships cannot collide! Please replace ship 3!")
            ship3 = ship(3)
        ship4 = ship(4)
        while (bool(set(ship1) & set(ship2)) or bool(set(ship1) & set(ship3))
               or bool(set(ship1) & set(ship4)) or bool(set(ship2) & set(ship3))
               or bool(set(ship2) & set(ship4))or bool(set(ship3) & set(ship4))):
            print("Ships cannot collide! Please replace ship 4!")
            ship4 = ship(4)
        ships = [ship1, ship2, ship3, ship4]
        return ships
    print("Player 1 place your ships!")
    p1ships = shipcheck()
    print("Player 2 place your ships!")
    p2ships = shipcheck()

    player = 1  # battle phase
    while True:
        # checks quesses of p1
        while player == 1:
            print("\nPLAYER 01:")
            GuessRow = input("What row do you guess? \n")
            try:
                t = int(GuessRow)
            except BaseException:
                sys.exit("Program ended")
            GuessColumn = input("What column do you guess? \n")
            try:
                t = int(GuessColumn)
            except BaseException:
                sys.exit("Program ended")
            guess = [GuessColumn + " " + GuessRow]

            if bool(
                set(guess) & set(
                    p2ships[0]) or set(guess) & set(
                    p2ships[1]) or set(guess) & set(
                    p2ships[2]) or set(guess) & set(
                    p2ships[3])):
                if (grid_p2[int(GuessRow) - 1][int(GuessColumn) - 1] == "O"):
                    print("You guessed that already!")
                else:
                    update_gridHit_p2(grid_p2, GuessRow, GuessColumn)
                    display_grid_p2(grid_p2, Columns)
                    print("You've hit an enemy vessel!")
                    p1score += 1
                    if p1score == 10:
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
                if (int(GuessRow) < 1 or int(GuessRow) > int(Rows)) or (
                        int(GuessColumn) < 1 or int(GuessColumn) > int(Columns)):
                    print("Outside the set grid. Please pick a number within it your Rows and Columns.")

                elif (grid_p2[int(GuessRow) - 1][int(GuessColumn) - 1] == "X"):
                    print("You guessed that already.")

                else:
                    # Updates the grid with an "X" saying that you missed the ship
                    print("You missed!")
                    update_gridMiss_p2(grid_p2, GuessRow, GuessColumn)
                    display_grid_p2(grid_p2, Columns)
                    player = 2

        # checks quesses of p1
        while player == 2:
            print("\nPLAYER 02:")
            GuessRow = input("What row do you guess? \n")
            try:
                t = int(GuessRow)
            except BaseException:
                sys.exit("Program ended")
            GuessColumn = input("What column do you guess? \n")
            try:
                t = int(GuessColumn)
            except BaseException:
                sys.exit("Program ended")
            guess = [GuessColumn + " " + GuessRow]

            if bool(
                set(guess) & set(
                    p1ships[0]) or set(guess) & set(
                    p1ships[1]) or set(guess) & set(
                    p1ships[2]) or set(guess) & set(
                    p1ships[3])):
                if (grid_p1[int(GuessRow) - 1][int(GuessColumn) - 1] == "O"):
                    print("You guessed that already!")
                else:
                    update_gridHit_p1(grid_p1, GuessRow, GuessColumn)
                    display_grid_p1(grid_p1, Columns)
                    print("You've hit an enemy vessel!")
                    p2score += 1
                    if p2score == 10:
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
                if (int(GuessRow) < 1 or int(GuessRow) > int(Rows)) or (
                        int(GuessColumn) < 1 or int(GuessColumn) > int(Columns)):
                    print("Outside the set grid. Please pick a number within it your Rows and Columns.")

                elif (grid_p1[int(GuessRow) - 1][int(GuessColumn) - 1] == "X") or (grid_p1[int(GuessRow) - 1][int(GuessColumn) - 1] == "O"):
                    print("You guessed that already.")

                else:
                    # Updates the grid with an "X" saying that you missed the ship
                    print("You missed!")
                    update_gridMiss_p1(grid_p1, GuessRow, GuessColumn)
                    display_grid_p1(grid_p1, Columns)
                    player = 1


def b_help():
    print("\nHow to play:\n" +
          "-Abort any time during the game by entering a letter\n" +
          "-Use numbers to set the coordinates of the starting position of your vessels\n" +
          "-The size of the grid is 6 by 6\n" +
          "-You have four vessels, their lengths are marked by their names\n" +
          "-You can't place your vessels on top of each other\n" +
          "-During input, your coordinates will be hidden\n" +
          "-Destroy all enemy vessels by guessing their locations, to win\n" +
          "-X marks a miss, O marks a hit\n" +
          "-If you guess right, or miss, your turn ends\n" +
          "-If you try to hit the same coordinates again, you can try again")


print("\nWELCOME TO\n╔╗ ╔═╗╔╦╗╔╦╗╦  ╔═╗╔═╗╦ ╦╦╔═╗\n╠╩╗╠═╣ ║  ║ ║  ║╣ ╚═╗╠═╣║╠═╝\n╚═╝╩ ╩ ╩  ╩ ╩═╝╚═╝╚═╝╩ ╩╩╩ ")

while True:
    start = input("\nPress P to play, H for help or Q to exit!\n")
    if start.lower() == "p":
        b_start()
    elif start.lower() == "h":
        b_help()
        continue
    elif start.lower() == "q":
        print("Program ended")
        break
    else:
        print("Please enter a valid command!")
