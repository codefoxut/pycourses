
class Mediator(list):
    pass


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.append(self)

    def say(self, value):
        for p in self.mediator:
            if p is not self:
                p.value += value


if __name__ == '__main__':
    m1 = Mediator()
    p1 = Participant(m1)
    p2 = Participant(m1)
    p1.say(3)
    p2.say(5)
    print(p1.value, p2.value)