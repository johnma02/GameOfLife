import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import time

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

    def randomBoard(self):
        self.gameBoard = np.random.randint(2, size=(self.gridSize, self.gridSize))

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

    # This function is called by our main method, specifically by a FuncAnimation object to create an animation
    def animate(self, frame, img, gameBoard):
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
        img.set_data(newBoard)
        return img

    # clears the board / replaces all values in the board with 0 or OFF
    def clearBoard(self):
        self.gameBoard = np.zeros(shape=(self.gridSize, self.gridSize))

    def displayBoard(self):
        plt.imshow(self.gameBoard, interpolation='nearest')
        plt.show()


def main():
    print("Welcome to Conway's Game of Life")
    userInput = input("For an explanation of Conway's Game of Life, press [e]\n"
                      "To create a game of Conway's Game of Life, press [p]\n"
                      "To quit Conway's Game of Life, press [q]\n")
    validUserInputs = ['e', 'p', 'q']
    if userInput not in validUserInputs:
        print("-- Invalid input --")
        main()
    if userInput == 'e':
        print("Rules of Conway's Game of Life: ")
        time.sleep(2)
        print("The game is played on an 2D array, elements in the array represent cells in the game")
        time.sleep(3)
        print("If a cell is ON: \n"
              "The cell will turn OFF if it has fewer than two neighbors\n"
              "The cell will also turn OFF if it has more than three neighbors\n"
              "If the cell has two or three neighbors, it will remain ON")
        time.sleep(5)
        print("If a cell is OFF\n"
              "The cell will turn ON if it has exactly three neighbors")
        time.sleep(3)
        print("Returning to Main Menu...")
        time.sleep(3)
        main()
    if userInput == 'q':
        print("Exiting...")
        return
    if userInput == 'p':
        userGridLength = int(input("Enter an integer to represent your 2D array game board's size\n"))
        Game = GameOfLife(userGridLength)
        print("Your game has been initiated\n"
              "This is how your game board currently looks like")
        Game.displayBoard()
        while userInput != 'd':
            userInput = input("To plant life onto your game board, press [p]\n"
                              "To create a game board with randomly placed life, press [r]\n"
                              "To finalize your game board, press [d]\n")
            if userInput == 'p':
                x = int(input("Enter the x coordinate of your desired life form (0 - "+str(userGridLength-1)+")\n"))
                y = int(input("Enter the y coordinate of your desired life form (0 - "+str(userGridLength-1)+")\n"))
                Game.plantLife(y,x)
                print("This is how your game board currently looks like")
                Game.displayBoard()
            if userInput == 'r':
                Game.randomBoard()
                print("This is how your game board currently looks like")
                Game.displayBoard()
        print("Your game will be saved to the current directory")
        fps = int(input("How fast would you like you game to be played? (Frames per second)\n"))
        name = input("What would you like your game to be called? (Please end your game name with .gif)\n")
        time.sleep(2)
        print("Saving game to directory")
        fig, ax = plt.subplots()
        img = ax.imshow(Game.gameBoard, interpolation='nearest')
        ani = animation.FuncAnimation(fig, Game.animate, fargs=(img, Game.gameBoard),
                                      frames=250,
                                      interval=10,
                                      save_count=50)
        ani.save(name, fps=fps)
        plt.show()
        print("Successfully saved Game as Game.gif")
        print("Exiting program...")


if __name__ == '__main__':
    main()
