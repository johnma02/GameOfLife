from GameOfLife import GameOfLife
from matplotlib import animation
import matplotlib.pyplot as plt
import time

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
        print("Successfully saved Game as "+name)
        print("Exiting program...")


if __name__ == '__main__':
    main()
