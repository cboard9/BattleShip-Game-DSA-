class ShipHitValidation(object):

    #check to see if target coordinate is a * (or a 'ship' in this game) the sea_of_ships if the output from the function
    #that contains a list of two elements, the first being a dictionary that maps a * coordinate to the 'ship' it belongs to
    #the second element is a list of Ship objects. Each Ship object is the root node in a linked list pointing to all coordinates
    #associated with that ship
    def validate_ship(self, coordinate, sea_of_ships):

        coordinates = sea_of_ships[0]
        ships = sea_of_ships[1]

        ship_num = coordinates.get(coordinate)

        if ship_num is not None:
            root_ship = ships[ship_num]
            if root_ship.coordinate == coordinate:
                ships[ship_num] = root_ship.next_ship
                return True
            else:
                current_ship = root_ship
                ship = current_ship.next_ship
                while True:
                    if ship.coordinate == coordinate:
                        current_ship.next_ship = ship.next_ship
                        return True
                    current_ship = ship
                    ship = ship.next_ship

    #check to see if entire ship connected to target coordinate has been hit
    #if the element in the ship location is None then nothing is left of that ship and it can be considered 'sunk'
    def validate_ship_sunk(self, coordinate, sea_of_ships):

        coordinates = sea_of_ships[0]
        ships = sea_of_ships[1]

        ship_num = coordinates.get(coordinate)

        if ship_num is not None and ships[ship_num] is None:
            return True

        return False

    #checks if ever ship has been sunk. if so then user has found them all and user has won
    def game_over(self, sea_of_ships):
        for ship in sea_of_ships[1]:
            if ship is not None:
                return False

        return True

