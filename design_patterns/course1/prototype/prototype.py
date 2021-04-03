import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


if __name__ == '__main__':
    print('----step1---')
    address1 = Address('123 london road', 'london', 'UK')
    john = Person('John', address1)
    print(john)
    jane1 = john
    jane1.name = 'Jane'
    print(john, '\n', jane1)
    print('----step2---')
    john = Person('John', address1)
    jane2 = Person('Jane', address1)
    print(john, '\n', jane2)
    jane2.address.street_address = '123b london road'
    print('after address change.')
    print(john, '\n', jane2)
    print('----step3---')
    address2 = Address('123 london road', 'london', 'UK')
    john = Person('John', address2)
    jane3 = copy.deepcopy(john)
    jane3.name = 'Jane'
    jane3.address.street_address = '123b london road'
    print(john, '\n', jane3)