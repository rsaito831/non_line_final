import numpy as np
import math


def logsitic(b):
    n = 2000
    x = [0.6, 0.45]

    b = round(b, 3)

    e_0 = np.array([[-1 / math.sqrt(2)], [1 / math.sqrt(2)]])
    f_0 = np.array([[1 / math.sqrt(2)], [1 / math.sqrt(2)]])

    cnt = 0
    logLi = 0
    logSi = 0

    f4 = open("attractor.csv", "a")

    for i in range(n):
        cnt += 1
        x.append(b * x[-1] * (1 - x[-2]))

        if i > (n - 201):
            f4.write(str(b) + " " + str(x[-3]) + " " + str(x[-2]) + "\n")

        DF = np.array([[0, 1], [-b * x[-1], b * (1 - x[-2])]])

        e_1 = np.dot(DF, e_0)
        f_1 = np.dot(DF, f_0)

        L1 = np.linalg.norm(e_1)

        hoge = (np.dot(f_1.T, e_1) / L1**2) * e_1
        f_1_ = f_1 - hoge
        hoge = np.linalg.norm(f_1_)
        S1 = L1 * hoge

        logLi += math.log(L1)
        logSi += math.log(S1)

        e_0 = e_1 / L1
        f_0 = f_1_ / hoge

    lambda1 = logLi / cnt
    lambda2 = logSi / cnt - lambda1

    return x[-100:], lambda1, lambda2


def main():
    def __log_make(b, x):
        result = str(b) + " " + str(x) + "\n"
        return result

    f1 = open("delay_log.csv", "w")
    f2 = open("lambda1_log.csv", "w")
    f3 = open("lambda2_log.csv", "w")

    for b in np.linspace(1.8, 2.27, 470):
        x, lambda1, lambda2 = logsitic(b)
        for i in x:
            result = __log_make(b, i)
            f1.write(result)

        result_ly1 = __log_make(b, lambda1)
        f2.write(result_ly1)

        result_ly2 = __log_make(b, lambda2)
        f3.write(result_ly2)

    f1.close()
    f2.close()
    f3.close()


if __name__ == "__main__":
    main()
