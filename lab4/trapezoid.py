import math


def f(x):
    return math.sqrt(1 + math.sin(x))


def trapezoid(a, b):
    return ((b - a) / 2) * (f(a) + f(b))


def calculate_trapezoid(points):
    res = 0
    for i in range(len(points) - 1):
        res += trapezoid(points[i], points[i + 1])
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
    return 1 / 3.0 * (s_2 - s_1)


if __name__ == '__main__':
    values_01 = get_values(0, 1, 0.1)
    values_005 = get_values(0, 1, 0.05)
    middle_rect_01 = calculate_trapezoid(values_01)
    middle_rect_005 = calculate_trapezoid(values_005)

    print("Метод трапеций для шага h={0}  = {1}".format(0.1, middle_rect_01))
    print("               для шага h={0} = {1}".format(0.05, middle_rect_005))
    print("Погрешность Рунге для метода трапеций: {0}".format(
        runge_inaccuracy(middle_rect_01, middle_rect_005)))