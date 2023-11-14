import tkinter as tk

class Solver():
    """A class to solve a Sudoku grid using backtracking algorithm
    
    Attributes:
        grid (arr)"""
    def __init__(self, grid):
        """Initialize a Solver class to solve a Sudoku board

        Args:
            grid (arr): the Sudoku grid
        """
        self.grid = grid
        self.empty = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    self.empty.append((row, col))

    def printGrid(self):
        """Displays the sudoku board

        Args:
            grid(array): the Sudoku grid
        """
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end= " ")
            print()

    def zeros(self):
        """Find all empty spaces within the Sudoku board. Empty spaces are indicate by a 0.

        Args:
            grid(array): the Sudoku grid.

        Returns:
            list of tuples: the rows and columns of all the empty spaces within the grid
        """
        empty = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 0:
                    empty.append((row, col))
                
        return empty
    
    def checkNum(self, num, row, col):
        """Verify the solution
        
        Args:
            grid(array): the Sudoku grid
            num(int): the potential solution
            row(int): the current row index
            col(int): the current column index

        Returns:
            bool: True if the answer is valid and False otherwise 
        
        """
        for i in range(len(self.grid[0])): # check answer against row
            if (self.grid[row][i] == num) and col != i:
                return False
            
        for j in range(len(self.grid)): # check answer against column
            if (self.grid[j][col] == num) and row != j:
                return False
            
        y = row // 3 * 3
        x = col // 3 * 3

        for i in range(y, y + 3):
            for j in range(x, x + 3):
                if self.grid[i][j] == num and i != row and j != col:
                    return False
                
        return True
    
    def backtrack(self):
        """Implementing a backtracking process to solve the Sudoku
        
        Args:
        
            grid(array): the Sudoku grid
            cells(list of tuples): a list containing the positions of all empty cells
            
        Returns:
        
        """
        current = 0

        while current < len(self.empty):
            row, col = self.empty[current]
            found = False
            for num in range(self.grid[row][col] + 1, 10):

                if self.checkNum(num, row, col):
                    found = True
                    self.grid[row][col] = num
                    current += 1
                    break

            if not found:
                current -= 1 
                self.grid[row][col] = 0
        
        return self.grid

def main(grid):
    solver = Solver(grid)
    solver.backtrack()
    return solver
        
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
        
    SUDOKU = [
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
    
    main(SUDOKU).printGrid()