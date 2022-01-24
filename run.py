#!/usr/bin/env python3.9
from account import Account
from password import Password


def create_account(first_name, last_name, username, password):
    account = Account(first_name, last_name, username, password)
    return account


def save_account(account):
    account.save_account()


def delete_account(account):
    account.delete_account()


def find_account(username):
    return Account.find_by_username(username)
