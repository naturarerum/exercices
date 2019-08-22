from MaxSizeList import MaxSizeList
from MaxSizeList import Account, AccountExisting

#a = MaxSizeList(3)
#a.get_list()
#print(a.get_max_size())
print("To create an account type 1, to use an existing account, type 2")
user_input = input()
if user_input == '1':
    print("enter your name : ")
    user_name = input()
    print("enter your initial deposit : ")
    user_deposit = str(input())
    new_account = Account(user_name,user_deposit)
    new_account.register_account()
    new_account.print_users_list()
elif user_input == '2':
    print("enter your name : ")
    user_name = input()
    print("enter your account number : ")
    user_account_number = input()
    existing_account = AccountExisting(user_name,user_account_number)
    if existing_account.validate_user() == True:
        print("Acces verified")
        print("print : Please chose one option : ")
        print("1. withdraw")
        print("2. Deposit") 
        print("3. display balance" )
    elif existing_account.validate_user() == False:
        print("Acces denied")