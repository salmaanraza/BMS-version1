import accountManagement as am
import dataStorage  

def login(user_accounts):
    """this function enable user to login to there account"""


    while True:
        user_account_number = input("Enter account number: ")
        password = input("Enter account password: ")

        if len(user_account_number) != 4:
            print("Try again.\nEnter your 4 digit account number")
            continue
        elif len(password) != 6:
            print("Try again.\nEnter your 6 digit account password")
            continue
        
        account = am.find_account(user_account_number, user_accounts)

        if account:
            print("Account found.")

            if account["blocked"]:
                print("""Account is blocked.
Please contact the bank administrator..""")
                break
        else:
            print("Account not found")
            continue
        if account["password"] == password:
            print("Login successful.")
            account["failed_attempts"] = 0
            account["blocked"] = False
            dataStorage.save_all_accounts(user_accounts)
            return account
            
        else:
            print("wrong password")
            account["failed_attempts"]+=1
            if account["failed_attempts"] == 5:
                account["blocked"] = True
                print("Account blocked")
                
                dataStorage.save_all_accounts(user_accounts)
                return None
                
        dataStorage.save_all_accounts(user_accounts)