# [Breath 4 Hypermap version 2.3](https://plscks.github.io/testHYPERMAP/hypermap.html)
## Changelog
### 12/05/2019 Planner 2.4.5
  * Fixes map level 30 HP/MP/AP
  * Fixes extra 5% to hit given for Ranged
  * Replaces gender specific grammar with gender neutral grammar
  * Corrects TLL description to be accurate per current mechanics
  * Corrects typo in Doom Howler's Scream of the Banshee
  * Changes Hellfire and Range Strike to have similar usage cost descriptions diferentiating them from eachother
  * Dark Heart and Sorcerer's Might descriptions changed to note that they can now go over maximum MP
  * Clarifies Holy Champion's Cloak of Tornado description to show AP/MP cost choices
  
### 12/05/2019 Planner 2.4.4
  * Fixes Seraph free skill, Arc Lightning was swapped with Clockwork Cloud still from years ago
  
### 11/28/2019 Planner 2.4.3
  * Reverts changes for Doom Howler Spell Combat skill as it ended up getting removed from the game instead
  
### 11/28/2019 Map version 2.3.1 / Planner 2.4.2
  * Updates Sewers coordinates to reflect new smaller sewers
  * Adds previously overlooked Spell Combat to the Doom Howler Aether Manipulation tree
  
### 11/24/2019 Planner 2.4.1
  * Updates skill changes from [11/24/2019 patch](https://www.nexusclash.com/modules.php?name=Forums&file=viewtopic&t=9318)
  
### 11/11/2019 Map version 2.3
  * Adds Keyboard support
  * Adds ARIA compatibility

### 11/03/2019 Map version 2.2
  * Adds Halloween costume shops
  * Updates planner to show Advocate Word of Holy Light no longer being a child skill
  * Fixes typo on Laurentia Costume Shop tile

### 09/18/2019 Map version 2.1
  * Profile Lookup tool updated to v0.5
  * Profile Tool can set missing exploration badges on Hypermap using localStorage
  * Fixes Profile Lookup Tool avatar stretching bug
  * Hypermap stays in Badge mode when changing planes

### 09/11/2019 Map version 2.0
  * Rewrote HTML to be mobile friendly
  * Rewrote CSS to be mobile friendly
  * Edited hypermap script to accommodate new HTML and CSS
  * Adds updated [Profile Lookup Tool](https://plscks.github.io/testHYPERMAP/profileLookup.html)
  * Adds updated [Character Planner](http://plscks.github.io/testHYPERMAP/chargen_b4_v2_2.html)

In January 2019 [Nexus Clash](https://www.nexusclash.com/index.php) received an update that changed the outer planes maps. The community took to it and created a google sheets map of the new planes tiles. I took it one step farther and edited in the new maps to a local copy of the old [hypermap](https://www.nexusclash.com/hypermap/) last updated Nov 04 2015 by Thalanor a.k.a. Esrahil. I used a very hastily written python script to pull out the new tile information from saved html files of the in-game screen. At the end of February the game changed the in game link to my copy of the updated map. It is an honor to have the privilege of maintaining the current edition of the map. None of these things were originally written by me except for the python scripts, sorry they are so sloppy.

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
