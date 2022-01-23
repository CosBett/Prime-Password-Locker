class Account:
    '''
    Class that generates new instances of account
    '''
    accounts_list = []  # Empty accounts list to store the accounts created

    def __init__(self, first_name, last_name, username, password):  # New instances and variables
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = username
        self.password = password

    def save_account(self):
        '''
        save_account method saves account objects into accounts_list
        '''

        Account.accounts_list.append(self)

    def delete_account(self):
        '''
        delete_account method remove account objects from accounts_list
        '''

        Account.accounts_list.remove(self)
