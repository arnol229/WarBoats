import boats
from random import shuffle, randint

class Player(object): # create the player
    power = None
    ai = None
    my_board = None
    enemy_board = None

    def __init__(self, power, my_board, enemy_board, ships, ai):
        self.ai = ai
        self.power = power
        self.ships = ships
        self.enemy_board = enemy_board
        self.my_board = my_board
        print self.ships, len(self.ships)
        print "setting up ships..."
        for Ship in self.ships:
            print "ship: {}".format(Ship)
            self.place_ship(boats.Boat(Ship))
        print "ships are set."
        #self.my_board.print_board(self.my_board)

    def place_ship(self, ship):
        shuffle(self.my_board.look_options)
        #######
        ship_spot = []
        pos = 0
        place = False
        for direction in self.my_board.look_options:
            place = direction(ship, randint(0, self.my_board.rows), randint(0, self.my_board.cols))
        #while not place:
        #    place = self.my_board.look_options[pos](ship, randint(0,self.my_board.rows), randint(0,self.my_board.cols))
        #    print "trying method #: {} ".format(pos)
        #    pos += 1 #will this work? lookoption functions will set place to true if it fits
        #    if pos is 4:
        #        print "Could not find coordinates to place ship!"