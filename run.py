#!/usr/bin/env python3.9
from account import Account
from password import Password


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
