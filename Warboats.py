#Main File
import Player
import Board
import Game
import Boats
# login = False
# 
# while login == False:
#   intial LOGIN
#   - if successful, login = True
# 
# if login == True: 
run = True
rows = None
cols = None

while run == True:
    print """
Main Menu:
1.New Game
2.Change login
3.About (how to Play)
4.Credits
5.Exit
    """
    command = int(input("Choice #: "))

    if command == 1: 
        rows = 0
        cols = 0
        BoardSize = raw_input("""Board Size
            1. 8x8
            2. 4x4
            Please choose:""")
        if BoardSize == 1:
            rows = 4
            cols = 4
        if BoardSize == 2:
            rows = 8
            cols = 8
        if BoardSize != 1 and BoardSize != 2:
            print "you dun fucked up now, boy"
        Players = input("How many players? (1 or 2)")
        if Players == 1:
            Power = input("""Super Powers!
            0. No Powers
            1. Radar
            2. Super Gun
            3. Deflector Shield
    
            """)

            Ships = input("How many ships?: ")

            Game.Game((Player(Power, Board(rows, cols), Board(rows, cols), Ships, False)), (Player(randint(0,3), Board(rows, cols), Board(rows, cols), Ships, True)))
        if Players == 2:
            Power1 = input("""Super Powers!(Player1)
            0. No Powers
            1. Radar
            2. Super Gun
            3. Deflector Shield
    
            """)
            Power2 = input("""Super Powers!(Player2)
            0. No Powers
            1. Radar
            2. Super Gun
            3. Deflector Shield
    
            """)
            Ships = input("How many Ships?(please consider the map size): ")
            #Board = Board.Board(rows, cols)
            Player1 = Player.Player(Power1, Board.Board(rows,cols), Board.Board(rows, cols), Ships, False)
            Player2 = Player.Player(Power2, Board.Board(rows,cols), Board.Board(rows, cols), Ships, False)
            Game.Game(Player1, Player2)
                # Creates a game (Player 1 with his power, 2 boards(his and enemies), ships to put on the board, and not AI
                # Player2 passing the same elements
    if command == 2:
        #self.login = Authentication()
        pass
    if command == 3:
        #display howtoplay.txt
        pass
    
    if command == 4:
        print """
        made by bo arnold
        email: arnol229@gmail.com
        """
    if command == 5:
        run = False

    else:
        print "Error!"