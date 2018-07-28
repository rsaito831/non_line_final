import numpy as np
import math


def logsitic(a):
    n = 2000
    x = [0.45]
    lyapunov_ex = 0
    a = round(a, 3)

    f3 = open("attractor.csv", "a")

    for i in range(n):
        x.append(a * x[-1] * (1 - x[-1]))

        dfx = a * (1 - 2 * x[-1])
        lyapunov_ex += math.log(abs(dfx))

        if i > (n - 201):
            f3.write(str(a) + " " + str(x[-2]) + " " + str(x[-1]) + "\n")
            f3.write(str(a) + " " + str(x[-1]) + " " + str(x[-1]) + "\n")
    f3.close()

    lyapunov_ex = lyapunov_ex / (n)

    return x[-100:], lyapunov_ex


def main():
    def __log_make(a, x):
        result = str(a) + " " + str(x) + "\n"
        return result

    f1 = open("log.csv", "w")
    f2 = open("lyapunov_ex_log.csv", "w")

    for a in np.linspace(0.001, 4.0, 4000):
        x, lyapunov_ex = logsitic(a)
        for i in x:
            result = __log_make(a, i)
            f1.write(result)

        result_ly = __log_make(a, lyapunov_ex)
        f2.write(result_ly)

    f1.close()
    f2.close()


if __name__ == "__main__":
    main()
