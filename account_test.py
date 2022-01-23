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

        self.assertEqual(self.new_contact.first_name, "Cosmas")
        self.assertEqual(self.new_contact.last_name, "Bett")
        self.assertEqual(self.new_contact.username, "Prime")
        self.assertEqual(self.new_contact.password, "M@2021")
