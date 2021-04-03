

def factorial_head(num: int) -> int:
    if num == 0:
        return 1

    # use recursion
    _result = factorial_head(num-1)

    # some operations
    return num * _result


def factorial_tail(num: int, accumulator: int = 1) -> int:
    if num == 1:
        return accumulator

    return factorial_tail(num - 1, accumulator * num)


if __name__ == '__main__':
    print("factorial(5) -> ", factorial_head(5))
    print("factorial(10) -> ", factorial_head(10))

    print("factorial(5) -> ", factorial_tail(5))
    print("factorial(10) -> ", factorial_tail(10))