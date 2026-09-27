import csv
import sys

blueline_funcs = []

def parse_int(value, is_upper):
    if value == "NA":
        return sys.maxsize if is_upper else -sys.maxsize
    return int(value)


def parse_blueline(name, snrs, upprs, lwrs, seq, blueline_funcs):
    func = ""
    func += "func " + name + "() u8 {\n"
    func += "\t" + name + "_count u8 := 0\n"

    lines = []
    for i, snr in enumerate(snrs):
        snrs[i] = snr.replace("-", "_")
    for i, num in enumerate(upprs):
        lines.append(
            "\t" + name + "_count += " + snrs[i] + " > " + str(parse_int(num, True))
        )
    for i, num in enumerate(lwrs):
        lines.append(
            "\t" + name + "_count += " + snrs[i] + " < " + str(parse_int(num, False))
        )

    func += "\n".join(lines) + "\n"
    func += "\treturn " + name + "_count\n"
    func += "}\n\n"

    blueline_funcs.append(func)


def main():
    path = "BLMidTest - Sheet1.csv"
    blueline_funcs = []

    with open(path, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            name = row[0]
            snrs = row[1].split("|")
            upprs = row[2].split("|")
            lwrs = row[3].split("|")
            seq = row[4]
            parse_blueline(name, snrs, upprs, lwrs, seq, blueline_funcs)

    with open("arctext.txt", "w", newline="") as f:
        f.write("".join(blueline_funcs))

    # print(blueline_funcs)
    print("end")


if __name__ == "__main__":
    main()