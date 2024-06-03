"""test"""
import src.functions


def test_factorial():
    """test"""
    assert src.functions.factorial(5) == 120
    assert src.functions.factorial(0) == 1


def test_hatred_s():
    """test"""
    assert (src.functions.hatred_s('s is the worst letter')
            == ' hate!  i hate!  the wor hate! t letter')


def test_destined_tea():
    """test"""
    assert src.functions.destined_tea() != 'coffee'


def test_what_the_animal_says():
    """test"""
    assert src.functions.what_the_animal_says('cat') == 'meow'
    assert src.functions.what_the_animal_says('dog') != 'meow'
