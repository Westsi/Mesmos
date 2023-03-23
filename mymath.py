import math


def sec(v):
    return 1 / (math.cos(v))


def csc(v):
    return 1 / (math.sin(v))


def cot(v):
    return 1 / (math.tan(v))


def asec(v):
    return math.acos(1 / v)


def acsc(v):
    return math.asin(1 / v)


def acot(v):
    return math.atan(1 / v)


def sech(v):
    return 1 / (math.cosh(v))


def csch(v):
    return 1 / (math.sinh(v))


def coth(v):
    return 1 / (math.tanh(v))


def asech(v):
    return math.acosh(1 / v)


def acsch(v):
    return math.asinh(1 / v)


def acoth(v):
    return math.atanh(1 / v)
