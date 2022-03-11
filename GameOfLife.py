import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
Rules of Conway's Game of Life:
If a cell is ON:
    The cell will turn OFF if it has fewer than two neighbors
    The cell will turn OFF if it has more than three neighbors
        -> The cell will remain ON if it has two or three neighbors
If a cell is OFF:
    The cell will turn ON if it has exactly three neighbors
    
This implementation of the Game of Life uses Numpy arrays to represent the
game board, Matplotlib to display the game board, and ArgParse to create
a user interface through the command line.
"""


class GameOfLife:
    """
    The body of our game will be contained in this class
    """
    # Static variables representing cell states on our game board.
    ON = 1.00
    OFF = 0.00
    gridSize = 9
    gameBoard = np.zeros(shape=(9, 9))

    """
    Constructor creates a game board with grid size equal to the 
    variable grid size squared.
    
    Default grid size = 9
    """

    def __init__(self, gridSize: int = 9):
        self.gridSize = gridSize
        self.gameBoard = np.zeros(shape=(gridSize, gridSize))

    # set a point on the game board to ON
    def plantLife(self, i: int, j: int):
        self.gameBoard[i, j] = self.ON

    # checks the 8 neighbors of a point on the game board
    def cellNeighbors(self, i: int, j: int) -> float:
        neighborSum = 0
        cellNeighbors = [
            self.gameBoard[(i - 1) % self.gridSize, (j - 1) % self.gridSize],
            self.gameBoard[(i - 1) % self.gridSize, j],
            self.gameBoard[(i - 1) % self.gridSize, (j + 1) % self.gridSize],
            self.gameBoard[i, (j - 1) % self.gridSize],
            self.gameBoard[i, (j + 1) % self.gridSize],
            self.gameBoard[(i + 1) % self.gridSize, (j - 1) % self.gridSize],
            self.gameBoard[(i + 1) % self.gridSize, j],
            self.gameBoard[(i + 1) % self.gridSize, (j + 1) % self.gridSize]
        ]
        for k in cellNeighbors:
            neighborSum += k
        return neighborSum

    """
      runs the game: iterates through the entire game board, determining what points to
      change based on Conway's game rules. Implements this by cloning the game board
      and mapping changes onto the cloned board, replacing the old game board with the
      new game board once the entire board has been iterated through.
    """
    def gameMain(self) -> gameBoard:
        newBoard = self.gameBoard.copy()
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                if self.gameBoard[i, j] == self.ON:
                    if self.cellNeighbors(i, j) < 2 or self.cellNeighbors(i, j) > 3:
                        newBoard[i, j] = self.OFF
                else:
                    if self.cellNeighbors(i, j) == 3:
                        newBoard[i, j] = self.ON
        self.gameBoard = newBoard
        return self.gameBoard
    # clears the board / replaces all values in the board with 0 or OFF
    def clearBoard(self):
        self.gameBoard = np.zeros(shape=(self.gridSize, self.gridSize))

    # puts the game board to output
    def display(self):
        fig = plt.imshow(self.gameBoard, interpolation='nearest')


newGame = GameOfLife(9)
newGame.plantLife(0, 0)
newGame.plantLife(1, 1)
newGame.plantLife(2, 1)
newGame.plantLife(1, 2)
newGame.plantLife(0, 2)

