import csv
import sys

def parsePL(PLsnrs, PLupps, PLlws, seq):
    PLfunc = ""
    PLfunc += "func check_purple() u8 {\n"
    for i, num in enumerate(PLupps):
        PLfunc += "\t" + PLsnrs[i] + " > " + str(parseInt(num, True)) + " => " + seq + "\n"
    for i, num in enumerate(PLlws):
        PLfunc += "\t" + PLsnrs[i] + " < " + str(parseInt(num, False)) + " => " + seq + "\n"
    PLfunc += "}"
    return PLfunc


def parseInt(s, upr):
    if (s=="NA" and upr):
        return sys.maxsize
    elif (s=="NA" and not upr):
        return -sys.maxsize
    else:
        return int(s)

path = "PLTest - Sheet1.csv"
with open(path, newline="") as file:
    reader = csv.reader(file)

    PLcount = 0
    PLstage = False
    PLfunc = ""
    PLsnrs = []
    PLupps = []
    PLlws = []
    seq = ""

    for row in reader:
        if (row[1]!=None and row[1]=="BLS"):
            PLstage = True
            PLcount += 1
            PLsnrs = row[2].split("|")
            PLupps = row[3].split("|")
            PLlws = row[4].split("|")
            seq = row[5]
            PLfunc = parsePL(PLsnrs, PLupps, PLlws, seq)
        elif (row[1]!=None and row[1]=="BLE"):
            PLstage = False

    with open("arctext.txt", "w", newline="") as f:
        f.write(PLfunc)

print("end")
