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
in a directory of the users choosing.


This repository includes an example of a saved game instance named "Example.gif".

See this [link](http://pi.math.cornell.edu/~lipa/mec/lesson6.html) for more
interesting patterns.

This program is executable from the command line, provided the required packages are installed.


```commandline
python main.py
```
If this program is initiated from the command line, whenever a MatPlotLib plot is opened, the user should close the plot whenever they are finished viewing the plot in order for the program to continue running.

Required packages:

[Numpy](https://numpy.org/install/), [Matplotlib](https://matplotlib.org/stable/users/installing/index.html)
