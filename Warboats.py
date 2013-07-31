#General notes:
# different kinds of ships instead of 1,2. D = destroyer = 3 piece ship
# mark X for spots missed on the board
# rounds of fire? multiple spot submissions -> evaluate

from random import randint

board = []
# find acceptable spots to place ships and create the list to pull from
# def acceptable_spots(board):
#     acc_spots = [] #acceptable spot list
#     for row in board:
#         for col in row:
#             while col == "O":
# # I want this loop to check every if.. this might be an infinite loop right now?
#                 if col+1 == "O"
#                     acc_spots.append([row][col],[row][col+1])
#                     continue
#                 elif col-1 == "O":
#                     acc_spots.append([row][col],[row][col-1])
#                     continue
#                 elif row+1 == "O":
#                     acc_spots.append([row][col],[row+1][col])
#                     continue
#                 elif row-1 == "O":
#                     acc_spots.append([row][col],[row+1][col])
#                     break

#     return acc_spots

# Robert's acceptable spots Algo
# Step 1 - get board size
# Step 2 - go row by row and append all spots
def roberts_spot_algorithm(row_size, col_size):
    print 'Board Size: {0}x{1}'.format(row_size, col_size)
    spots = []
    for row in range(row_size):
        x = row
        for col in range(col_size):
            y = col

            # so we have our starting point of
            # (x,y) now we need to find the next point for a 2x1 piece
            # vertical and horizontal
            anchor_point = (x,y,)
            if x - 1 > 0:
                # checking if the piece can go vertically up 1 spot
                spots.append((anchor_point, (x-1, y,),))
            if x + 1 < row_size:
                # checking to see if piece can go vertically down 1 spot
                spots.append((anchor_point, (x+1, y,),))
            if y - 1 > 0:
                # checking to see if piece can go horizontally left 1 spot
                spots.append((anchor_point, (x, y-1,),))
            if y + 1 < col_size:
                # checking to see if piece can go horizontally right 1 spot
                spots.append((anchor_point, (x, y + 1,),))

    return spots

#pprint = pretty print
import pprint
roberts_test = roberts_spot_algorithm(3,3)
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(roberts_test)

# Find out if user wants to create or get random board
def get_board(input):
    input.lower()
    if input == "create":
        size = raw_input("please enter the dimensions (format #x#): ")
        row_size = int(size[0])
        col_size = int(size[2])
        print "Generating your board with {} rows and {} collumns...".format(row_size, col_size)
        print row_size, col_size
        gen_board(row_size, col_size)
    elif input == "random":
        print "generating random board..."
        row_size = randint(3,10)
        col_size = randint(3,10)
        gen_board(row_size, col_size)
        print row_size, col_size
    else:
        get_board(str(raw_input("error, please retry : Create / Random: ")))


# generate the initial board
def gen_board(rows, cols):
    for row in range(rows):
        board.append(["O"] * cols)
    print_board(board)


#Print board function
# Why is this printing so many rows? maybe problem is in gen_board?
def print_board(board):
    for row in board:
        col_list = []
        for col in row:
            col_list.append(col)
        print " ".join(col_list)

# place ship will call acceptable_spots to find valid places to put ships
# after choosing a certain spot, it must then remove the spot from acc_spots
# and then redefine acc_spots, accounting for the taken spot
# Do i need another function to handle that? or can that be taken care of here
# def place_ship():

get_board(str(raw_input("please choose : Create / Random: ")))