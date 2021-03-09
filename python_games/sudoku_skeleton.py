import copy
########################################### This function reads in block from file 
def grid_from_file(file_name):
    lst=[]
    f=open(file_name)
    for line in f:
        lst2=[]
        for i in line:
            if i == "x":
                lst2.append(i)
            elif i.isdigit():
                lst2.append(int(i))
        lst.append(lst2)
    return lst

##################################################
def subgrid_values(grid, row, col):
    val = []
    #get dimension of inner box
    n = int(len(grid)**(0.5))
    #get starting row and starting col
    r = (row//n)*n
    c = (col//n)*n 
    for i in range(r, r+n):
        for j in range(c, c+n):
            val.append(grid[i][j])       
    return val
# This returns a list of values in the subgrid
def column_values(grid,col):
    val=[]
    n=len(grid)
    for i in range(n):
        val.append(grid[i][col])
    return val
#This returns a list of values in the column
def row_values(grid,row):
    val=[]
    n=len(grid)
    for i in range(n):
        val.append(grid[row][i])
    return val
#This returns a list of values in the row
#################################################

def valid_entry(grid,num,r,c):
    check1=num not in column_values(grid,c)
    check2=num not in row_values(grid,r)
    check3=num not in subgrid_values(grid,r,c)
    if check1 and check2 and check3:
        return True
    return False
###################################################
def grids_augmented_in_row(grid,num,r):
    #Write code here
#################################################### This should recursively use the function above to                 
def grids_augmented_with_number(grid,num): 
    #Write code here
#################################################### This should recursively use the function above to complete the sudoku puzzle.
def solve_sudoku(file_name):
    #Write code here
#################################################### this makes a function that chooses sudoku block based of numbers
def block_selector(number):
    if number==1:
        return "gridA.txt"
    elif number==2:
        return "gridB.txt"
    elif number==3:
        return "gridC.txt"
    elif number==4:
        return "gridD.txt"
    elif number==5:
        return "gridE.txt"
    elif number==6:
        return "gridF.txt"
    else:
        return Null
#################################################### this solves the block, change number variable to swap blocks
number=6
print(solve_sudoku(block_selector(number)))
