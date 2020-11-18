# Process mapdata.csv and place into hypermap script.js
import csv

outputTileNames = set()
outputTileTypes = set()

with open('mapdata_amaravati.csv', mode='r') as mapdata:
    csv_data = csv.DictReader(mapdata)
    line_count = 0
    for row in csv_data:
        outputTileNames.add(f'registerTileNames({int(row["x"])-19},{row["y"]},6,\"{row["tile_name"]}\");')
        outputTileTypes.add(f'registerTileTypes({int(row["x"])-19},{row["y"]},6,\"{row["tile_type"]}\");')
        line_count += 1
    print(f'Processed {line_count} number of lines')

with open('adjustedCoords.js', 'w') as outfile:
    outfile.write('// Amaravati Names data set\n')
    for line in outputTileNames:
        outfile.write(f'{line}\n')
    outfile.write('\n// Amaravati Types data set\n')
    for line in outputTileTypes:
        outfile.write(f'{line}\n')
