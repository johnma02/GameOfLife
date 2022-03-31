# GameOfLife
#### Work in progress.
Game of Life implemented in Python.
![alt-text](https://github.com/johnma02/GameOfLife/blob/master/GameExamples/LargerInstance.gif)


This implementation is Object-Oriented as an exercise in 
Object-Oriented programming.

[Explanation of The Game of Life](http://pi.math.cornell.edu/~lipa/mec/lesson6.html)


Once executed, users will be prompted to create a game board with 
size of their choosing, and then will be prompted to populate
the game board with "life".


Once the user finalizes the game board, they will be prompted to enter the speed in frames
per second with which they wish their game instance to be "played" at, then they will be
prompted to name their game file.


The game instance will be saved as _"name"_.gif
in the working directory of the python file.


This repository includes an example of a saved game instance named "Example.gif".

This example is a "Glider" pattern, see this [link](http://pi.math.cornell.edu/~lipa/mec/lesson6.html) for more
interesting patterns.

This program is executable from the command line, provided the required packages are installed.


```commandline
python main.py
```
If this program is initiated from the command line, whenever a MatPlotLib plot is opened, the user should close the plot whenever they are finished viewing the plot in order for the program to continue running.

Required packages:

[Numpy](https://numpy.org/install/), [Matplotlib](https://matplotlib.org/stable/users/installing/index.html)



## Current future objectives
- [x] Allow users to save animations to other directories
- [ ] Add custom colors to finished game gif files
- [ ] Add cool preset games
- [ ] Detect if user has initiated program from command line and run a separate main function giving special instructions to the user
- [ ] Create feature to allow user to save configurations for future use


#### Currently, I think using SQLite to store coordinates on on the users cloned directory may be feasible to fufill this task. Will look into it.
- [ ] Create beautiful GUI
#### I'm leaving this task for until I feel this project is "complete". Through some preliminary investigation, _Tkinter_, _Pygame_, or _Qt_ seem to be best suited for this task.

## Known Issues
See  above instructions for users who elect to execute this program from the command line
