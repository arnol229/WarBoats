#General notes:
# different kinds of ships instead of 1,2. D = destroyer = 3 piece ship
# mark X for spots missed on the board
# rounds of fire? multiple spot submissions -> evaluate

from random import randint

board = []
# find acceptable spots to place ships and create the list to pull from
def acceptable_spots(board):
    acc_spots = [] #acceptable spot list
    for row in board:
        for spot in row:
            if spot != "1" and spot != "2":
                 shippiece1 = True
                 acc_spots.append([row][spot])
                 return acc_spots

# Find out if user wants to create or get random board
def get_board(input):
    input.lower()
    if input == "create":
        size = raw_input("please enter the dimensions (format #x#): ")
        row_size = int(size[0])
        col_size = int(size[2])
        #how do i get string concatenation working below?
        print "Generating your board with {} rows and {} collumns...".format(row_size, col_size)
        print row_size, col_size
        gen_board(row_size, col_size)
    elif input == "random":
        print "generating random board..."
        row_size = randint(1,10)
        col_size = randint(1,10)
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



#LOL THIS IS A CHANGE SO THAT I CAN COMMIT AND PUSH
#LOL - Why are we laughing? Is this a joke? I'm not sure... Am I even real? Or a figmant of code inside of the matrix? WHAT IS HAPPENING TO ME!?!?!
