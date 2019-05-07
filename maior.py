def maximo(x, y, z):
    if x > y and x > z:
        return x
    if x < y and y > z:
        return y
    if z > y and x < z:
        return z
    if x == y and x == z:
        return x 

def test_maximo_2():
    assert maximo(2, 1, 0) == 2
def test_maximo_1():
    assert maximo(-1, 1, 0) == 1
def test_maximo_negativo():
    assert maximo(-3, -2, -1) == -1
def test_maximo_0():
    assert maximo(-1, 0, -5) == 0
def test_maximo_igual():
    assert maximo(0, 0, 0) == 0