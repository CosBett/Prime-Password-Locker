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


def isexits_account(username):
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


def find_site(page):
    return Password.find_by_site(page)


def isexist_site(page):
    return Password.site_exists(page)


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
        if option == 1:
            if display_account():
                for account in display_account():
                    print(f'{account.username}')
            else:
                print('No Accounts Found')

        elif option == 2:
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
                    login_option = int(input())
                    if login_option == 1:
                        print('New site')
                        print('˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜')

                        print('Enter Site Name')
                        site = input()

                        print('Enter password')
                        password = input()

                        save_site(create_site(site, password))
                    elif login_option == 2:
                        if display_sites():
                            for page in display_sites():
                                print(f'{page.site}:{page.paseword}')
                        else:
                            print('No password saved for this site!')
                            print('\n')

                    elif login_option == 3:
                        print('Please enter the name of site to delete')

                        page = input()
                        if isexist_site(site):
                            remove_site = (site)
                            delete_site(remove_site)

                        else:
                            print(
                                f'Above {site} is not found, Enter a saved site to delete')
                    elif login_option == 4:
                        print('Thank you, Bye')
                        break
            else:
                print('Incorrect Username or password!')

        elif option == 3:
            print('New Account')
            print('˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜')

            print('Enter your First Name')
            first_name = input()

            print('Enter your Last_Name')
            last_name = input()

            print('Enter Username')
            username = input()

            print('Enter your Password')
            password = input()

            save_account(create_account(
                first_name, last_name, username, password))
            print('Account has been created!')
            while True:
                print(
                    f'Welcome {username} Kindly reply with below Numbers for an Option')

                print(
                    '1) Save new Password \n 2) Display Saved Password \n 3) Delete Password \n 4) Exit')
                login_option = int(input())
                if login_option == 1:
                    print('New site')
                    print('˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜')

                    print('Enter Site Name')
                    site = input()

                    print('Enter password')
                    password = input()

                    save_site(create_site(site, password))
                elif login_option == 2:
                    if display_sites():
                        for page in display_sites():
                            print(f'{page.site}:{page.paseword}')
                    else:
                        print('No password saved for this site!')
                        print('\n')

                elif login_option == 3:
                    print('Please enter the name of site to delete')

                    page = input()
                    if isexist_site(site):
                        remove_site = (site)
                        delete_site(remove_site)

                    else:
                        print(
                            f'Above {site} is not found, Enter a saved site to delete')
                elif login_option == 4:
                    print('Thank you, Bye')
                    break
