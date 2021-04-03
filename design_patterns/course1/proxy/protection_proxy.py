
class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car is being driven by {self.driver}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver too young')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


if __name__ == '__main__':
    driver = Driver('John', 55)
    car = Car(driver)
    car.drive()

    car = CarProxy(driver)
    car.drive()

    driver2 = Driver('Jane', 15)
    car = Car(driver2)
    car.drive()

    car = CarProxy(driver2)
    car.drive()

