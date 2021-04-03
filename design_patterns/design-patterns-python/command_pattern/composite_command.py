import unittest

from .command_pattern import Command, BankAccount, BankAccountCommand


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=None):
        super().__init__()
        for i in items or []:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):

    def __init__(self, from_acc, to_acc, amount):
        super().__init__([
            BankAccountCommand(
                from_acc, BankAccountCommand.Action.WITHDRAW, amount
            ),
            BankAccountCommand(
                to_acc, BankAccountCommand.Action.DEPOSIT, amount
            )
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False

        self.success = ok


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        dep1 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 100
        )
        dep2 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 50
        )
        composite = CompositeBankAccountCommand(
            [dep1, dep2]
        )
        composite.invoke()
        print(ba)
        composite.undo()
        print(ba)

    def test_transfer_fail(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amt = 600
        wd = BankAccountCommand(
            ba1, BankAccountCommand.Action.WITHDRAW, amt
        )
        dp = BankAccountCommand(
            ba2, BankAccountCommand.Action.DEPOSIT, amt
        )
        transfer = CompositeBankAccountCommand([wd, dp])
        transfer.invoke()
        print("ba1", ba1)
        print("ba2", ba2)
        transfer.undo()
        print("ba1", ba1)
        print("ba2", ba2)

    def test_better_transfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amt = 700
        transfer = MoneyTransferCommand(ba1, ba2, amt)
        transfer.invoke()
        print(f'ba1: {ba1}, ba2: {ba2}')
        transfer.undo()
        print(f'ba1: {ba1}, ba2: {ba2}')
        print(transfer.success)


if __name__ == '__main__':
    unittest.main()
