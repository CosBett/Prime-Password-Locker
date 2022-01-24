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

    @classmethod
    def display_sites(cls):
        '''
        Function to display sites and passwords
        '''
        return cls.passwords_list

    @classmethod
    def find_by_site(cls, site_find):
        '''
        Function to enable user to look for password using the site value
        '''
        for sitefind in cls.passwords_list:
            if sitefind.site == site_find:
                return sitefind

    @classmethod
    def site_exists(cls, site_find):
        for sitefind in cls.passwords_list:
            if sitefind.site == site_find:
                return sitefind
        return False
