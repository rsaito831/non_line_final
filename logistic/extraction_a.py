import sys


def extraction():
    alpha = sys.argv[1]

    f1 = open("extraction.csv", "w")
    with open("attractor.csv") as f2:
        for line in f2:
            msg = line.split()

            if float(msg[0]) == float(alpha):
                f1.write(line)

        f1.close()


def main():
    extraction()


if __name__ == "__main__":
    main()
