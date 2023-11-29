import math


# 2. В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot.
# Чем больше тестов на каждую функцию - тем лучше

def test_pi():
    assert math.pi == 3.141592653589793


def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(math.pi) == math.pi ** 0.5


def test_pow():
    assert math.pow(9, 2) == 81
    assert math.pow(math.pi, math.pi) == math.pi**math.pi

def test_hypot():
    x=math.e
    y=math.pi
    assert math.hypot(x,y) == math.sqrt(x * x + y * y)