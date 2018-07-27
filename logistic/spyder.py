import numpy as np
#import math


def func1(x):
    return x


def func2(x):
    a = 3.7
    return a * x * (1 - x)


def body(x):
    y1 = func1(x)
    y2 = func2(x)

    return y1, y2


def main():
    f1 = open("func1.csv", "w")
    f2 = open("func2.csv", "w")

    for x in np.linspace(0, 1, 1000):
        y1, y2 = body(x)

        f1.write(str(x) + " " + str(y1) + "\n")
        f2.write(str(x) + " " + str(y2) + "\n")

    f1.close()
    f2.close()


if __name__ == "__main__":
    main()
