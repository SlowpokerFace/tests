from src.functions import *


def test_factorial():
    """test"""
    assert factorial(5) == 120
    assert factorial(0) == 1


def test_hatred_s():
    """test"""
    assert hatred_s('s is the worst letter') == ' hate!  i hate!  the wor hate! t letter'


def test_destined_tea():
    """test"""
    assert destined_tea() != 'coffee'


def test_what_the_animal_says():
    """test"""
    assert what_the_animal_says('cat') == 'meow'
    assert what_the_animal_says('dog') != 'meow'
