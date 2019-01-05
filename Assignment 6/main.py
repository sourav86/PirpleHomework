"""
Assignment #6 : Advance Loop - Draw Playing Board
"""

#Create function to display playing board
def drawPlayingBoard(row,col):
# Validating input row and column value against maximum width and height of terminal.
    if row <=120 and col <=120:
        for r in range(1,row+1):
            if r%2 != 0:
                for c in range(col):
                    if c%2 == 0:
                        if c != col-1:
                            print(" ",end="")
                    else:
                            print("|",end="")
                else:
                    print("")
            else:
                print("-"*col)

        print(True)
    else:
        print(False)

#Execute the function with row = 20 and column = 20
drawPlayingBoard(20,20)