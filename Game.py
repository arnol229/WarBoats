class Play(object): # Create a game. save these objects to pull up a match history?
    Winner = None
    rows = None
    cols = None
    Player1 = None
    Player2 = None

    def __init__(self, Player1, Player2):
        self.Player1 = Player1
        self.Player2 = Player2
        self.Player1.MyBoard.print_board()
        #print self.Player1.Ships
        #print self.Player2.Ships
        #self.player1.EnemyBoard = Board.GiveBoard(self.Player2.MyBoard) 
        #Battle(Player1, Player2)
    #def battle():
        #while self.Winner == False:
            #self.fire()

    #def fire():
    #def check_winner():