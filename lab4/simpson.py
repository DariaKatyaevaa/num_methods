import math


def f(x):
    return math.sqrt(1 + math.sin(x))


def simpson(a, b):
    return ((b - a) / 6) * (f(a) + 4 * f((a + b) / 2) + f(b))


def calculate_simpson(points):
    res = 0
    for i in range(len(points) - 1):
        res += simpson(points[i], points[i + 1])
    return res


def get_values(a, b, step):
    scope = int(round((b - a) / step))
    res = []
    x = a
    for i in range(scope):
        res.append(x)
        x += step
    if res[len(res) - 1] != b:
        res.append(b)
    return res


def runge_inaccuracy(s_2, s_1):
    return 1 / 15.0 * (s_2 - s_1)


if __name__ == '__main__':
    values_01 = get_values(0, 1, 0.1)
    values_005 = get_values(0, 1, 0.05)
    simpson_01 = calculate_simpson(values_01)
    simpson_005 = calculate_simpson(values_005)

    print("Метод Симпсона для шага h={0}  = {1}".format(0.1, simpson_01))
    print("               для шага h={0} = {1}".format(0.05, simpson_005))
    print("Погрешность Рунге для метода Симпсона: {0}".format(runge_inaccuracy(simpson_01, simpson_005)))
