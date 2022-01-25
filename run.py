#!/usr/bin/env python3.9
from ast import While
from account import Account
from password import Password

# Account class


def create_account(first_name, last_name, username, password):
    account = Account(first_name, last_name, username, password)
    return account


def save_account(account):
    ''' 
    Function to save contact
    '''
    account.save_account()


def delete_account(account):
    ''' 
    Function to delete contact
    '''
    account.delete_account()


def find_account(username):
    ''' 
    Function to find contact by username
    '''
    return Account.find_by_username(username)


def exist_account(username):
    ''' 
    Function to show contact exist
    '''
    return Account.account_exists(username)


def display_account():
    ''' 
    Function to display contact 
    '''
    return Account.display_account()

# Password Class


def create_site(site, password):
    passwords = Password(site, password)
    return passwords


def save_site(passwords):
    passwords.save_site()


def delete_site(passwords):
    passwords.delete_site()


def display_sites():
    return Password.display_sites()

 # Main function


def main():
    print('Welcome  To Prime Password Locker')
    print('/˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜')
    print('Kindly reply with below Numbers for an Option')

    while True:

        print('1) Display Accounts \n 2 Login \n 3) Create Account \n 4) Exit')

        option = int(input())
        if option == 2:
            print('Enter your username')
            username = input()
            print('Énter your password')
            password = input()
            account = find_account(username)
            if account.username == username and account.password == password:

                print('Logged in Successfully')
                while True:
                    print(
                        f'Welcome {username}, Kindly reply with below Numbers for an Option')

                    print(
                        '1) Save new Password \n 2) Display Saved Password \n 3) Delete Password \n 4) Exit')
                    log_option = int(input())
                    if log_option == 1:
                        print('New site')
                        print('˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜')

                        print('Enter Site Name')
                        site = input()

                        print('Enter password')
                        password = input()

                        save_site(create_site(site, password))
                    elif log_option == 2:
                        if display_sites():
                            for page in display_sites():
                                print(f'{page.site}:{page.paseword}')
