
##############################################Part A: Get Grid #############################################

def grid_from_file(file_name):
    grid = []
    f = open(file_name)
    for row in f:
        rows = []
        for column in row:
            if column.isdigit():
                # rows.append(column)
                rows.append(int(column))
            elif column.isalnum():
                rows.append(column)
        grid.append(rows)
    return grid

##############################################Part B: Valid Entry #############################################

def subgrid_values(grid, row, col):
    val = []
    # get dimension of inner box
    n = int(len(grid) ** (0.5))
    # #get starting row and starting col
    r = (row // n) * n
    c = (col // n) * n
    for i in range(r, r + n):
        for j in range(c, c + n):
            val.append(grid[i][j])
    return val


def valid_entry(grid, num, r, c):
    check = True
    # rowCheck
    for i in range(len(grid)):
        if grid[r][i] != num:
            check = True
        else:
            check = False
            return check
    # colCheck
    for j in range(len(grid)):
        if grid[j][c] != num:
            check = True
        else:
            check = False
            return check
    # SUBGRID
    subgrid = subgrid_values(grid, r, c)
    subgrid_leng = len(subgrid)
    for i in range(subgrid_leng):
        if subgrid[i] != num:
            check = True
        else:
            check = False
            return check
    # returning the check after checking rows, columns and or subgrid
    return check


##############################################Part C: Enter Number In Row #############################################


def grids_augmented_in_row(grid, num, r):
    import copy
    validAugGrid = []
    for i in range(len(grid)):
        # if one of the elements is already the same as the number, return the original grid already
        if grid[r][i] == num:
            return [grid]
        if valid_entry(grid, num, r, i) and grid[r][i] == 'x':  # Use valid entry function to determine if the element in the row can be entered and loop throug everycolumn i
            gridCopy = copy.deepcopy(grid)
            gridCopy[r][i] = num  ### include the number trying to be added to subgrid
            validAugGrid.append(gridCopy)  # append valid grid to the list of possible subgrids

    return validAugGrid

##############################################Part D: Enter Number (#############################################

# Backtracking skeleton, modified for function
def solutions(completed, options, rowCounter, partial):
    if completed(partial, rowCounter):
        return [partial] #when completed returns true then a partial solution (with all rows checked) is returned
    else:
        res = []
        for o in options(partial, rowCounter): #o iterates through the options given which comes from insterting the number into each one of the rows recusrively
            res += solutions(completed, options, rowCounter + 1, o) #recursive call with the row counter being plus one to check the next row of each of the possible partial solutions
        return res

def grids_augmented_with_number(grid, num):
    import copy
    grid_copy = copy.deepcopy(grid)

    def completed(partial, rowCounter):  #
        if rowCounter == len(grid): #using additiional input argument to keep count of how many rows have been
            return True             #  checked and when last row is checked we know the function is completed

    def options(partial, rowCounter):  #options takes the partial solution and the row count
        augmentedGrids = grids_augmented_in_row(partial, num, rowCounter) #the options are given by the function defined in part c where number is inserted row by row giving back possible matrices
        return augmentedGrids

    sols = solutions(completed, options, 0, grid)
    return sols


############################################## Part E: Solve Sudoku  #############################################

def solve_sudoku(file_name):
    gridFromFile = grid_from_file(file_name)
    listA= [gridFromFile]
    listC = []
    for j in range(1,len(gridFromFile)+1): #loop to insert all numbers from 1 to n into each row
        listB = []
        for i in range(len(listA)): #loop to go through every possible matrix solution to iserting a number into a row
            listB = grids_augmented_with_number(listA[i], j) #list will contain possible matrices of inserting number j into each of the possible solutions i
            for z in range(len(listB)):
                listC.append(listB[z])
        listA = listC #update list 1 with the augmented list three which has added a the next number to each row and pass this list to the next function call
        listC=[] #empty list to append next possible solution of next iteration and pass this value into the original list
    return listA[0]


print(solve_sudoku('gridF.txt'))

