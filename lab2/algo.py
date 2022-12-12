from common import *


class Dichotomies:
    @staticmethod
    def flfr(l, r):
        return f(l) * f(r)

    @staticmethod
    def solve():
        l = a
        r = b
        m = (l + r) / 2
        iteration = math.ceil(math.log2((b - a) / epsilon))
        for i in range(iteration):
            m = (l + r) / 2
            if Dichotomies.flfr(l, m) < 0:
                r = m
            else:
                l = m
        return m, iteration


class Newton:
    @staticmethod
    def find_next_x(x):
        return x - (f(x) / df(x))

    @staticmethod
    def solve():
        iteration = 0
        x = x0
        while True:
            iteration += 1
            next_x = Newton.find_next_x(x)
            if abs(next_x - x) <= epsilon:
                return next_x, iteration
            x = next_x


class ModNewton:
    @staticmethod
    def find_next_x(x):
        return x - (f(x) / df(x0))

    @staticmethod
    def solve():
        iteration = 0
        x = x0
        while True:
            iteration += 1
            next_x = ModNewton.find_next_x(x)
            if abs(next_x - x) <= epsilon:
                return next_x, iteration
            x = next_x


class Chord:
    @staticmethod
    def find_next_x(x):
        return x - ((f(x) * (x - x0)) / (f(x) - f(x0)))

    @staticmethod
    def solve():
        iteration = 1
        x = a  # x1
        while True:
            iteration += 1
            next_x = Chord.find_next_x(x)
            if abs(f(next_x)) / m < epsilon:
                return next_x, iteration
            x = next_x


class MovChord:
    @staticmethod
    def find_next_x(prev_x, x):
        return x - ((f(x) * (x - prev_x)) / (f(x) - f(prev_x)))

    @staticmethod
    def solve():
        iteration = 1
        prev_x = x0
        x = a  # x1
        while True:
            iteration += 1
            next_x = MovChord.find_next_x(prev_x, x)
            if abs(f(next_x)) / m < epsilon:
                return next_x, iteration
            prev_x = x
            x = next_x


class SipleIteration:
    @staticmethod
    def solve():
        iteration = 0
        x = x0
        while True:
            iteration += 1
            next_x = fi(x)
            if abs(next_x - x) / m < epsilon:
                return next_x, iteration
            x = next_x
