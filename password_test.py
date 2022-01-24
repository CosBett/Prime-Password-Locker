import unittest
from password import Password


class TestPaswords(unittest.TestCase):
    def setUp(self):
        '''
        This function creates a new instance of the password class before every given test
        '''
        self.new_password = Password('gitHub', '11111')

    def tearDown(self):
        '''
        This function ensures that the password list array is cleared before every test
        '''
        Password.passwords_list = []

    def test_init(self):
        '''
        Function test if the data entered will appear when the function is called
        '''
        self.assertEqual(self.new_password.site, 'gitHub')
        self.assertEqual(self.new_password.password, '11111')

    def test_save_site(self):
        '''
        function that check if the added value is taken in the list
        '''
        self.new_password.save_site()
        self.assertEqual(len(Password.passwords_list), 1)

    def test_save_multiple_site(self):
        '''
        This function checks if the sites entered were added to the list
        '''
        self.new_password.save_site()
        test_pass = Password('Netlify', '22222')
        test_pass.save_site()
        self.assertEqual(len(Password.passwords_list), 2)

    def test_delete_site(self):
        '''
        this  checks the delete function
        '''
        self.new_password.save_site()
        test_pass = Password('Netlify', '22222')
        test_pass.save_site()
        self.new_password.delete_site()
        self.assertEqual(len(Password.passwords_list), 1)


if __name__ == '__main__':
    unittest.main()
