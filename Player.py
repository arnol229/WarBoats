class Player(object): # create the player
    Ships = None
    Power = None
    AI = None
    MyBoard = None
    EnemyBoard = None

    def __init__(self, Power, MyBoard, EnemyBoard, Ships, AI):
        self.AI = AI
        self.Power = Power
        self.Ships = Ships
        self.EnemyBoard = EnemyBoard
        self.MyBoard = MyBoard
        #print self.Ships
        for Ship in self.Ships:
            print "ship:", Ship
            place_ship(Boats.Boat(Ship))
        #self.MyBoard.print_board(self.MyBoard)

    def place_ship(self, ship):
        shuffle(self.MyBoard.lookoptions)
        #######
        ShipSpot = []
        pos = 0
        place = False
        while place == False:
            place = self.MyBoard.lookoptions[pos](ship, randint(0,WarBoats.rows), randint(0,Warboats.cols))
            print "trying method #: ", pos
            pos += 1 #will this work? lookoption functions will set place to true if it fits
            if pos == 4:
                print "Could not find coordinates to place ship!"