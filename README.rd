# Breath 4 Hypermap
In January 2019 [Nexus Clash](https://www.nexusclash.com/index.php) recieved an update that changed the outer planes maps. The community took to it and created a google sheets map of the new planes tiles. I took it one step farther and edited in the new maps to a local copy of the old [hypermap](https://www.nexusclash.com/hypermap/) last updated Nov 04 2015 by Thalanor a.k.a. Esrahil. I used a very hastily written python script to pull out the new tile information from saved html files of the in-game screen. At the end of February the game changed the in game link to my copy of the updated map. It is an honor to have the privilege of maintaining the current edition of the map. None of these things were originally written by me except for the python scripts, sorry they are so sloppy.

## read script
read.py is the python script I used to pull the tile colors and coordinate data, it was very hastily written in python 3.7.2 and requires at least python 3.7.

### How to use
Note - Certain formatting will break this (such as non-unicode characters)
* load nexusclash.com and login
* connect to a character
* click the map button while outside to ensure the map info is loaded
* save the source code (input.html) (in chrome-like right click and click 'Save-as' make sure 'webpage, HTML only' is data type)
* run 'python read.py -i input.html'
* do what you'd like with the data

## readBatch script
Similar to read.py only run 'python readBatch.py' and it should process all the .html files in the working directory.

## Character Planner
I also have a slightly modified version of the [Character Planner](https://www.nexusclash.com/chargen_b3.5.html?v2) which changes the level/delevel button position and updates skill descriptions when needed. I don't think anyone realizes it is even here.
