class Account:
    '''
    Class that generates new instances of account
    '''
    accounts_list = []  # Empty accounts list to store the accounts created

    def __init__(self, first_name, last_name, username, password):  # New instances and variables
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_account(self):
        '''
        save_account function saves account objects into accounts_list
        '''

        Account.accounts_list.append(self)

    def delete_account(self):
        '''
        delete_account function remove account objects from accounts_list
        '''

        Account.accounts_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        '''
        This function allow a user to search account by username and return back the account
        '''
        for account in cls.accounts_list:
            if account.username == username:
                return account

    @classmethod
    def account_exists(cls, username):
        '''
        This function checks if the username exist in the stored list of accounts
        '''
        for account in cls.accounts_list:
            if account.username == username:
                return True
        return False
