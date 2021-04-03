class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Person: {self.name} with id as {self.id}"


class PersonFactory:
    current_id = 0

    def create_person(self, name):
        person = Person(self.current_id, name)
        self.current_id += 1
        return person


if __name__ == '__main__':
    pf = PersonFactory()
    person1 = pf.create_person("Salman")
    person2 = pf.create_person("shahrukh")
    print(person1)
    print(person2)