import csv

path = "PLTest.csv"
with open(path, newline="") as file:
    reader = csv.reader(path)

    PLcount = 0
    PLstage = False

    for row in reader:
        if (row[1]=="BLS"):
            PLstage = True
            PLcount += 1
        elif (row[1]=="BLE"):
            PLstage = False