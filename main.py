# 0s will be placeholders for empty slots
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10): # loop through values 1-9
        if valid(bo, i, (row,col)): # check if that value is valid
            bo[row][col] = i # num is valid -> insert that value into slot

            if solve(bo):
                return True

            # backtrack and reset the last element because it is not actually correct
            bo[row][col] = 0

    # if looped through all the values and is all invalid
    return False



def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        # check through each row i to see if the number is already there NOT including the slot that the num was just inserted into
        if bo[pos[0]][i] == num and pos[1] != i:
            return False # found that number in row -> so invalid option

    # Check column
    for i in range(len(bo)):
        # check through each column i to see if the number is already there NOT including the spot the num was inserted into
        if bo[i][pos[1]]== num and pos[0] != i:
            return False; # found that number in column -> so invalid option

    # Check the 3x3 square it's in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                # Check to see if that num already exists NOT inlcuding the spot it was just inserted in
                if bo[i][j] == num and (i,j) != pos:
                    return False # num does exist

    # All the checks went through -> since none returned false means valid option
    return True

# for a visual output
def print_board(bo):
    # after every 3 rows, print the border
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
    # after every 3 columns print the border
        for j in range(len(bo[0])):
            # the j != 0 is for the condition where it's in the beginning
            if j % 3 == 0 and j != 0:
                # end="" is so that it doesn't print a /n
                print(" | ", end ="")

            if j == 8:
                 print(bo[i][j])
            else:
                 print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    # check each row
    for i in range(len(bo)):
        # check each column
        for j in range(len(bo)):
            # if there is an empty slot (0) in that position
            if bo[i][j] == 0:
                # return that position (row,col)
                return (i,j)

    # if there are no empty slots (0s)
    return None


print_board(board)
solve(board)
print ("\nSOLVED BOARD")
print_board(board)