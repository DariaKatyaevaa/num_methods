from algo import *

# метод половинного деления(дихотомии)
result, iteration = Dichotomies().solve()
print('метод половинного деления(дихотомии)', result)
print(iteration)

# метод Ньютона
result, iteration = Newton().solve()
print('метод Ньютона', result)
print(iteration)

# метод модифицированный Ньютона
result, iteration = ModNewton().solve()
print('метод модифицированный Ньютона', result)
print(iteration)

# метод хорд
result, iteration = Chord().solve()
print('метод хорд', result)
print(iteration)

# метод подвижных хорд
result, iteration = MovChord().solve()
print('метод подвижных хорд', result)
print(iteration)

# метод простой итерации
result, iteration = SipleIteration().solve()
print('метод простой итерации', result)
print(iteration)
