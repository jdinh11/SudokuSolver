import pygame as pg

def printGrid(grid):
    """Displays the sudoku board

    Args:
        grid(array): the Sudoku grid
    """
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end= " ")
        print()

def zeros(grid):
    """Find all empty spaces within the Sudoku board. Empty spaces are indicate by a 0.

    Args:
        grid(array): the Sudoku grid.

    Returns:
        list of tuples: the rows and columns of all the empty spaces within the grid
    """
    empty_spaces = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                empty_spaces.append((row, col))
            
    return empty_spaces

def solution(grid):
    pass

"""def solve(grid):
    space = empty(grid)
    
    if space == None:
        return True
    else:
        row, col = space
    
    for i in range(1, 10):
        if checkNum(grid, i, row, col):
            return grid
        
        grid[row][col] = 0

    return False
"""        

"""def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if checkNum(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True
"""

def checkNum(grid, num, row, col):
    #check answer against the row
    for i in range(len(grid[0])):
        if (grid[row][i] == num) and col != i:
            return False
        
    for j in range(len(grid)):
        if (grid[j][col] == num) and row != j:
            return False
        
    y = row // 3 * 3
    x = col // 3 * 3

    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if grid[i][j] == num and i != row and j != col:
                return False
            
    return True

def main(grid):
    pass
        
if __name__ == "__main__":
    """    grid = [
    [7,4,0,0,0,0,0,1,0],
    [0,0,0,0,7,0,0,9,4],
    [9,0,0,0,0,0,8,6,7],
    [0,9,4,1,8,0,5,0,0],
    [5,8,0,0,4,0,0,7,9],
    [3,7,0,0,9,6,0,0,0],
    [0,0,0,6,0,0,7,0,0],
    [0,3,9,0,5,0,0,0,0],
    [1,6,7,4,0,0,9,0,3]
]
"""    
        
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    print(main(grid))