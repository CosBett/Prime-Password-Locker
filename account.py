class Account:
    '''
    Class that generates new instances of account
    '''
    user_accounts = []

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = username
        self.password = password
