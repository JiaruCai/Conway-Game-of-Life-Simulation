#
# Usage: python3 Conway.py width height
# Generates a width by height board with random live/dead cells and prints a new step every second
#
# Game board should print like:
# _____________________
# |     █████         |
# |   █   █ ██        |
# | ███  █ █  ███     |
# | ████              |
# ---------------------
#
#upper bound _
#lower bound -

##set up a class which declares the main data structure 
import random 
def conway_rule(width, height):
    #initialize the grid 
    matrix = []
    #set up the matrix
    for i in range(height):
        horizontal = ""
        for j in range(width):
            if random.uniform(0, 1) > 0.5:
                horizontal = horizontal + "█"
            else:
                horizontal = horizontal + " "
                #print a black sqaure 
                #otheriwse white/empty 
        matrix.append(horizontal)
    draw_conway(matrix, width, height)
    #while true apply the four rules until command C stops the function 
    #Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    #Any live cell with two or three live neighbours lives on to the next generation.
    #Any live cell with more than three live neighbours dies, as if by overpopulation.
    #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    import time
    while True:
        #how to update next generation 
        for i in range(height):
            for j in range(width):
                #changed this part to eight directions
                #the strategy to locate neighbors: (i-1, j) upper; (i+1, j) lower; (i, j-1) left; (i, j+1) right
                #(i-1, j-1) left up (i-1, j+1)right up (i+1, j-1) left down (i+1, j+1) right down 
                summation = (j-1 >= 0 and matrix[i][j-1] == "█") + (i-1 >= 0 and matrix[i-1][j] == "█") + (i+1 <height and matrix[i+1][j] == "█") + (j+1 < width and matrix[i][j+1] == "█")
                summation += (j-1 >= 0 and i-1 >= 0 and matrix[i-1][j-1] == "█") + (i-1 >= 0 and j+1 < width and matrix[i-1][j+1] == "█") + \
                (i+1 <height and j-1 >= 0 and matrix[i+1][j-1] == "█") + (j+1 < width and i+1 <height and matrix[i+1][j+1] == "█")
                if matrix[i][j] == "█":
                    #live < 2 or > 3
                    if summation < 2 or summation >3:
                        matrix[i] = matrix[i][:j] + " " + matrix[i][j+1:]
                else:
                    #dead exactly 3
                    if summation ==3:
                        matrix[i] = matrix[i][:j] + "█" + matrix[i][j+1:]
        draw_conway(matrix, width, height)
        time.sleep(1.0)




first_time = True 
def draw_conway(matrix, width, height):
    global first_time
    if not first_time:
        string = str(height+3)
        print('\033[' + string + 'F')
    first_time = False

    print("┌" + "─" * (width) + "┐")
    #print result section 
    for i in matrix:
        print("│" + i + "│" , sep='\n')
    print("└" + "─" * (width) + "┘")

    ##randomly generate live and death cells
    #print(*matrix, sep='\n')


import sys
_, width, height = sys.argv
width = int(width)
height = int(height)
conway_rule(width, height)




