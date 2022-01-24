#!/usr/bin/env python3.9
from account import Account
from password import Password


def create_account(first_name, last_name, username, password):
    account = Account(first_name, last_name, username, password)
    return account
