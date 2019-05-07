def fizzbuzz(n):
    if n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    if n % 3 != 0 and n % 5 == 0:
        return "Buzz"
    if n % 3 == 0 and n % 5 == 0 and n != 0:
        return "FizzBuzz"
    if n % 3 != 0 and n % 5 != 0 or n == 0:
        return n



def test_fizzbuz0():
    assert fizzbuzz(0) == 0
def test_fizzbuz9():
    assert fizzbuzz(9) == "Fizz"
def test_fizzbuz10():
    assert fizzbuzz(10) == "Buzz"
def test_fizzbuz15():
    assert fizzbuzz(15) == "FizzBuzz"
def test_fizzbuz1241():
    assert fizzbuzz(1241) == 1241 
