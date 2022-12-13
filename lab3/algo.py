import copy
import math
import decimal

decimal.getcontext().rounding = decimal.ROUND_DOWN
A = [[1.2345, 3.1415, 1], [2.3456, 5.9690, 0], [3.4567, 2.1828, 2.1]]
b = [9.9275, 14.2836, 12.8833]
solution = [1.0, 2.0, 2.41]


def norm(x, x_k):
    """
   считаем норму
    """
    difference_sum = sum(((x[i] - x_k[i]) ** 2 for i in range(3)))
    return math.sqrt(difference_sum)


def compact_gauss(A, b, r):
    for i in range(len(A)):
        a = A[i][i]
        for k in range(i, len(A)):
            A[i][k] = discardNDigits(A[i][k] / a, r)
        b[i] = discardNDigits(b[i] / a, r)
        for k in range(i + 1, len(A)):
            c = discardNDigits(-A[k][i], r)
            for j in range(i, len(A)):
                A[k][j] += discardNDigits(c * A[i][j], r)
            b[k] += discardNDigits(c * b[i], r)

    for i in range(len(A) - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            c = discardNDigits(-A[k][i], r)
            A[k][i] = discardNDigits(A[k][i] + c * A[i][i], r)
            b[k] = discardNDigits(b[k] + c * b[i], r)

    return b.copy()


def gauss_main_element(A, b, r):
    n = len(A)
    visited = [False] * n
    order = []
    for _ in range(n):
        max_items = map(lambda x: (x[0], *max(enumerate(x[1]), key=lambda y: abs(y[1]))), enumerate(A))
        i, j = max(filter(lambda y: not visited[y[0]], max_items), key=lambda x: abs(x[2]))[:2]
        a = A[i][j]
        visited[i] = True
        order.append((i, j))
        for k in range(n):
            A[i][k] = discardNDigits(A[i][k] / a, r)
        b[i] = discardNDigits(b[i] / a, r)
        for k in range(n):
            if visited[k]:
                continue
            c = -A[k][j]
            for l in range(n):
                A[k][l] = discardNDigits(A[k][l] + c * A[i][l], r)
            b[k] = discardNDigits(b[k] + c * b[i], r)

    x = [0 for _ in range(0, n)]
    for i in range(n - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            c = -A[order[k][0]][order[i][1]]
            A[order[k][0]][order[i][1]] = discardNDigits(A[order[k][0]][order[i][1]] + c * A[order[i][0]][order[i][1]],
                                                         r)
            b[order[k][0]] = discardNDigits(b[order[k][0]] + c * b[order[i][0]], r)
        x[order[i][1]] = b[order[i][0]]

    return x


def discardNDigits(x, n):
    # 34,1499 By default it should return 34.15 due to '99' after '34.14'
    c = decimal.Decimal(x)
    return float(round(c, n))


if __name__ == '__main__':
    A = [[1.2345, 3.1415, 1], [2.3456, 5.9690, 0], [3.4567, 2.1828, 2.1]]
    b = [9.9275, 14.2836, 12.8833]

    print('Компактная схема Гаусса:')

    print('k = 2')
    cg2 = compact_gauss(copy.deepcopy(A), copy.deepcopy(b), 2)
    print(cg2)
    print(norm(cg2, solution), '\n')

    print('k = 4')
    cg4 = compact_gauss(copy.deepcopy(A), copy.deepcopy(b), 4)
    print(cg4)
    print(norm(cg4, solution), '\n')

    print('k = 6')
    cg6 = compact_gauss(copy.deepcopy(A), copy.deepcopy(b), 6)
    print(cg6)
    print(norm(cg6, solution), '\n')

    print('Метод Гаусса с выбором главного элемента:')

    print('k = 2')
    mg2 = gauss_main_element(copy.deepcopy(A), copy.deepcopy(b), 2)
    print(mg2)
    print(norm(mg2, solution), '\n')

    print('k = 4')
    mg4 = gauss_main_element(copy.deepcopy(A), copy.deepcopy(b), 4)
    print(mg4)
    print(norm(mg4, solution), '\n')

    print('k = 6')
    mg6 = gauss_main_element(copy.deepcopy(A), copy.deepcopy(b), 6)
    print(mg6)
    print(norm(mg6, solution), '\n')
