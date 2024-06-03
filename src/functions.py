"""functions"""
import random


def factorial(n: int) -> int:
    """a function calculating factorial"""
    cur = 1
    for i in range(1, n + 1):
        cur *= i
    return cur


def hatred_s(s: str):
    """delete all s's"""
    string = s[:].replace('s', ' hate! ')
    return string


def destined_tea():
    """it will choose your tea"""
    tea = random.choice(['black', 'green'])
    return tea


def what_the_animal_says(s):
    """no comment"""
    match s:
        case 'dog':
            return 'bark'
        case 'cat':
            return 'meow'
        case 'duck':
            return 'crack'
        case _:
            return 'incorrect animal'
