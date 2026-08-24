Yes — the current README is trying to show the **architecture/data flow visually**, but it has become difficult to read. For GitHub, I would replace that diagram-heavy content with a structured README using the exact sections you listed.

Below is a **clean README written specifically for your current BMS**, without claiming features you haven't implemented.

````markdown
# 🏦 Banking Management System

A command-line Banking Management System built with Python.

This project is designed to simulate the basic operations of a banking system while applying Python concepts such as functions, modules, lists, dictionaries, JSON file handling, input validation, exception handling, authentication, and persistent data storage.

---

## 📌 Project Name

**Banking Management System (BMS)**

---

## 📌 Requirements

The system is designed to:

- Create customer accounts
- Generate a unique 4-digit account number
- Store customer account information
- Allow customers to log in using their account number and password
- Track failed login attempts
- Block an account after 5 incorrect password attempts
- Prevent blocked accounts from logging in
- Display account details
- Check account balance
- Deposit money
- Withdraw money
- Transfer money between accounts
- Save account changes permanently using JSON
- Allow customers to log out and return to the main menu

---

## 📌 Scope

### Included

The current version includes:

- Account creation
- Customer authentication
- Password validation
- Unique account number generation
- Failed login attempt tracking
- Account blocking
- Account details
- Balance checking
- Deposits
- Withdrawals
- Money transfers
- Input validation
- JSON-based persistent storage
- Customer menu
- Main menu
- Logout functionality

### Not Included

The current version does not include:

- Administrator panel
- Automatic account unblocking
- Password encryption/hashing
- Transaction history
- Interest calculation
- Loans
- ATM functionality
- Multiple account types
- Database integration
- Graphical user interface

These can be considered for future versions.

---

## 📌 Architecture

The project follows a modular structure where different responsibilities are separated into different Python files.

```text
BankingManagementSystemVersion1/
│
├── main.py
├── accountManagement.py
├── auth.py
├── bankingOperations.py
├── costumerMenu.py
├── dataStorage.py
│
├── data/
│   └── accounts.json
│
└── README.md
````

### Module Responsibilities

| Module                 | Responsibility                                                              |
| ---------------------- | --------------------------------------------------------------------------- |
| `main.py`              | Controls the main menu and overall program flow                             |
| `accountManagement.py` | Creates accounts, generates account numbers, and finds accounts             |
| `auth.py`              | Handles login, password verification, failed attempts, and account blocking |
| `costumerMenu.py`      | Displays and controls the customer menu                                     |
| `bankingOperations.py` | Handles balance, deposit, withdrawal, and transfer operations               |
| `dataStorage.py`       | Loads and saves account data                                                |
| `accounts.json`        | Stores persistent customer account information                              |

---

## 📌 Components / Functions

### Account Management

The account management component is responsible for creating and locating accounts.

Main responsibilities:

* Validate customer information
* Generate unique account numbers
* Create account dictionaries
* Find accounts using account numbers

Each account contains information such as:

```json
{
    "name": "muhammad salman raza",
    "password": "191121",
    "account_number": "9607",
    "initial_deposit": 25000.0,
    "failed_attempts": 0,
    "blocked": false
}
```

---

### Authentication

The authentication system handles customer login.

The login process:

1. Requests the account number.
2. Requests the password.
3. Finds the account.
4. Checks whether the account is blocked.
5. Compares the entered password with the stored password.
6. Increases `failed_attempts` when the password is incorrect.
7. Blocks the account after 5 failed attempts.
8. Resets `failed_attempts` after a successful login.

---

### Customer Menu

After successful authentication, the logged-in account is passed to the customer menu.

```text
CUSTOMER MENU

1. Account Details
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. Logout
```

The customer menu acts as the interface between the logged-in customer and the banking operations.

---

### Banking Operations

The banking operations component handles financial operations.

#### Check Balance

Displays the customer's current balance.

#### Deposit

Adds a valid deposit amount to the customer's balance.

#### Withdrawal

Subtracts money from the customer's balance after checking that:

* The amount is greater than zero.
* The customer has sufficient balance.

#### Transfer

Transfers money between two accounts.

The system checks that:

* The receiver account number is valid.
* The receiver account exists.
* The receiver is not the sender's own account.
* The transfer amount is greater than zero.
* The sender has sufficient balance.

After a successful transfer:

```text
Sender Balance   = Sender Balance - Transfer Amount
Receiver Balance = Receiver Balance + Transfer Amount
```

---

## 📌 Workflow

The overall workflow of the system is:

```text
                    START
                      │
                      ▼
              Load accounts.json
                      │
                      ▼
                 MAIN MENU
                /    |     \
               /     |      \
              ▼      ▼       ▼
        Create     Login    Exit
        Account      │
           │         ▼
           │    Find Account
           │         │
           │         ▼
           │    Check Blocked
           │         │
           │         ▼
           │    Verify Password
           │         │
           │         ▼
           │    Successful Login
           │         │
           │         ▼
           │    CUSTOMER MENU
           │         │
           │    ┌────┼────┬────┬────┐
           │    ▼    ▼    ▼    ▼    ▼
           │ Details Balance Deposit Withdraw Transfer
           │
           ▼
      Save Account Data
           │
           ▼
      accounts.json
```

---

## 📌 Data Flow

The system uses a list of account dictionaries while the program is running and JSON for permanent storage.

### Loading Data

When the program starts:

```text
accounts.json
      │
      ▼
load_accounts()
      │
      ▼
user_accounts
```

`user_accounts` contains the accounts loaded from the JSON file.

---

### Creating an Account

```text
User Input
    │
    ▼
create_accounts()
    │
    ├── Validate Name
    ├── Validate Password
    ├── Validate Deposit
    └── Generate Account Number
    │
    ▼
Account Dictionary
    │
    ▼
user_accounts
    │
    ▼
accounts.json
```

---

### Login

```text
Account Number + Password
            │
            ▼
        find_account()
            │
            ▼
      Account Dictionary
            │
            ▼
      Check Credentials
            │
      ┌─────┴─────┐
      ▼           ▼
   Correct      Incorrect
      │           │
      ▼           ▼
 Customer      Failed Attempt
 Menu              │
                    ▼
              5 Attempts?
                    │
              ┌─────┴─────┐
              ▼           ▼
             No          Yes
              │           │
              │           ▼
              │       Block Account
              │
              ▼
        Save JSON Data
```

---

### Banking Operation

For example, during a deposit:

```text
Customer
   │
   ▼
Enter Deposit Amount
   │
   ▼
Validate Amount
   │
   ▼
Update Account Balance
   │
   ▼
Save user_accounts
   │
   ▼
accounts.json
```

---

## 📌 Validation

The system validates different types of user input before processing it.

### Name Validation

The customer's name is checked to ensure it contains valid alphabetic characters while allowing spaces.

### Password Validation

The system requires a password with exactly 6 characters.

### Account Number Validation

The account number must contain exactly 4 digits.

### Deposit Validation

The deposit amount must:

* Be a valid number
* Be greater than zero

### Withdrawal Validation

The withdrawal amount must:

* Be a valid number
* Be greater than zero
* Not exceed the customer's current balance

### Transfer Validation

The transfer amount must:

* Be a valid number
* Be greater than zero
* Not exceed the sender's balance

The receiver account must also exist and cannot be the sender's own account.

### Login Validation

The system checks:

* Whether the account exists
* Whether the account is blocked
* Whether the password is correct
* Number of failed attempts

---

## 📌 Business Logic

The main rules controlling the system are:

### Account Creation

Every customer receives a unique 4-digit account number.

### Login Attempts

A failed password increases:

```text
failed_attempts += 1
```

After 5 failed attempts:

```text
blocked = true
```

A successful login resets:

```text
failed_attempts = 0
blocked = false
```

### Blocked Accounts

A blocked account cannot access the customer menu.

The customer must contact the bank administrator.

### Withdrawal

A customer cannot withdraw more money than their available balance.

### Transfer

A customer cannot:

* Transfer money to a nonexistent account
* Transfer money to their own account
* Transfer more money than their available balance

### Data Persistence

Changes made during banking operations are saved back to the JSON file so that account data remains available after restarting the program.

---

## 📌 Input

The system accepts input such as:

* Customer name
* Password
* Account number
* Main menu choice
* Customer menu choice
* Deposit amount
* Withdrawal amount
* Transfer amount
* Receiver account number

Example:

```text
Enter your choice: 2
Enter account number: 9607
Enter account password: 191121
```

---

## 📌 Processing

The program processes the input by:

1. Validating the entered data.
2. Finding the relevant account.
3. Checking authentication and account status.
4. Performing the requested banking operation.
5. Updating the account dictionary.
6. Saving the updated account list to JSON.

For example, a transfer processes two accounts:

```text
Sender Account
      │
      ├── Subtract Transfer Amount
      │
      ▼
Updated Sender Balance


Receiver Account
      │
      ├── Add Transfer Amount
      │
      ▼
Updated Receiver Balance
```

---

## 📌 Output

The program displays results such as:

```text
Login successful.
```

```text
Account found.
```

```text
Total balance = 25000.0
```

```text
Deposit successful.
```

```text
Withdrawal successful.
```

```text
Money Transfer successful.
```

```text
Account blocked.
```

```text
Account not found.
```

---

## 📌 Test Cases

The completed BMS was tested against different normal and invalid situations.

### Account Tests

* Valid account creation
* Invalid name
* Invalid password length
* Invalid deposit
* Unique account number generation
* Account saved to JSON

### Authentication Tests

* Correct account number and password
* Incorrect account number
* Incorrect password
* Successful login after failed attempts
* Failed-attempt counter reset
* Account blocked after 5 failed attempts
* Blocked account cannot log in

### Deposit Tests

* Valid deposit
* Zero deposit
* Negative deposit
* Invalid text input
* Balance updated correctly
* JSON updated correctly

### Withdrawal Tests

* Valid withdrawal
* Zero withdrawal
* Negative withdrawal
* Invalid input
* Withdrawal greater than balance
* Balance updated correctly
* JSON updated correctly

### Transfer Tests

* Valid receiver account
* Nonexistent receiver account
* Transfer to own account
* Zero transfer
* Negative transfer
* Invalid transfer input
* Transfer greater than available balance
* Successful transfer
* Sender balance updated
* Receiver balance updated
* Changes saved to JSON

### Menu Tests

* Main menu
* Customer menu
* Customer operations
* Logout
* Return to main menu

**Result: All 30 planned test cases passed successfully.**

---

## 📌 Technologies Used

* Python
* JSON
* File I/O
* Functions
* Modules
* Lists
* Dictionaries
* Loops
* Conditional statements
* Exception handling

---

## 📌 Project Status

**Version 1.0 — Completed**

The current version successfully implements account management, authentication, account blocking, persistent JSON storage, and basic banking operations through a command-line interface.

---


