# BMS-version1
A console-based Banking Management System built with Python, featuring account creation, unique account numbers, password-based authentication, deposits, withdrawals, balance checking, money transfers, login attempt tracking, account blocking, input validation, error handling, and file-based data storage.

# 🏦 Banking Management System

A console-based Banking Management System built with Python.

This project is designed as a real-world Python practice project to strengthen programming fundamentals, especially functions, data structures, validation, error handling, file handling, modules, and program structure.

---

## 📌 Project Overview

The Banking Management System allows users to create bank accounts, log in using their account number and password, and perform basic banking operations.

The system focuses on building a structured Python application rather than simply practicing individual Python concepts.

---

 ✨ Features

 Account Management
- Create a new account
- Generate a unique account number
- Set an account password
- Make an initial deposit
- Find existing accounts
- Update account information

 Authentication & Security
- Login using account number and password
- Track failed login attempts
- Block an account after 5 failed login attempts
- Reset failed attempts after successful login

  Banking Operations
- Deposit money
- Withdraw money
- View account balance
- Transfer money between accounts
- Logout

 System Features
- Main menu
- Input validation
- Error handling
- File-based account storage
- Load account data when the program starts
- Save account data after changes



🏗️ Project Architecture

The project is planned using a modular structure:

text
Banking Management System/
│
├── main.py
│
├── account_management.py
├── authentication.py
├── customer_menu.py
├── banking_operations.py
│
└── data/
    └── accounts.json

# 🏦 Banking Management System

A console-based Banking Management System built with Python.

This project is designed as a real-world Python practice project to strengthen programming fundamentals, especially functions, data structures, validation, error handling, file handling, modules, and program structure.

---

## 📌 Project Overview

The Banking Management System allows users to create bank accounts, log in using their account number and password, and perform basic banking operations.

The system focuses on building a structured Python application rather than simply practicing individual Python concepts.

---

## ✨ Features

### Account Management
- Create a new account
- Generate a unique account number
- Set an account password
- Make an initial deposit
- Find existing accounts
- Update account information

### Authentication & Security
- Login using account number and password
- Track failed login attempts
- Block an account after 5 failed login attempts
- Reset failed attempts after successful login

### Banking Operations
- Deposit money
- Withdraw money
- View account balance
- Transfer money between accounts
- Logout

### System Features
- Main menu
- Input validation
- Error handling
- File-based account storage
- Load account data when the program starts
- Save account data after changes

---

## 🏗️ Project Architecture

The project is planned using a modular structure:

``text
Banking Management System/
│
├── main.py
│
├── account_management.py
├── authentication.py
├── customer_menu.py
├── banking_operations.py
│
└── data/
    └── accounts.json

Module Responsibilities
main.py

Controls the overall program and connects the different modules.

account_management.py

Handles:

Account creation
Account number generation
Finding accounts
Updating account data
authentication.py

Handles:

Login
Password verification
Failed login attempts
Account blocking
customer_menu.py

Handles the menu available after successful login.

banking_operations.py

Handles:

Deposits
Withdrawals
Balance checking
Money transfers
data/accounts.json

Stores account data permanently between program runs.

🔄 Workflow
START
  │
  ▼
Load Saved Account Data
  │
  ▼
MAIN MENU
  │
  ├───────────────┬───────────────┐
  ▼               ▼               ▼
Create Account   Login           Exit
  │               │               │
  ▼               ▼               ▼
Enter Name      Enter Account    END
  │             Number
  ▼               │
Set Password      ▼
  │             
  ▼  
Generate          
Account Number  Find Account
  │               │
  ▼               ▼
Initial Deposit  Verify Credentials
  │               │
  ▼          ┌────┴─────┐
Create       │          │
Account    Wrong      Correct
  │           │          │
  ▼           ▼          ▼
Save       Attempts   CUSTOMER MENU
Account      +1           │
  │           │           │
  ▼           │     ┌─────┼──────┬──────────┐
Main Menu     │     ▼     ▼      ▼          ▼
              │  Deposit Withdraw Balance Transfer
              │     │      │      │          │
              │     └──────┴──────┴──────────┘
              │                  │
              │                  ▼
              │             Save Changes
              │                  │
              │                  ▼
              │               Logout
              │                  │
              │                  ▼
              │              MAIN MENU
              │
              ▼
        5 Failed Attempts?
          │          │
         Yes         No
          │          │
          ▼          ▼
    Block Account  Try Again
          │
          ▼
      Login Ends

🔀 Data Flow
                         USER
                          │
                          │ Input
                          ▼
                    ┌───────────┐
                    │  main.py  │
                    └─────┬─────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
       Create Account    Login    Customer Menu
             │            │            │
             ▼            ▼            ▼
       Account         Find/Verify   Banking
      Management       Account       Operations
             │            │            │
             └────────────┼────────────┘
                          │
                          ▼
                    ACCOUNT DATA
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
     Account Number      Name          Password
          │
          ├── Balance
          ├── Failed Attempts
          └── Blocked Status
                          │
                          ▼
                   Save Account Data
                          │
                          ▼
                    accounts.json
                          │
                          │ Load
                          ▼
                    Python Program

🛡️ Validation

The system validates user input at different stages.

Main Menu
Only valid menu options are accepted.
Invalid options are rejected.
Empty input is rejected.
Account Creation
Name cannot be empty.
Name must contain valid characters.
Password must meet the required length.
Initial deposit must be a valid number.
Initial deposit must be greater than 0.
Generated account numbers must be unique.
Login
Account number cannot be empty.
Account number must exist.
Password cannot be empty.
Incorrect credentials increase the failed-attempt counter.
Account is blocked after 5 failed attempts.
Successful login resets failed attempts.
Deposit
Amount must be numeric.
Amount must be greater than 0.
Withdrawal
Amount must be numeric.
Amount must be greater than 0.
Amount cannot exceed the available balance.
Money Transfer
Destination account must exist.
Destination account cannot be the sender's own account.
Transfer amount must be numeric.
Transfer amount must be greater than 0.
Sender must have sufficient balance.

📋 Business Rules
Every account must have a unique account number.
An account must have a valid name and password.
Initial deposits must be greater than zero.
Users must provide valid credentials to log in.
An account is blocked after 5 failed login attempts.
A successful login resets the failed-attempt counter.
Deposits must be greater than zero.
Withdrawals must be greater than zero.
Users cannot withdraw more than their available balance.
Users cannot transfer more than their available balance.
Users cannot transfer money to their own account.
The destination account must exist before a transfer.
Account data must be saved after account information changes.
Saved account data must be loaded when the program starts.


    
