'''
Class Anemone
Lab 16
Author: Bailey Baker
Description: A program to generate and store passwords into a text file.
'''
from password_generator import PasswordGenerator
import os
import json

pwo = PasswordGenerator()

# function to call on PasswordGenerator class to generate password
def generate():
    pwo.generate()

# function that appends newly added to account to list of other accounts 
def update(account, accounts):
    account.append(input('\nEnter name of website for username and password: '))
    account.append(input('\nEnter username: '))
    account.append(pwo.generate())
    account = dict(zip(header, account))
    accounts.append(account)  

# function that calls on PasswordGenerator class to update settings for newly generated passwords
def settings():
    pwo.minlen = int(input("Enter password minimum length: "))
    pwo.maxlen = int(input("Enter password maximum length: "))
    pwo.minuchars = int(input("Enter password minimum uppercase chars: "))
    pwo.minlchars = int(input("Enter password minimum lower case chars: "))
    pwo.minnumbers = int(input("Enter password minimum numbers: "))
    pwo.minschars = int(input("Enter password minimum special chars: "))

# function to print all accounts and their passwords/usernames
def show(accounts):
    for name in accounts:
            print(f'{name}\n') 

# function to delete any account by the name of said accounts website/app                                              
def delete(accounts):
    find = input("\nEnter the account you'd like to delete: ")
    for name in accounts:
        if find == name['account']:
            accounts.remove(name)
    return accounts

print("\nWelcome to the password generator/exporter\n")

accounts = []

# adds all passwords/accounts stored on text file to accounts list
with open('passwords.txt', 'r') as f:
    if os.stat('passwords.txt').st_size != 0:
        lines = '[' + ','.join(line for line in f) + ']'
        accounts =json.loads(lines)

#REPL loop to get website, username, and generate a password.
while True:
    command = input("Enter a command or enter 'help' to see available commands: ").lower()
    account = []
    header = ['account', 'username', 'password']
    
    if command == 'new':
        update(account, accounts)        
    
    elif command == 'settings':
        settings()
    
    elif command == 'list':
        show(accounts)       
    
    elif command == 'delete':
        delete(accounts)
    
    elif command == 'exit':
        break
    
    elif command == 'help':
        print('\nAvailable commands:')
        print('new  - Enter information for new account and generate a password')
        print('settings  - Change settings for generated passwords')
        print('list - Show all accounts and their respective username/passwords')
        print('delete - Enter account info to have said account deleted')
        print('exit - Exit the program\n')
    
    else:
        print("\nUnknown command!")
# write accounts back to text file, seperated by new line for each account
with open('passwords.txt', 'w') as f:
    for name in accounts:
        json.dump(name, f)
        f.write('\n')