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
    ON = 1
    OFF = 0
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

    def plantLife(self, i: int, j: int):
        self.gameBoard[i,j] = self.ON

    def cellNeighbors(self, i: int, j: int) -> float:
        iPlusOne = i + 1
        jPlusOne = j + 1
        if iPlusOne == self.gridSize:
            iPlusOne = 0
        if jPlusOne == self.gridSize:
            jPlusOne = 0
        neighborSum = 0
        cellNeighbors = [
                    self.gameBoard[i - 1, j - 1],
                    self.gameBoard[i - 1, j],
                    self.gameBoard[i - 1, jPlusOne],
                    self.gameBoard[i, j - 1],
                    self.gameBoard[i, jPlusOne],
                    self.gameBoard[iPlusOne, j - 1],
                    self.gameBoard[iPlusOne, j],
                    self.gameBoard[iPlusOne, jPlusOne]
                ]
        for k in cellNeighbors:
            neighborSum += k
        return neighborSum

    def gameMain(self):
        newBoard = self.gameBoard
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                neighborCount = self.cellNeighbors(i, j)
                if self.gameBoard[i, j] == self.ON and neighborCount < 2:
                    newBoard[i, j] = self.OFF
                elif self.gameBoard[i, j] == self.ON and neighborCount > 3:
                    newBoard[i, j] = self.OFF
                elif self.gameBoard[i, j] == self.OFF and neighborCount == 3:
                    newBoard[i, j] = self.ON
        self.gameBoard = newBoard

    def clearBoard(self):
        self.gameBoard = np.zeros(shape=(self.gridSize, self.gridSize))

    def outGame(self):
        plt.imshow(self.gameBoard, interpolation='nearest')
        plt.show()


newGame = GameOfLife(9)
newGame.plantLife(3, 3)
newGame.plantLife(2, 3)
newGame.plantLife(1, 4)
newGame.plantLife(2, 5)
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()



