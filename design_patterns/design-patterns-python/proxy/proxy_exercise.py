class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    def drink(self):
        if self.person.age < 18:
            return "too young"
        else:
            return self.person.drink()

    def drive(self):
        if self.person.age < 16:
            return "too young"
        else:
            return self.person.drive()

    def drink_and_drive(self):
        return "dead"


if __name__ == '__main__':
    person = Person(30)
    rp = ResponsiblePerson(person)
    print(rp.drive())
    print(rp.drink_and_drive())
