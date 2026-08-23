def costumer_menu(account):
    while True:

        print("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            CUSTOMER MENU
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

        elif user_choice == "3":
             print("Deposit Money")

        elif user_choice == "4":
             print("Withdraw Money")

        elif user_choice == "5":
             print("Transfer Money")

        else:
             print("Logout")
        break
        
            