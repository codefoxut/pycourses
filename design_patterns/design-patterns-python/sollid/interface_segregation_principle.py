# ISP
from abc import abstractmethod


class Machine:
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

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, doc):
        pass

    @abstractmethod
    def scan(self, doc):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, doc):
        self.printer.print(doc)

    def scan(self, doc):
        self.scanner.scan(doc)






if __name__ == '__main__':
    pass