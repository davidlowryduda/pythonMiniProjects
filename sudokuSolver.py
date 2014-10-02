"""
.. module:: sudokuSolver.py

.. moduleauthor:: David Lowry-Duda <davidlowryduda@davidlowryduda.com>

"""

class Cell:
    """
    The Cell class.

    This about the cell class, TODO

    """

    # instance variables: row, col, group, possib, isSolved
    isSolved = False

    def __init__(self, row, col, possibs = range(1,10)):
        self.row = row
        self.col = col
        self.group = self.findGroup(row, col)
        self.possib = possibs

    # Figure out which group the cell is in
    def findGroup(self, row, col):
        pass

    def getRow(self):
        return self.row

    def setRow(self, row):
        self.row = row

    def getCol(self):
        return self.col

    def setCol(self, col):
        self.col = col

    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getPossib(self):
        return self.possib

    def removePossib(self, n):
        try:
            self.possib.remove(n)
        except ValueError:
            pass

    def getSolved(self):
        return isSolved

    def setSolved(self, newBool):
        self.isSolved = newBool



class SudokuGrid:

    # instance variables: grid

    grid = []

    # TODO: Check starting grid
    def __init__(self, startingGrid, size=9):
        for row in range(size):
            self.grid.append([])
            for col in range(size):
                if startingGrid[row][col]:
                    self.grid[row].append(Cell(row,col,startingGrid[row][col]))
                else:
                    self.grid[row].append(Cell(row,col))

    # Set up row, col, group lists?

    # Check row/rows

    # Check col/cols

    # Check group/groups

    # Find minimal number of choices

    # stillPossible?



class SudokuSolver:

    def __init__(self, size=9):
        self.sudokuGrid = SudokuGrid()

    # Main Runner
    ## Check everything
    ## find if still possible
    ## find minimal spot
    ## guess at minimal spot, run Runner recursively on guess
