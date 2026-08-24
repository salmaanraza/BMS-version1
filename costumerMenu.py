import bankingOperations as bs
def costumer_menu(account,user_accounts):
    """this function print costumer menu after successful login"""
    while True:

        print("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          CUSTOMER MENU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Account Details
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. Logout

━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
             print("Account details")
             print(f"""Name:{account["name"]}
password:{account["password"]}
balance:{account["initial_deposit"]}""")
             if account["blocked"]:
                status = "Blocked"
             else:
                status = "Active"

             print("Account Status:", status)

        elif user_choice == "2":
             print("Account balance")
             bs.balance(account)
        elif user_choice == "3":
             print("Deposit Money")
             bs.deposit(account,user_accounts)
        elif user_choice == "4":
             print("Withdraw Money")
             bs.withdrawal(account,user_accounts)

        elif user_choice == "5":
             print("Transfer Money")
             bs.transferMoney(account,user_accounts)

        
        elif user_choice == "6":
            print("Logout")
            break
        else:
            print("Invalid choice")
        
            