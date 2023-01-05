import unittest
from datetime import datetime
from Bank import Customer, BankAccount
import sys

sys.path.append('../Initial_project')


class FunctionsTest(unittest.TestCase):
    def setUp(self):
        self.akbar = Customer('Akbar', 'Babaii', '09123456789', 'akbar@gmail.com')
        self.asgar = ('Asqar', 'Rezaii', '09123456788', 'asqar@gmail.com')
        self.akbar_acc = BankAccount(self.akbar, 20000)
        self.asgar_acc = BankAccount(self.asgar, 1000000)

    def test_get_balance(self):
        self.assertEqual(20000 - 600, self.akbar_acc.get_balance(), "موجودی درست نمایش داده نمیشود.")
        self.assertEqual(1000000 - 600, self.asgar_acc.get_balance(), "موجودی درست نمایش داده نمیشود.")

    def test_deposit(self):
        self.akbar_acc.deposit(2500)
        self.assertEqual(20000 + 2500 - 600, self.akbar_acc.get_balance(), "واریز ب حساب ب درستی صورت نمیگیرد.")
        self.asgar_acc.deposit(2500)
        self.assertEqual(1000000 + 2500 - 600, self.asgar_acc.get_balance(), "واریز ب حساب ب درستی صورت نمیگیرد.")

    def test_withdraw(self):
        self.akbar_acc.withdraw(1000)
        self.assertEqual(20000 - 1000 - 600 - 600, self.akbar_acc.get_balance(),
                         "برداشت ب درستی صورت نمیگیرد.")
        self.asgar_acc.withdraw(1000)
        self.assertEqual(1000000 - 1000 - 600 - 600, self.asgar_acc.get_balance(),
                         "برداشت ب درستی صورت نمیگیرد.")

    def test_transfer(self):
        self.akbar_acc.transfer(self.asgar_acc, 2000)
        self.assertEqual(20000 - 600 - 2000 - 600, self.akbar_acc.get_balance(), "موجودی درست نمایش داده نمیشود.")
        self.assertEqual(1000000 - 600 + 2000, self.asgar_acc.get_balance(), "موجودی درست نمایش داده نمیشود.")


if __name__ == '__main__':
    unittest.main()
