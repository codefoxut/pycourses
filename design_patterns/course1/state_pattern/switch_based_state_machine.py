
from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


def unlock_the_lock():
    code = '1234'
    state = State.LOCKED
    entry = ''

    while True:
        if state == State.LOCKED:
            entry += input(entry)

            if entry == code:
                state = State.UNLOCKED

            if not code.startswith(entry):
                state = State.FAILED
        elif state == State.FAILED:
            print('\nFailed')
            entry = ''
            state = State.LOCKED
        elif state == state.UNLOCKED:
            print('\nUNLOCKED')
            break


if __name__ == '__main__':
    unlock_the_lock()