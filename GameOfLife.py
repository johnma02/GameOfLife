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

    def plantLife(self, i: int, j: int):
        self.gameBoard[i, j] = self.ON

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
            print("k: "+str(k)+" i: "+str(i)+" j: "+str(j))
            neighborSum += k
        return neighborSum

    def gameMain(self):
        newBoard = self.gameBoard.copy()
        print("ITERATION")
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                if self.gameBoard[i,j] == self.ON:
                    if self.cellNeighbors(i,j) < 2 or self.cellNeighbors(i,j) > 3:
                        newBoard[i,j] = self.OFF
                else:
                    if self.cellNeighbors(i,j) == 3:
                        newBoard[i,j] = self.ON
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
print(newGame.cellNeighbors(3, 3))
print(newGame.cellNeighbors(2, 3))
print(newGame.cellNeighbors(3, 4))
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()
newGame.outGame()
newGame.gameMain()
v
