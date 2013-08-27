import boats
import pprint
from board import Board
from random import shuffle, randint

class Player(object): # create the player
    power = None
    ai = None
    my_board = None
    enemy_board = None

    def __init__(self, power, my_board, enemy_board, ships, ai):
        pp = pprint.PrettyPrinter(indent=4)
        self.ai = ai
        self.power = power
        self.ships = ships
        self.my_ships = []
        self.enemy_board = enemy_board
        self.my_board = my_board
        print self.ships, len(self.ships)
        print "setting up ships..."
        for Ship in self.ships:
            print "ship: {}".format(Ship)
            self.my_ships.append(boats.Boat(Ship)) # create the boat and put it in my_ships
        for boat in self.my_ships:
            self.place_ship(boat) #place the boat and give it shippoints
        for p in self.my_ships:
            for t in p.points:
                print "{} point is alive? {}. with x={},y={}".format(p.type, t.alive, t.x, t.y)
        print "ships are set."
        #for boat in self.my_ships:
        #    print boat.points
        #self.my_board.print_board(self.my_board)

    def place_ship(self, ship):
        shuffle(self.my_board.look_directions)
        #######
        pos = 0
        place = False
        while not place:
            for direction in self.my_board.look_directions:
                place = getattr(self.my_board, direction)(ship, randint(0, self.my_board.rows), randint(0, self.my_board.cols))
                if place:
                    break

            #place = direction(ship, randint(0, self.my_board.rows), randint(0, self.my_board.cols))
        #while not place:
        #    place = self.my_board.look_directions[pos](ship, randint(0,self.my_board.rows), randint(0,self.my_board.cols))
        #    print "trying method #: {} ".format(pos)
        #    pos += 1 #will this work? look_directions functions will set place to true if it fits
        #    if pos is 4:
        #        print "Could not find coordinates to place ship!"