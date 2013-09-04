import boats
from board import Board
from random import shuffle, randint

class Player(object): # create the player
    power = None
    ai = None
    my_board = None
    enemy_board = None

    def __init__(self, power, my_board, enemy_board, ships, ID):
        #do we still need enemy_board?
        self.id = ID
        self.power = power
        self.ships = ships
        self.cooldown = []
        self.my_ships = [self.cooldown,]
        self.dead_boats = []
        self.enemy_board = enemy_board
        self.my_board = my_board
        print self.ships, len(self.ships)
        print "setting up ships..."
        for Ship in self.ships:
            print "ship: {}".format(Ship)
            if Ship is "Destroyer":
                self.my_ships.append(boats.Destroyer())
                continue
            if Ship is "Cruiser":
                self.my_ships.append(boats.Cruiser())
                continue
            if Ship is "WarBoat":
                self.my_ships.append(boats.WarBoat())# create the boat and put it in my_ships
                continue
        print len(self.my_ships)
        for boat in self.my_ships:
            if type(boat) is list:
                for cdboat in boat:
                    self.place_ship(cdboat) #place the boat and give it shippoints
            else:
                self.place_ship(boat)
        for boat in self.my_ships:
            if type(boat) is list:
                for cdboat in boat:
                    for point in boat.points:
                        self.my_board.board[point.x-1][point.y-1] = cdboat.id
            else:
                for point in boat.points:
                    self.my_board.board[point.x-1][point.y-1] = boat.id
        print "ships are set."

    def place_ship(self, ship):
        shuffle(self.my_board.look_directions)
        pos = 0
        place = False
        while not place:
            for direction in self.my_board.look_directions:
                place = getattr(self.my_board, direction)(ship, randint(1, self.my_board.rows), randint(1, self.my_board.cols))
                if place:
                    break

    def refresh_ships(self):
        for ship in self.cooldown:
            if ship.energy is ship.cooldown:
                self.my_ships.append(self.cooldown.pop(index(ship)))
            else:
                ship.energy += 1