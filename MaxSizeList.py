import random


class MaxSizeList(object):
    def __init__(self, long_max):
        """constructeur"""
        self.long = long_max
        self.list_attr = []

    def get_max_size(self):
        print("maxSize :")
        return self.long

    def get_list(self):
        return self.list_attr

    def set_attrs(self, listattrs):
        pass


class Account:

    users_list = [
        ["toto", 12345, 100],
        ["Gertrude", 56857, 250],
        ["Germaine", 65325, 800]
    ]

    def __init__(self, user_name, user_deposit):
        self.user_name = user_name
        self.user_deposit = user_deposit
        self.balance = self.user_deposit

    def create_account_number(self):
        numero_compte = ''
        i = 1
        while i < 6:
            i += 1
            nombre = str((random.randint(1, 9)))
            numero_compte = numero_compte + nombre
        return numero_compte
    
    def register_account(self):
        self.account_number = self.create_account_number()
        Account.users_list.append([self.user_name, self.account_number, self.balance])

    def print_users_list(self):
        for value in Account.users_list:
            print(value)

    
class AccountExisting(Account):

    def __init__(self, user_name, account_number):
        self.account_number = account_number
        self.user_name = user_name

    def validate_user(self):
        for value in Account.users_list:
            for elem in value:
                if elem == self.user_name:
                    print('Access granted : ', elem)
                    return True
                else:  return False
            