import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {int((end-start)*1000)}ms')
        return result
    return wrapper


def some_op():
    print('Starting op...')
    time.sleep(1)
    print('We are done!')
    return 123


@time_it
def some_op2():
    print('Starting op...')
    time.sleep(1)
    print('We are done!')
    return 123


if __name__ == '__main__':
    some_op()

    time_it(some_op)()
    # some op2
    some_op2()