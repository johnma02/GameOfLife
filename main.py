from GameOfLife import GameOfLife
from matplotlib import animation
import matplotlib.pyplot as plt
import subprocess
import webbrowser

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
        print("Opening web browser.")
        webbrowser.open("http://pi.math.cornell.edu/~lipa/mec/lesson6.html")
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
        fps = int(input("How fast would you like you game to be played? (Frames per second)\n"))
        name = input("What would you like your game to be called? (Please end your game name with .gif)\n")
        print("Instantiating game... This may take a while\n")
        fig, ax = plt.subplots()
        img = ax.imshow(Game.gameBoard, interpolation='nearest')
        ani = animation.FuncAnimation(fig, Game.animate, fargs=(img, Game.gameBoard),
                                      frames=250,
                                      interval=10,
                                      save_count=50)
        ani.save(name, fps=fps)
        successfulSave = False
        while not successfulSave:
            cwd = input("Would you like to save your game in the current working directory? [Y/n]\n")
            if cwd == "Y":
                successfulSave = True
                print("Successfully saved "+name+" to current working directory")
            elif cwd == "n":
                newDirectory = input("Would you like to create a new directory to save your game in [Y/n]?\n")
                if newDirectory == "Y":
                    pathName = input("Please enter the path name for your new directory\n")
                    proc = subprocess.run(
                        ['bash', './movegif.sh', name, '1', pathName],
                        stdout=subprocess.PIPE,
                    )
                    print(proc.stdout.decode("UTF-8"))
                    if proc.returncode == 0:
                        successfulSave = True
                    else:
                        continue
                elif newDirectory == "n":
                    pathName = input("Please enter the path name for your new directory\n")
                    proc = subprocess.run(
                        ['bash', './movegif.sh', name, '0', pathName],
                        stdout=subprocess.PIPE,
                    )
                    print(proc.stdout.decode("UTF-8"))
                    if proc.returncode == 0:
                        successfulSave = True
                    else:
                        continue
        print("Exiting program...")


if __name__ == '__main__':
    main()
