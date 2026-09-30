import csv
import sys

blueline_funcs = []
blueline_seqs = []
seq_count = 0


def parse_int(value, is_upper):
    if value == "NA":
        return 100000 if is_upper else -30
    return int(value)


def parse_blueline(name, snrs, upprs, lwrs, seq):
    global seq_count

    func = ""
    func += "func " + name + "() u8 {\n"
    func += "\tis_blueline := false\n"

    for i, snr in enumerate(snrs):
        snrs[i] = snr.replace("-", "_")
    for i, num in enumerate(upprs):
        func += (
            "\tis_blueline = " + snrs[i] + " > " + str(parse_int(num, True))
            + " or is_blueline\n"
        )
    for i, num in enumerate(lwrs):
        func += (
            "\tis_blueline = " + snrs[i] + " < " + str(parse_int(num, False))
            + " or is_blueline\n"
        )
    func += "\treturn is_blueline\n"
    func += "}\n\n"

    blueline_funcs.append(func)
    blueline_seqs.append(seq)
    seq_count += 1


def main():
    path = "BLMidTest - Sheet1.csv"

    with open(path, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            name = row[0]
            snrs = row[1].split("|")
            upprs = row[2].split("|")
            lwrs = row[3].split("|")
            seq = row[4]
            parse_blueline(name, snrs, upprs, lwrs, seq)

    with open("arctext.txt", "w", newline="") as f:
        f.write("".join(blueline_funcs))

    print("end")


if __name__ == "__main__":
    main()