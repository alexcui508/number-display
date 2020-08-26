import math


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True