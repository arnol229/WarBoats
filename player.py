import boats
from board import Board
from random import shuffle, randint

class Player(object): # create the player
    power = None
    ai = None
    my_board = None
    enemy_board = None

    def __init__(self, power, my_board, enemy_board, ships, ai):
        #do we still need enemy_board?
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
        for boat in self.my_ships:
            for point in boat.points:
                self.my_board.board[point.x -1][point.y -1] = boat.id
                # -1 on the points because the board starts at 1. not 0. 

        print "ships are set."

    def place_ship(self, ship):
        shuffle(self.my_board.look_directions)
        #######
        pos = 0
        place = False
        while not place:
            for direction in self.my_board.look_directions:
                place = getattr(self.my_board, direction)(ship, randint(1, self.my_board.rows), randint(1, self.my_board.cols))
                if place:
                    break