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
import random 
import sys
import time 
##set up a class which declares the main data structure 
class conway:
    def __init__(self, width = 0 , height = 0, string = "", str_input = False, setDefault=True):
        if not str_input:
            self.matrix = []
            self.width = width
            self.height = height
            self.setDefault = setDefault #when there is no set cell input 
            #initialize the grid 
            #set up the matrix
            #computer generated 
            ##draw by arrow keys 
            if self.setDefault:
                for i in range(self.height):
                    horizontal = ""
                    for j in range(self.width):
                        if random.uniform(0, 1) > 0.5:
                            horizontal = horizontal + "█"
                        else:
                            horizontal = horizontal + " "
                            #print a black sqaure 
                            #otheriwse white/empty 
                    self.matrix.append(horizontal)
            else:
                ##self define the board, empty, and call setcell in the test file 
                for i in range(self.height):
                    horizontal = ""
                    for j in range(self.width):
                        horizontal = horizontal + " "
                    self.matrix.append(horizontal)
        else:
            self.matrix = []
            #print("second path is true")
            ##assume input matrix is read line by line 
            horizontal = ""
            for i in string:
                if i != ",":
                    horizontal = horizontal + i
                    # print(i,"new line")
                else:
                    self.matrix.append(horizontal[1:])
                    horizontal = ""
            self.height = len(self.matrix)
            self.width = len(self.matrix[0])
            # print(self.height, "height")
            # print(self.width, "width")


    def setCell(self, x, y):
        self.matrix[y-1] = self.matrix[y-1][:x-1] + "█" + self.matrix[y-1][x:] #change into x-1
        #x <-> width, y <-> height  
        #should be able to set cell whenever the programmer wants 

    def tick(self):
        #implement only once conway rule, only once
        #while true apply the four rules until command C stops the function 
        #Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        #Any live cell with two or three live neighbours lives on to the next generation.
        #Any live cell with more than three live neighbours dies, as if by overpopulation.
        #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        #how to update next generation 
        current_matrix =[]
        for i in range(self.height):
            horizontal = ""
            for j in range(self.width):
                #changed this part to eight directions
                #the strategy to locate neighbors: (i-1, j) upper; (i+1, j) lower; (i, j-1) left; (i, j+1) right
                #(i-1, j-1) left up (i-1, j+1)right up (i+1, j-1) left down (i+1, j+1) right down 
                #错误在不可立马就改到原来的matrix里面
                summation = (j-1 >= 0 and self.matrix[i][j-1] == "█") + (i-1 >= 0 and self.matrix[i-1][j] == "█") +\
                 (i+1 <self.height and self.matrix[i+1][j] == "█") + (j+1 < self.width and self.matrix[i][j+1] == "█")
                summation += (j-1 >= 0 and i-1 >= 0 and self.matrix[i-1][j-1] == "█") + (i-1 >= 0 and j+1 < self.width and self.matrix[i-1][j+1] == "█") + \
                (i+1 <self.height and j-1 >= 0 and self.matrix[i+1][j-1] == "█") + (j+1 < self.width and i+1 <self.height and self.matrix[i+1][j+1] == "█")
                # if i == 2 and j == 2:
                #     print(summation, i , j)
                #     print(j-1 >= 0 and self.matrix[i][j-1] == "█") #left
                #     print(i-1 >= 0 and self.matrix[i-1][j] == "█") #up
                #     print(i+1 <self.height and self.matrix[i+1][j] == "█") #down
                #     print(j+1 < self.width and self.matrix[i][j+1] == "█") #right
                #     print(j-1 >= 0 and i-1 >= 0 and self.matrix[i-1][j-1] == "█") #up left
                #     print(i-1 >= 0 and j+1 < self.width and self.matrix[i-1][j+1] == "█") #up right
                #     print(i+1 <self.height and j-1 >= 0 and self.matrix[i+1][j-1] == "█") #left down 
                #     print(j+1 < self.width and i+1 <self.height and self.matrix[i+1][j+1] == "█") #right down 
                if self.matrix[i][j] == "█":
                    #live < 2 or > 3
                    if summation < 2 or summation >3:
                        horizontal = horizontal + " "
                        #self.matrix[i] = self.matrix[i][:j] + " " + self.matrix[i][j+1:]
                    else:
                        horizontal = horizontal + "█"
                else:
                    #dead exactly 3
                    if summation ==3:
                        horizontal = horizontal + "█"
                    else:
                        horizontal = horizontal + " "
                        #self.matrix[i] = self.matrix[i][:j] + "█" + self.matrix[i][j+1:]
            current_matrix.append(horizontal)
        self.matrix = current_matrix
        print("excuted")
        #self.draw_conway() this part should be also done in the test file 
        #time.sleep(1.0) test file should be in control of this 

    def string(self, size=1, show_border=True):
        #only return string object 
        #size:2, 0.5 and 0.125, default 1 
        #size means print scales
        #show_boarder:whether to implement borders like print("┌" + "─" * (self.width) + "┐")
        #print("┌" + "─" * (self.width) + "┐")
        #print("└" + "─" * (self.width) + "┘")
        #print result section 
        if show_border:
            thisStr = ""
            thisStr += "┌" + "─" * (self.width) + "┐\n"
            for i in self.matrix:
                thisStr += "│" + i + "│\n"
            thisStr += "└" + "─" * (self.width) + "┘"
            return thisStr
        else:
            thisStr = ""
            for i in self.matrix:
                thisStr += i + "\n"
            return thisStr


        

        ##randomly generate live and death cells
        #print(*matrix, sep='\n')



##python main function 

if __name__ == "__main__":
    #print here 
    #should be something it will be when we run in the terminal 
    _, width, height = sys.argv
    width = int(width)
    height = int(height)
    test_obj = conway(width,height) 
    #print("┌" + "─" * (self.width) + "┐")
    #for i in test_obj.string():
    print(test_obj.string()) #print the innitial image 
    #print("└" + "─" * (self.width) + "┘")
    while True:
        print('\033[' + str(test_obj.height+3) + 'F')
        test_obj.tick() #only apply once conway rule 
        #print("┌" + "─" * (self.width) + "┐")
        print(test_obj.string()) #only print once after the matrix is changed 
        #print("└" + "─" * (self.width) + "┘")
        time.sleep(1.0) #to make sure the image is printed every second 









