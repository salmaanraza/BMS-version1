import json
def save_accounts(account_details):
            with open("E:/python/projects/BankingManagementSystemVersion1/data/accounts.json", "r") as file:
                user_account = json.load(file)

            user_account.append(account_details)
            
            with open("E:/python/projects/BankingManagementSystemVersion1/data/accounts.json", "w") as file:
                json.dump(user_account, file, indent=5)


def load_accounts():
    with open("E:/python/projects/BankingManagementSystemVersion1/data/accounts.json", "r") as file:
      user_account = json.load(file)
    return user_account

def save_all_accounts(user_accounts):
    with open("data/accounts.json", "w") as file:
        json.dump(user_accounts, file, indent=5)