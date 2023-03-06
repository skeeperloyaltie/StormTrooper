import math
from tabulate import tabulate

def reWriteTrooperData(file):
    headers = ["StormTrooper", "X", "Y", "Z", "Rank", "Distance to Rendezvous"]
    rows = []
    with open(file) as f:
        for line in f:
            parts = line.strip().split()
            try:
                # print(parts) # check the parts values
                id = parts[0][3:].replace(":", '')
            # Extract the coordinates and remove non-numeric characters
                coords = "".join(filter(str.isdigit, parts[1]))
                x, y, z = map(int, [coords[i:i+2] for i in range(0, len(coords), 2)])
                rank = parts[2]
                distance = math.sqrt((x - 10) ** 2 + (y - 10) ** 2 + (z - 10) ** 2)
            except (ValueError, IndexError): # make sure to handle the EOF of the file
#                 # skip lines with invalid or insufficient coordinate data
                continue
            rows.append([id, x, y, z, rank, f"{distance:.2f} KM"])
    table = tabulate(rows, headers=headers, tablefmt="plain", colalign=("center",)*6)
    print('\t\t\t{}'.format("Stormtrooper Data".upper()))
    print(table)
# Call the function to test it
reWriteTrooperData('Data.txt')
