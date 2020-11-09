# Process mapdata.csv and place into hypermap script.js
import csv

output = set()

with open('mapdata_amaravati.csv', mode='r') as mapdata:
    csv_data = csv.DictReader(mapdata)
    line_count = 0
    for row in csv_data:
        if line_count == 0:
            output.add('// Amaravati data set')
            line_count += 1
        output.add(f'registerTileNames({row["x"]},{row["y"]},6,{row["tile_name"]});')
        output.add(f'registerTileNames({row["x"]},{row["y"]},6,{row["tile_type"]});')
        line_count += 1
    print(f'Processed {line_count} number of lines')

with open('test.js', 'w') as outfile:
    for line in output:
        outfile.write(f'{line}\n')
