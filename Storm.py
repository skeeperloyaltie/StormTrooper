import math

import math

def reWriteTrooperData():
    print("StormTrooper  X      Y    Z  Rank      Distance to Rendezvous")
    print("---------------------------------------------------------")
    with open("Data.txt") as f:
        for line in f:
            parts = line.strip().split()
            id = parts[0][3:]
            # Extract the coordinates and remove non-numeric characters
            coords = "".join(filter(str.isdigit, parts[1]))
            x, y, z = map(int, [coords[i:i+2] for i in range(0, len(coords), 2)])
            rank = parts[2]
            distance = math.sqrt((x - 10) ** 2 + (y - 10) ** 2 + (z - 10) ** 2)
            print(f"{id:>11} {x:>6} {y:>5} {z:>3} {rank:>8} {distance:>22.2f} KM")

# Call the function to test it
reWriteTrooperData()
