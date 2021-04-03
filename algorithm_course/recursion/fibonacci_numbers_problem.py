

def fibonacci_head(num: int) -> int:

    if num == 0:
        return 0
    if num == 1:
        return 1

    # recursion
    _result1 = fibonacci_head(num - 1)
    _result2 = fibonacci_head(num - 2)

    return _result1 + _result2


def fibonacci_tail(num: int, a: int = 0, b: int = 1) -> int:

    if num == 0:
        return a
    if num == 1:
        return b

    return fibonacci_tail(num - 1, b, a+b)


def fibonacci_iteration_upto(num: int) -> int:
    a, b = 0, 1

    while a < num:
        print(a, end=", ")
        a, b = b, a + b

    return a


if __name__ == '__main__':
    print("fib(20) -> ", fibonacci_head(20))
    print("fib(10) -> ", fibonacci_head(10))

    print("fib(20) -> ", fibonacci_tail(20))
    print("fib(10) -> ", fibonacci_tail(10))

    print("fib after (2000) -> ", fibonacci_iteration_upto(2000))
    print("fib after (100) -> ", fibonacci_iteration_upto(100))