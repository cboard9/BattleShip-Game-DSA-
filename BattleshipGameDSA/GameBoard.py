import random

class GameBoard(object):

    #returns a random empty matrix
    def create_board(self):

        ##can randomize the game board size but for consistency it has been standarized to size 10x10
        size = random.randint(10, 10)
        blank_board = [[i for i in range(1, size+1)] for _ in range(0, size)]
        return blank_board

    #returns a matrix with * (or 'ships' in this game) randomly placed throughout the graph
    def create_internal_game_board(self, size, x, y):

        amount_of_ships = [True, False, False, False]                   #amount of ships placed will be 25% of the size of the board

        internal_board = [[i for i in range(1, size+1)] for _ in range(0, size)]

        visited = []
        stack = []

        stack.append((x, y))
        visited.append((x, y))

        while len(stack) > 0:
            cell = []

            if(x + 1, y) not in visited and x + 1 < size:   #is right available? then add to cell list
                cell.append("R")

            if (x - 1, y) not in visited and x - 1 >= 0:  #is left available? then add to cell list
                cell.append("L")

            if (x, y + 1) not in visited and y + 1 < size:  #is up available? then add to cell list
                cell.append("U")

            if (x, y - 1) not in visited and y - 1 >= 0:  #is down available? then add to cell list
                cell.append("D")

            if len(cell) > 0:
                cell_chosen = random.choice(cell)                     #check if cell list empty and randomly choose where to go

                if cell_chosen == "R":
                    x += 1
                    visited.append((x, y))                               #make this cell current cell and mark as visited
                    stack.append((x, y))                                 #add this new current cell to the stack
                    if random.choice(amount_of_ships):
                        internal_board[x][y] = "*"

                elif cell_chosen == "L":
                    x -= 1
                    visited.append((x, y))
                    stack.append((x, y))
                    if random.choice(amount_of_ships):
                        internal_board[x][y] = "*"

                elif cell_chosen == "U":
                    y += 1
                    visited.append((x, y))
                    stack.append((x, y))
                    if random.choice(amount_of_ships):
                        internal_board[x][y] = "*"

                elif cell_chosen == "D":
                    y -= 1
                    visited.append((x, y))
                    stack.append((x, y))
                    if random.choice(amount_of_ships):
                        internal_board[x][y] = "*"

            else:
                x, y = stack.pop()                                  #if no cells available, pop one from the stack (backtracking)

        return internal_board

    #updates the 'game_board' matrix passed in at the coordinate passed in and marks it depending on the 'hit_or_miss' boolean passed in
    def update_board(self, game_board, coordinate, hit_or_miss):
        x, y = coordinate

        if hit_or_miss:
            game_board[x][y] = "*"
        else:
            game_board[x][y] = "X"

    #prints the game board in readable format for the user
    def print_board(self, game_board):

        str_board = ""

        for row_num in range(1, len(game_board)+1):
            str_board += "Row " + str(row_num) + ": | "
            for col_num in range(0, len(game_board)):
                str_board += str(game_board[row_num-1][col_num]) + " | "
            str_board += "\n"

        print(str_board)




