from Ship import *

class ShipFinder(object):

    #helper function to traverse board
    #uses DFS method to traverse the game_board passed in to find the entire 'ship' that the passed in (x,y) coordinate is part of
    #and then returns the root node of the linked list of nodes
    def traverseBoard(self, x, y, game_board, coordinate_to_ship_map, ship_num, visited):

        #Depth First Search

        stack = [(x, y)]
        size = 0
        rows = len(game_board)
        cols = len(game_board)

        ships = []

        ship = None

        while len(stack) > 0:
            x, y = stack.pop()
            new_ship = Ship((x, y))

            if visited[x][y]:
                continue

            visited[x][y] = True

            if game_board[x][y] != "*":
                continue

            if ship is not None:
                ship.next_ship = new_ship

            coordinate_to_ship_map.update({(x, y): ship_num})

            #add adjacent elements to stack, and not going out of bounds

            if x + 1 < rows and game_board[x+1][y]:
                stack.append([x+1, y])
            if x - 1 >= 0 and game_board[x-1][y]:
                stack.append([x-1, y])
            if y + 1 < cols and game_board[x][y+1]:
                stack.append([x, y+1])
            if y - 1 >= 0 and game_board[x][y-1]:
                stack.append([x, y-1])

            ship = new_ship
            ships.append(ship)
            size += 1

        # ships connected so want to return the first ship of the connected nodes, the root ship
        if size > 0:
            return ships[0]


    #this adds the root nodes found when traversing the board from each node through DFS
    #returns the dictionary that maps each coordinate to the ship it belongs to
    #using the ship each coordinate belongs to, places the root ship node at that index in an array
    #this function then returns the coordinate map and the array of linked lists for each ship
    def sea_of_ships(self, game_board):

        sea_of_ships = []

        #this is a map to map coordinates to the ship they belong to
        coordinate_to_ship_map = {}
        visited = [[False for i in game_board[0]] for _ in game_board[0]]
        ship_num = 0

        for x in range(len(game_board)):
            for y in range(len(game_board)):
                if visited[x][y]:
                    continue
                root_ship = self.traverseBoard(x, y, game_board, coordinate_to_ship_map, ship_num, visited)

                if root_ship is not None:
                    coordinate = root_ship.coordinate
                    index = coordinate_to_ship_map.get(coordinate)

                    #this is creating hashmap
                    sea_of_ships.insert(index, root_ship)

                    ship_num += 1

        return [coordinate_to_ship_map, sea_of_ships]





