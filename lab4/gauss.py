import math


def f(x):
    return math.sqrt(1 + math.sin(x))


def gauss():
    x = [0.033765, 0.169395, 0.380690, 0.619310, 0.830605, 0.966235]
    A = [0.085662, 0.180381, 0.233957, 0.233957, 0.180381, 0.085662]
    res = 0
    for i in range(6):
        res += A[i] * f(x[i])
    return res


if __name__ == '__main__':
    print(gauss())
