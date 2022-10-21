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

print_board(board)