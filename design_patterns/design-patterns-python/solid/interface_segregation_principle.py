# Interface Segregation Principle
"""
The Interface Segregation Principle is simple: don't throw everything in
the kitchen sink into an interface because then all its users will have
to implement things they do not need. Instead, split the interface into
several smaller ones.
"""

from abc import abstractmethod


class Machine:  # not good.
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        """Not supported."""
        raise NotImplementedError('Printer cannot scan!')


# #######

class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class PhotoCopier(Printer, Scanner):
    def print(self, doc):
        pass

    def scan(self, doc):
        pass


class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def print(self, doc):
        pass

    @abstractmethod
    def scan(self, doc):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner, fax):
        self.scanner = scanner
        self.printer = printer
        self.fax = fax

    def print(self, doc):
        self.printer.print(doc)

    def scan(self, doc):
        self.scanner.scan(doc)

    def fax (self, doc):
        self.fax.fax(doc)


if __name__ == '__main__':
    pass
