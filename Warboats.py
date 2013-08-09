#General notes:
# different kinds of ships instead of 1,2. D = destroyer = 3 piece ship
# mark X for spots missed on the board
# rounds of fire? multiple spot submissions -> evaluate
import time
import random
import pprint

pp = pprint.PrettyPrinter(depth=6)
board = []
open_spots = []
ship_count = 0
ship_pos = []
# Robert's acceptable spots Algo
# Step 1 - get board size
# Step 2 - go row by row and append all spots
def acceptable_spots(row_size, col_size):
    print 'Board Size: {0}x{1}'.format(row_size, col_size)
    for row in range(row_size):
        x = row
        for col in range(col_size):
            y = col
            # so we have our starting point of
            # (x,y) now we need to find the next point for a 2x1 piece
            # vertical and horizontal
            anchor_point = (x,y,)
            if x - 1 >= 0:
                # checking if the piece can go vertically up 1 spot
                open_spots.append((anchor_point, (x-1, y,),))
            if x + 1 <= row_size:
                # checking to see if piece can go vertically down 1 spot
                open_spots.append((anchor_point, (x+1, y,),))
            if y - 1 >= 0:
                # checking to see if piece can go horizontally left 1 spot
                open_spots.append((anchor_point, (x, y-1,),))
            if y + 1 <= col_size:
                # checking to see if piece can go horizontally right 1 spot
                open_spots.append((anchor_point, (x, y + 1,),))
    #for spots in open_spots:
        #print "spot:" , spots

# Find out if user wants to create or get random board
def get_board(input):
    input.lower()
    if input == "create":
        size = raw_input("please enter the dimensions (format #x#): ")
        row_size = int(size[0])
        col_size = int(size[2])
        print "Generating your board with {} rows and {} collumns...".format(row_size, col_size)
        gen_board(row_size, col_size)
        open_spots = acceptable_spots(row_size, col_size)
        #ship_count = (int(raw_input("How many ships?")))
        return open_spots
        #print row_size, col_size
    elif input == "random":
        print "generating random board..."
        row_size = random.randint(3,10)
        col_size = random.randint(3,10)
        gen_board(row_size, col_size)
        open_spots = acceptable_spots(row_size, col_size)
        #ship_count = (int(raw_input("How many ships?")))
        return open_spots
        #print row_size, col_size
    else:
        get_board(str(raw_input("error, please retry : Create / Random: ")))


# generate the initial board
def gen_board(rows, cols):
    for row in range(rows):
        board.append(["O"] * cols)
    print_board(board)


#Print board function
def print_board(board):
    for row in board:
        col_list = []
        for col in row:
            col_list.append(col)
        print " ".join(col_list)

def remove_spots(open_spots, ship):
    xy1, xy2 = ship
    indexes = []
    counter = 0
    for coord in open_spots:
        if xy1 == coord[0] or xy1 == coord[1] or xy2 == coord[0] or xy2 == coord[1]:
            indexes.append(open_spots.index(coord))
            popped = open_spots.pop(open_spots.index(coord))
            #print "coordinate {0} popped!".format(popped)
    for i in indexes:
        gone = open_spots.pop(i - counter)
        #print "we got rid of: ", gone
        counter += 1

def place_ship(ship_count,open_spots):
    #print "open spots: "
    #pp.pprint(open_spots)
    while ship_count != 0:
        ship = random.choice(open_spots)
        remove_spots(open_spots, ship)
        ship_pos.append(ship)
        print "ship #{}: {}".format(ship_count, ship)
        for xy in ship:
            board[xy[0]][xy[1]] = "{}".format(ship_count)
            print_board(board)
        ship_count -= 1
        #print "open spots: "
        #pp.pprint(open_spots)

#def fire(input):
print """

WAR BOATS!

"""
time.sleep(1)
print """The Deadliest game known to man!

"""
time.sleep(2)
def main_menu():
    print """Main Menu

    1. Play vs Comp
    2. 2 Player
    3. Settings
    4. Credits
    5. Quit"""
    choice = int(raw_input("What would you like to do?: "))
    if choice == 1:
        get_board(raw_input("please choose : Create / Random: ").lower())
    elif choice == 2:
        print """

        this aint done yet, son.

        """
        time.sleep(1)
        main_menu()
    elif choice == 3:
        print """

        this aint done yet, son.

        """
        time.sleep(1)
        main_menu()
    elif choice == 4:
        print """

        Developed by Bo Arnold
        Email: arnol229@gmail.com
        
        """
        time.sleep(1)
        main_menu()
    elif choice == 5:
        print "Goodbye!"
    else:
        print """

        ERROR: please enter a valid choice.
        
        """
        time.sleep(1)
        main_menu()

#### START ####

main_menu()
#get_board(str(raw_input("please choose : Create / Random: ")))
ship_count = (int(raw_input("How many ships?")))
place_ship(ship_count, open_spots)

print "ship position(s): "
pp.pprint(ship_pos)
#print "remaining open_spots:"
#pp.pprint(open_spots)
print_board(board)
main_menu()