import accountManagement as am
import auth
import dataStorage
import costumerMenu as cm
user_accounts = dataStorage.load_accounts()
while True:
    print("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            🏦 BANKING MANAGEMENT SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    MAIN MENU
    1. Create Account
    2. Login
    3. Exit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

    choice = input("Enter your choice: ")

    if (choice == "1"):
        print("Welcome to our BANK")
        print("Create your account.")
        new_account = am.create_accounts(user_accounts)
        user_accounts.append(new_account)



    elif (choice == "2"):

        print("Add your accound number below")
        login = auth.login(user_accounts)
        if login:
            cm.costumer_menu(login,user_accounts)
        

    elif (choice == "3"):


        print("Exit")
        print("Thanks for coming")
        break
