from ShipFinder import *
from GameBoard import *
from ShipHitValidation import *
from ScoreNode import *
from ScoreBoard import *

class Game(object):

    def run(self):

        print("Welcome to Battleship (kind of)!\n"
              "A random playing field will be generated...\n"
              "On each turn enter the row and column number you would like to shoot at to reveal a ship.\n"
              "You will be provided 10 missiles to hit all the ships on the playing board.\n"
              "If you hit a ship, you get to keep that missle. If you miss, you will lose the missile you shot with.\n"
              "Good luck!\n\n"
              )

        GB = GameBoard()
        SF = ShipFinder()
        SHV = ShipHitValidation()
        SB = ScoreBoard(15)

        option = 1

        while option != 0:
            total_hits = 0
            score = 0
            ammunition = 10
            ammunition_used = 0
            game_board = GB.create_board()
            internal_board = GB.create_internal_game_board(len(game_board), 0, 0)
            ships = SF.sea_of_ships(internal_board)
            user_coordinates = []

            SB.display_scores()

            player_name = input("\nEnter player name: ")

            while ammunition_used < ammunition:

                GB.print_board(game_board)

                #turn this comment off to see where the ships are for testing purposes
                GB.print_board(internal_board)

                while True:
                    try:
                        while True:
                            x = int(input("Enter row: ")) - 1
                            if 0 <= x < len(game_board):
                                break
                            else:
                                print("Row out of bounds. Please enter a valid row.")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid row.")

                while True:
                    try:
                        while True:
                            y = int(input("Enter column: ")) - 1
                            if 0 <= y < len(game_board):
                                break
                            else:
                                print("Column out of bounds. Please enter a valid column.")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid column.")

                user_coordinate = (x, y)

                if user_coordinate in user_coordinates:
                    print("Coordinate already guessed, try again.")
                    continue

                user_coordinates.append(user_coordinate)

                ship_hit = SHV.validate_ship(user_coordinate, ships)
                ship_sunk = SHV.validate_ship_sunk(user_coordinate, ships)
                game_win = SHV.game_over(ships)

                if ship_hit:
                    total_hits += 1
                    print("Ship hit!")
                    if ship_sunk:
                        score += 1
                        print("Ship sunk!")
                    if game_win:
                        print("Congratulations you have sunk all the ships with " + str(ammunition-ammunition_used) + " missiles.")
                        break
                    print("You still have " + str(ammunition - ammunition_used) + " missiles remaining...")
                else:
                    ammunition_used += 1
                    print("Shot missed!")
                    print("You now have " + str(ammunition - ammunition_used) + " missiles remaining...")

                GB.update_board(game_board, user_coordinate, ship_hit)

            player_node = ScoreNode(player_name, score)
            SB.add_score(player_node)

            print("You lose!\n"
                  "The board reveal is below...")
            GB.print_board(internal_board)

            try:
                while True:
                    option = int(input("Would you like to play again (1: yes, 0: no): "))
                    if 0 <= option <= 1:
                        break
                    else:
                        print("Row out of bounds. Please enter a valid row.")
            except ValueError:
                print("Invalid input. Please enter a valid option.")

        print("Goodbye!")

















