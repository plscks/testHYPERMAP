# Hopefully read an html file and spit out useful stuff?
#
# ######################
# ## Proof Of Concept ##
# ######################
#
# written by plscks
#
# Oh lord! I've used this for stuff, maybe I'll refine it in the future.
#
# This program pulls tile color, coordinates, and tile title from raw source code of any nexusclash.com page source code
# as long as the map was opened when the source code saved.
#
# Written terribly in python 3.7.2
# requires python 3.7
#
# ################
# ## HOW TO USE ##
# ################
#
# 1) load nexusclash.com
# 2) login
# 3) connect to a character
# 4) click the map button while outside to ensure the map info is loaded
# 5) save the source code (input.html) (in chrome-like right click and click 'Save-as' make sure 'webpage, HTML only' is data type)
# 6) run 'python readBatch.py'
# 7) do what you'd like with the data
#
# Sorry this is a huge mess of cobbled together nightmare pudding. - plscks
#
# p.s. - I'm really sorry about the 25 elifs down there, I'll fix that maybe one day if I can???
#
# TODO
########
# place equations for coordinates in a dictionary and use the dictionary to pull coordinates
#
import os
import re
import sys, getopt
from os import listdir
from os.path import isfile, join
from collections import OrderedDict

def readFiles(cwd):
    """Read files in current directory, create a list of all .html files, and then verify they are the proper files"""

    files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
    allFiles = []
    keep = []
    for item in files:
        if item.endswith('.html'):
            allFiles.append(item)
    for htmlFile in allFiles:
        with open (htmlFile, 'rt') as in_file:
            try:
                contents = in_file.read()
                isCorrect1 = re.search(r'\d{1,2}\, \d{1,2}(?= \w)', contents)
                isCorrect = isCorrect1.group(0)
                keep.append(htmlFile)
            except UnicodeDecodeError:
                pass
            except AttributeError:
                pass
    return keep

cwd = os.getcwd()
goodList = readFiles(cwd)
finalNameListLaur = []
finalTypeListLaur = []
finalNameListStyg = []
finalTypeListStyg = []
finalNameListEly = []
finalTypeListEly = []

for inputfile in goodList:
    with open (inputfile, 'rt') as in_file:
        contents = in_file.read() # Read the entire file into a variable named contents.
        xy = ['x', 'y']
        center = {}
        print(inputfile)

        try:
            planeRaw = re.search(r'(?<=\d ).*(?=, a <a)', contents)
            plane = planeRaw.group(0)
        except AttributeError:
            planeRaw = re.search(r'(?<=\d ).*(?=, an <a)', contents)
            plane = planeRaw.group(0)
        
        if plane == 'Laurentia':
            planeNum = 0
        elif plane == 'Elysium':
            planeNum = 1
        elif plane == 'Stygia':
            planeNum = 2
        
        coordBig = re.search(r'\d{1,2}\, \d{1,2}(?= \w)', contents)
        coord = coordBig.group(0)
        print('(' + coord + ' ' + plane + ')\n')
        coorddecomma = coord.replace(',', '')
        coordlist = coorddecomma.split()
        coordlist = list(map(int, coordlist))
        center = dict(zip(xy, coordlist))    

        print('--------------------------------------------------')
        info1 = re.search(r'(<td height).*?(<\/td>)', contents)
        info = info1.group(0)
        print(info)

        color1 = re.search(r'(?<=bgcolor=).*?(?=  )', info)
        color = color1.group(0)
        print(color)
    
        title1 = re.search(r'(?<=title=").*?(?=">)', info)
        title = title1.group(0)
        print(title)

        print('-------------------------------------------------')

        pattern = re.compile(r'(<td height).*?(<\/td>)')
       
        for idx, m in enumerate(re.finditer(pattern, contents)):        
            color1 = re.search(r'(?<=bgcolor=).*?(?=  )', m.group(0))
            color = color1.group(0)
            print(color)
    
            title1 = re.search(r'(?<=title=").*?(?=">)', m.group(0))
            title = title1.group(0)
            if title == 'Twisted Void':
                title = 'Twisted Void, Twisted Void'
            tileInfos = title.split(", ")
            tileName, tileType = tileInfos
            print(tileName + ', ' + tileType)

            if (idx+1) == 1:
                x1 = center['x'] - 2
                y1 = center['y'] - 2
                print('(' + str(x1) + ', ' + str(y1) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x1) + ',' + str(y1) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x1) + ',' + str(y1) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x1) + ',' + str(y1) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x1) + ',' + str(y1) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x1) + ',' + str(y1) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x1) + ',' + str(y1) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 2:
                x2 = center['x'] - 1
                y2 = center['y'] - 2
                print('(' + str(x2) + ', ' + str(y2) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x2) + ',' + str(y2) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x2) + ',' + str(y2) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x2) + ',' + str(y2) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x2) + ',' + str(y2) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x2) + ',' + str(y2) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x2) + ',' + str(y2) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 3:
                x3 = center['x']
                y3 = center['y'] - 2
                print('(' + str(x3) + ', ' + str(y3) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x3) + ',' + str(y3) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x3) + ',' + str(y3) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x3) + ',' + str(y3) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x3) + ',' + str(y3) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x3) + ',' + str(y3) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x3) + ',' + str(y3) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 4:
                x4 = center['x'] + 1
                y4 = center['y'] - 2
                print('(' + str(x4) + ', ' + str(y4) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x4) + ',' + str(y4) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x4) + ',' + str(y4) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x4) + ',' + str(y4) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x4) + ',' + str(y4) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x4) + ',' + str(y4) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x4) + ',' + str(y4) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 5:
                x5 = center['x'] + 2
                y5 = center['y'] - 2
                print('(' + str(x5) + ', ' + str(y5) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x5) + ',' + str(y5) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x5) + ',' + str(y5) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x5) + ',' + str(y5) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x5) + ',' + str(y5) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x5) + ',' + str(y5) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x5) + ',' + str(y5) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 6:
                x6 = center['x'] - 2
                y6 = center['y'] - 1
                print('(' + str(x6) + ', ' + str(y6) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x6) + ',' + str(y6) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x6) + ',' + str(y6) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x6) + ',' + str(y6) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x6) + ',' + str(y6) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x6) + ',' + str(y6) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x6) + ',' + str(y6) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 7:
                x7 = center['x'] - 1
                y7 = center['y'] - 1
                print('(' + str(x7) + ', ' + str(y7) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x7) + ',' + str(y7) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x7) + ',' + str(y7) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x7) + ',' + str(y7) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x7) + ',' + str(y7) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x7) + ',' + str(y7) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x7) + ',' + str(y7) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 8:
                x8 = center['x']
                y8 = center['y'] - 1
                print('(' + str(x8) + ', ' + str(y8) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x8) + ',' + str(y8) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x8) + ',' + str(y8) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x8) + ',' + str(y8) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x8) + ',' + str(y8) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x8) + ',' + str(y8) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x8) + ',' + str(y8) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 9:
                x9 = center['x'] + 1
                y9 = center['y'] - 1
                print('(' + str(x9) + ', ' + str(y9) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x9) + ',' + str(y9) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x9) + ',' + str(y9) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x9) + ',' + str(y9) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x9) + ',' + str(y9) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x9) + ',' + str(y9) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x9) + ',' + str(y9) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 10:
                x10 = center['x'] + 2
                y10 = center['y'] - 1
                print('(' + str(x10) + ', ' + str(y10) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x10) + ',' + str(y10) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x10) + ',' + str(y10) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x10) + ',' + str(y10) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x10) + ',' + str(y10) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x10) + ',' + str(y10) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x10) + ',' + str(y10) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 11:
                x11 = center['x'] - 2
                y11 = center['y']
                print('(' + str(x11) + ', ' + str(y11) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x11) + ',' + str(y11) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x11) + ',' + str(y11) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x11) + ',' + str(y11) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x11) + ',' + str(y11) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x11) + ',' + str(y11) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x11) + ',' + str(y11) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 12:
                x12 = center['x'] - 1
                y12 = center['y']
                print('(' + str(x12) + ', ' + str(y12) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x12) + ',' + str(y12) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x12) + ',' + str(y12) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x12) + ',' + str(y12) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x12) + ',' + str(y12) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x12) + ',' + str(y12) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x12) + ',' + str(y12) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 13:
                x13 = center['x']
                y13 = center['y']
                print('(' + str(x13) + ', ' + str(y13) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x13) + ',' + str(y13) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x13) + ',' + str(y13) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x13) + ',' + str(y13) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x13) + ',' + str(y13) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x13) + ',' + str(y13) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x13) + ',' + str(y13) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 14:
                x14 = center['x'] + 1
                y14 = center['y']
                print('(' + str(x14) + ', ' + str(y14) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x14) + ',' + str(y14) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x14) + ',' + str(y14) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x14) + ',' + str(y14) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x14) + ',' + str(y14) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x14) + ',' + str(y14) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x14) + ',' + str(y14) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 15:
                x15 = center['x'] + 2
                y15 = center['y']
                print('(' + str(x15) + ', ' + str(y15) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x15) + ',' + str(y15) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x15) + ',' + str(y15) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x15) + ',' + str(y15) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x15) + ',' + str(y15) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x15) + ',' + str(y15) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x15) + ',' + str(y15) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 16:
                x16 = center['x'] - 2
                y16 = center['y'] + 1
                print('(' + str(x16) + ', ' + str(y16) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x16) + ',' + str(y16) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x16) + ',' + str(y16) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x16) + ',' + str(y16) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x16) + ',' + str(y16) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x16) + ',' + str(y16) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x16) + ',' + str(y16) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 17:
                x17 = center['x'] - 1
                y17 = center['y'] + 1
                print('(' + str(x17) + ', ' + str(y17) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x17) + ',' + str(y17) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x17) + ',' + str(y17) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x17) + ',' + str(y17) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x17) + ',' + str(y17) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x17) + ',' + str(y17) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x17) + ',' + str(y17) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 18:
                x18 = center['x']
                y18 = center['y'] + 1
                print('(' + str(x18) + ', ' + str(y18) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x18) + ',' + str(y18) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x18) + ',' + str(y18) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x18) + ',' + str(y18) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x18) + ',' + str(y18) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x18) + ',' + str(y18) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x18) + ',' + str(y18) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 19:
                x19 = center['x'] + 1
                y19 = center['y'] + 1
                print('(' + str(x19) + ', ' + str(y19) + ')')
                print('')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x19) + ',' + str(y19) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x19) + ',' + str(y19) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x19) + ',' + str(y19) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x19) + ',' + str(y19) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x19) + ',' + str(y19) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x19) + ',' + str(y19) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 20:
                x20 = center['x'] + 2
                y20 = center['y'] + 1
                print('(' + str(x20) + ', ' + str(y20) + ')\n')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x20) + ',' + str(y20) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x20) + ',' + str(y20) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x20) + ',' + str(y20) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x20) + ',' + str(y20) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x20) + ',' + str(y20) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x20) + ',' + str(y20) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 21:
                x21 = center['x'] - 2
                y21 = center['y'] + 2
                print('(' + str(x21) + ', ' + str(y21) + ')\n')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x21) + ',' + str(y21) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x21) + ',' + str(y21) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x21) + ',' + str(y21) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x21) + ',' + str(y21) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x21) + ',' + str(y21) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x21) + ',' + str(y21) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 22:
                x22 = center['x'] - 1
                y22 = center['y'] + 2
                print('(' + str(x22) + ', ' + str(y22) + ')\n')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x22) + ',' + str(y22) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x22) + ',' + str(y22) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x22) + ',' + str(y22) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x22) + ',' + str(y22) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x22) + ',' + str(y22) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x22) + ',' + str(y22) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 23:
                x23 = center['x']
                y23 = center['y'] + 2
                print('(' + str(x23) + ', ' + str(y23) + ')\n')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x23) + ',' + str(y23) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x23) + ',' + str(y23) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x23) + ',' + str(y23) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x23) + ',' + str(y23) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x23) + ',' + str(y23) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x23) + ',' + str(y23) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 24:
                x24 = center['x'] + 1
                y24 = center['y'] + 2
                print('(' + str(x24) + ', ' + str(y24) + ')\n')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x24) + ',' + str(y24) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x24) + ',' + str(y24) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x24) + ',' + str(y24) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x24) + ',' + str(y24) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x24) + ',' + str(y24) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x24) + ',' + str(y24) + ',' + str(planeNum) + ',"' + tileType + '");')
            elif (idx+1) == 25:
                x25 = center['x'] + 2
                y25 = center['y'] + 2
                print('(' + str(x25) + ', ' + str(y25) + ')\n')
                if planeNum == 0:
                    finalNameListLaur.append('registerTileNames(' + str(x25) + ',' + str(y25) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListLaur.append('registerTileTypes(' + str(x25) + ',' + str(y25) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 1:
                    finalNameListEly.append('registerTileNames(' + str(x25) + ',' + str(y25) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListEly.append('registerTileTypes(' + str(x25) + ',' + str(y25) + ',' + str(planeNum) + ',"' + tileType + '");')
                if planeNum == 2:
                    finalNameListStyg.append('registerTileNames(' + str(x25) + ',' + str(y25) + ',' + str(planeNum) + ',"' + tileName + '");')
                    finalTypeListStyg.append('registerTileTypes(' + str(x25) + ',' + str(y25) + ',' + str(planeNum) + ',"' + tileType + '");')

        print('---------------------------------------------\n')
        print('Center point: (' + coord + ' ' + plane + ')\n')


finalNameListEly = list(OrderedDict.fromkeys(finalNameListEly))
finalTypeListEly = list(OrderedDict.fromkeys(finalTypeListEly))
finalNameListStyg = list(OrderedDict.fromkeys(finalNameListStyg))
finalTypeListStyg = list(OrderedDict.fromkeys(finalTypeListStyg))
for elyName in finalNameListEly:
    print(elyName)
for stygName in finalNameListStyg:
    print(stygName)
print('\n')
for elyType in finalTypeListEly:
    print(elyType)
for stygType in finalTypeListStyg:
    print(stygType)
