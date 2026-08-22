import accountManagement as am

def login(user_accounts):
    """this function enable user to login to there account"""


    while True:
        user_account_number = input("Enter account number: ")

        if len(user_account_number) != 4:
            print("Try again.\nEnter your 4 digit account number")
            continue
        account = am.find_account(user_account_number, user_accounts)

        if account:
            print("Account number accepted.")
            
            break
        else:
            print("Account not found.")