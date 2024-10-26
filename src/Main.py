from venv import create

choices = ['Create user', 'Edit user', 'log in']
user_credentials = {}

def start():
    print('Hello and welcome to Project1!')

def print_choices():
    print('Enter choice')
    for index, choice in enumerate(choices):
        print(f"{index + 1}. {choice}")

def enter_flow():
    user_input = input("Select an option: ")
    if user_input == '1':
        create_user_flow()
    elif user_input == '2':
        edit_user_flow()
    elif user_input == '3':
        log_in_flow()

def create_user_flow():
    username = input('Enter your name: ')
    if username in user_credentials:
        print('Username already exists')
        create_user_flow()
    else:
        password = input('Enter your password: ')
        user_credentials[username] = password
        print(f"Your name is {username} and your password is {password}")


def edit_user_flow():
    print()

def log_in_flow():
    print()

start()
print_choices()
enter_flow()
