from cgi import test
import unittest  # Importing the unittest module
from account import Account


class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account(
            "Cosmas", "Bett", "Prime", "M@2021")  # create Account object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name, "Cosmas")
        self.assertEqual(self.new_account.last_name, "Bett")
        self.assertEqual(self.new_account.user_name, "Prime")
        self.assertEqual(self.new_account.password, "M@2021")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Account.accounts_list = []

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the accounts list
        '''
        self.new_account.save_account()  # saving the new account
        self.assertEqual(len(Account.accounts_list), 1)

    def test_delete_account(self):
        '''
        This method is to test if we can remove an account from our accounts list
        '''

        self.new_account.save_account()
        test_account = Account(
            "Cosmas", "Bett", "Prime", "M@2021")

        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(Account.accounts_list), 1)


if __name__ == '__main__':
    unittest.main()
