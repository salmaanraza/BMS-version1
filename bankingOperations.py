import dataStorage
from accountManagement import find_account
def balance(account):
    """this function show account's total balance in costumer menu"""
    print("Total balance =",account["initial_deposit"])


def deposit(account,user_account):
    """this function allow user to deposit money"""
    while True:
        deposit_input = input("Deposit: ")
        try:
            deposit_input = float(deposit_input)
            if deposit_input <= 0:
                print("Enter a valid amount greater than 0.")
                continue
            
            break
        except ValueError:
            print("Enter valid amount.")

    account["initial_deposit"] += deposit_input
    
    dataStorage.save_all_accounts(user_account)

def withdrawal(account,user_accounts):
    """this function allow user to Withdrawal money"""
    while True:
        print("Your current balance:",account["initial_deposit"])
        withdrawal_input = input("withdrawal: ")
        try:
            withdrawal_input = float(withdrawal_input)
            if withdrawal_input <= 0:
                print("Enter a valid amount greater than 0.")
                continue
            elif withdrawal_input > account["initial_deposit"] :
                print("Insufficient balance")
                print("Current balance:",account["initial_deposit"])
                continue
            
                
            break
        except ValueError:
            print("Enter valid amount.")
        

    account["initial_deposit"] -= withdrawal_input
    print("Remaining balance:",account["initial_deposit"])  
    print("Withdrawal successful.")
    dataStorage.save_all_accounts(user_accounts)

def transferMoney(account,uesr_accounts):
    print("Current balance:",account["initial_deposit"])
    while True:   
        receiver = input("Enter receiver account number: ")

        if len(receiver) != 4:
            print("Try again.\nEnter your 4 digit account number")
            continue

        receiver_account = find_account(receiver, uesr_accounts)

        if receiver_account is None:    
            print("Account number not found.")
            continue
        print("Account number found.")

        if receiver_account["account_number"] == account["account_number"]:
            print("You cannot transfer money to your own account.")
            continue
        while True:
            transfer = input("Enter amount:")
            try:
                transfer = float(transfer)
                if transfer <= 0:
                    print("Enter a valid amount greater than 0.")
                    continue
                elif transfer > account["initial_deposit"] :
                    print("Insufficient balance")
                    print("Current balance:",account["initial_deposit"])
                    continue
                elif receiver_account:
                    account["initial_deposit"] -= transfer
                    receiver_account["initial_deposit"] += transfer
                    print("Money Transfer successful")   
                    break
            except ValueError:
                print("Enter valid amount.")

        dataStorage.save_all_accounts(uesr_accounts)
        break