#Main File
from player import Player
from board import Board
from game import Game
from boats import Boat
from random import randint
# login = False
# 
# while not login:
#   intial LOGIN
#   - if successful, login = True
# 
# if login == True: 
running = True
rows = None
cols = None
ships = []
while running:
    print """
Main Menu:
1.New Game
2.Change login
3.About (how to Play)
4.Credits
5.Exit
    """
    command = int(input("Choice #: "))

    if command is 1: 
        rows = 0
        cols = 0
        board_size = input("""
Board Size
1. 8x8
2. 4x4
Please choose:""")
        if board_size is 2:
            rows = 4
            cols = 4
            ships = ["Destroyer", "Cruiser", "WarBoat"]
            print ships
        if board_size is 1:
            rows = 8
            cols = 8
            ships = ["Destroyer", "Destroyer", "Destroyer", "Cruiser", "Cruiser", "WarBoat", "WarBoat"]
            print ships
        players = input("How many players? (1 or 2)")
        if players is 1:
            power1 = input("""
Super Powers!
0. No Powers
1. Radar
2. Super Gun
3. Deflector Shield
    Please Choose: """)
            power2 = randint(0,3)
            Player1 = Player(power1, Board(rows,cols), Board(rows, cols), ships, 1)
            Player2 = Player(power2, Board(rows,cols), Board(rows, cols), ships, 2)
            winner = None
            Game(Player1, Player2)
        if players is 2:
            power1 = input("""
Super Powers!(Player 1)
0. No Powers
1. Radar
2. Super Gun
3. Deflector Shield
    Please Choose: """)
            power2 = input("""
Super Powers!(Player 2)
0. No Powers
1. Radar
2. Super Gun
3. Deflector Shield
    Please Choose: """)
            player1 = Player(power1, Board(rows,cols), Board(rows, cols), ships, 1)
            player2 = Player(power2, Board(rows,cols), Board(rows, cols), ships, 2)
            Game(player1, player2)
                # Creates a game (Player 1 with his power, 2 boards(his and enemies), ships to put on the board, and not AI
                # Player2 passing the same elements
    elif command is 2:
        #self.login = Authentication()
        pass
    elif command is 3:
        #display howtoplay.txt
        pass
    
    elif command is 4:
        print """
        made by bo arnold
        email: arnol229@gmail.com
        """
    elif command is 5:
        print "goodbye!"
        running = False

    else:
        print "Error!"