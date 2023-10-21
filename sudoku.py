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

def backtrack(grid, cells):
    """Implementing a backtracking process to solve the Sudoku
    
    Args:
    
        grid(array): the Sudoku grid
        cells(list of tuples): a list containing the positions of all empty cells
        
    Returns:
    
    """
    current = 0

    while current < len(cells):
        row, col = cells[current]
        found = False
        for num in range(grid[row][col] + 1, 10):

            if checkNum(grid, num, row, col):
                found = True
                grid[row][col] = num
                current += 1
                break

        if not found:
            current -= 1 
            grid[row][col] = 0          
    
    return grid

def solution(grid):
    pass

def checkNum(grid, num, row, col):
    """Verify the solution
    
    Args:
        grid(array): the Sudoku grid
        num(int): the potential solution
        row(int): the current row index
        col(int): the current column index

    Returns:
        bool: True if the answer is valid and False otherwise 
    
    """
    for i in range(len(grid[0])): # check answer against row
        if (grid[row][i] == num) and col != i:
            return False
        
    for j in range(len(grid)): # check answer against column
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
    empty_cells = zeros(grid)
    grid = backtrack(grid, empty_cells)
    return grid
        
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
    #printGrid(grid)
    printGrid(main(grid))
