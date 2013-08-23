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
        #self.MyBoard.print_board(self.MyBoard)

    def place_ship(self, ship):
        shuffle(self.MyBoard.lookoptions)
        #######
        pos = 0
        place = False
        while place == False:
            self.MyBoard.lookoptions[pos](ship, randint(0,WarBoats.rows), randint(0,Warboats.cols))
            pos += 1 #will this work? lookoption functions will set place to true if it fits