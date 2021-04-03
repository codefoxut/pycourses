
class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.combination = ''.join([str(i) for i in combination])

    def reset(self):
        self.status = ''

    def enter_digit(self, digit):
        if self.status in ['LOCKED', 'ERROR']:
            self.reset()

        self.status += str(digit)
        if not self.combination.startswith(self.status):
            self.status = 'ERROR'

        if self.combination == self.status:
            self.status = 'OPEN'


if __name__ == '__main__':
    cl = CombinationLock([1, 2, 3, 4, 5])
    print(cl.status)
    cl.enter_digit(1)
    print(cl.status)
    cl.enter_digit(23)
    print(cl.status)
    cl.enter_digit(45)
    print(cl.status)

    cl2 = CombinationLock([7, 8, 6])
    print(cl2.status)
    cl2.enter_digit(7)
    print(cl2.status)
    cl2.enter_digit(9)
    print(cl2.status)
