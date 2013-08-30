class Play(object): # Create a game. save these objects to pull up a match history?
    Winner = None
    rows = None
    cols = None
    Player1 = None
    Player2 = None

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player_list=[self.player1, self.player2]
        #below: check for ShipPoints on a boat objects on the player
        for player in self.player_list:
            player.my_board.print_board(player.my_board.board)
            for boat in player.my_ships:
                for point in boat.points:
                    print "{} point is alive? {}. with x={},y={}".format(boat.type, point.alive, point.x, point.y)

    #    Battle(player1, player2)
    #def battle(self, player1, player2): #the stage for fighting. scroll through firing, assessing dmg, using power
    #    while self.Winner == False:
    #        self.exchange()

    #def exchange(self): #how to design firing? ships have multiple cannons?
    #   if user fire input matches a ShipPoint x and y:
    #       replace x,y on board with "x"
    #   else:
    #       replace x,y with "~"
    #def check_winner(self): #check board.ship_points for quicker determination
    #def check_boat(self, boat):#same as is_alive on the boat? dont think i need...

    # firing idea:
    # each player scroll through and fire with a type of ship (d, then c, then wb) wb have 2 cannons?