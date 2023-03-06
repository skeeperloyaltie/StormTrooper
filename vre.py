import math
def reWriteTrooperData(file):
    # read data file
    with open(file, "r") as f:
        lines = f.readlines()

    # print table header
    print("{:^90}".format("StormTrooper Data"))
    print("{:<10}{:<10}{:<10}{:<10}{:<15}".format("ID", "X", "Y", "Z", "Rank"))
    print("-" * 55)

    # iterate over lines in data file
    for line in lines:
        line = line.strip()  # remove leading/trailing whitespace

        if not line:  # skip empty lines
            continue

        # parse data from line
        parts = line.split(":")
        id = parts[0].replace(" ", "")
        coords = parts[1].replace(" ", "")
        x, y, z = map(int, coords[1:].split("Y"))
        rank = parts[2].strip()

        # calculate distance to rendezvous
        distance = round(math.sqrt((x-10)**2 + (y-10)**2 + (z-10)**2), 2)

        # print trooper data
        print("{:<10}{:<10}{:<10}{:<10}{:<15}".format(id, x, y, z, rank, distance))

reWriteTrooperData('Data.txt')
