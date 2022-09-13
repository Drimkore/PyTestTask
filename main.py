def func_float_one(x):
    return int(x)


def func_float_two(x, y):
    return x+y


def func_float_three(x, y):
    return type(x/y)


def test_float_one():
    try:
        assert float(func_float_one(10)**309)
    except OverflowError:
        pass


def test_float_two():
    try:
        assert func_float_two(0.1, 0.2) == 0.3
    except AssertionError:
        pass


def test_float_three():
    assert func_float_three(1, 5) == float


s = {'q', 'w', 'e', 'r'}


def test_set_one():
    a = 'a'
    try:
        assert a in s
    except AssertionError:
        pass


def test_set_two():
    assert type(s) == set


def test_set_three():
    one_set = {1, 2, 3, 4}
    two_set = {3, 4, 5, 6}
    assert one_set & two_set == {3, 4}

