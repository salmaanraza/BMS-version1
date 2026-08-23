import random as rn
import dataStorage 
import auth

def account_number_generater(user_accounts):
    """this function creates four digit unique account number"""

    random_number = str(rn.randint(1000, 9999))

    while find_account(random_number, user_accounts) is not None:
        random_number = str(rn.randint(1000, 9999))

    return random_number
    
def create_accounts(user_accounts):
        """this function take user's name,password,initial deposit as input and validate them """
        while True:

            name = input("Enter your name: ").strip()
            validate_name = name.replace(" ","")
            if validate_name.isalpha():  

                break
            print("⚠️  Enter valid name")  
        print(f"Hello {name}")

        while True:           
            password =input("Enter your Password: ")
            length_of_password = len(password)
            if length_of_password < 6:
                print("Enter a strong password.")
            elif length_of_password > 6:
                print("password length must be 6 characters")
            else :
                print("Password accepted!")
                break

    
        while True:
            initial_deposit = input("Enter initial deposit: ")
            if initial_deposit == "":
                print("intial deposit = 0")
                initial_deposit = "0"
                
            try:
                initial_deposit = float(initial_deposit)
                if initial_deposit < 0:
                  print("Enter valid amount.")
                  continue                 
                
            except ValueError:
                print("Enter valid amount.")

            else:
                print("Deposit successfully")
                break
        account_number = account_number_generater(user_accounts)
        print("Your account number is:",account_number)

        new_account = account_details(name, password, account_number, initial_deposit)

        return new_account


def account_details(name,password,account_number,initial_deposit):
    """this function take name,password account number and init deposit as parameters and store them in dictionary"""
    account_details = {
        "name": name,
        "password": password,
        "account_number": account_number,
        "initial_deposit": initial_deposit,
        "failed_attempts":0,
        "blocked": False

    }
    dataStorage.save_accounts(account_details)
    return account_details

def find_account(account_number, user_accounts):

    for i in user_accounts:

        if account_number == i["account_number"]:
            return i

    return None
