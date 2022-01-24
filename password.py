class Password:
    def __init__(self, site, password):
        self.site = site
        self.password = password

    passwords_list = []       # password list for site added

    def save_site(self):
        '''
        This function save new sites and passwords 
        '''
        Password.passwords_list.append(self)

    def delete_site(self):
        '''
        this function enable user to delete saved site 
        '''
        Password.passwords_list.remove(self)
