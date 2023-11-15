def fizz_buzz(arg: int):
    if arg <= 0:
        return "Fizz buzz failed"


    elif arg % 3 != 0 and arg % 5 != 0:
        return arg

    elif arg % 3 == 0 and arg % 5 != 0:
        return "Fizz"

    elif arg % 3 != 0 and arg % 5 == 0:
        return "Buzz"

    elif arg % 3 == 0 and arg % 5 == 0:
        return "FizzBuzz"


def test_fizz_buzz():
    assert fizz_buzz(-3) == "Fizz buzz failed"
    assert fizz_buzz(2) == 2
    assert fizz_buzz(6) == "Fizz"
    assert fizz_buzz(10) == "Buzz"
    assert fizz_buzz(15) == "FizzBuzz"
