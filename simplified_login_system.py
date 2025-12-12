# 9. Simplified Login System

# Create a program that:

# Stores usernames and passwords in a dictionary.

# Has a function to validate the login.

# Uses a loop to allow attempts until the correct answer is reached or 3 errors are encountered.

# Uses conditions to check if the password is correct.

# Displays a success or blocked message.
users = {
    "alice": "123",
    "bob": "123",
    "carlos": "123",
    "diana": "123",
    "eva": "123"
}


def validate_login(login, password, users):
    attempts = 3
    
    if login not in users:
        return 'Login not found'

    while attempts > 0:
        if password == users[login]:
            return 'Logged in successfully.'
        else:
            attempts -= 1
            if attempts == 0:
                return 'Attempts exhausted! User blocked.'
            print(f"Incorrect password! Remaining attempts: {attempts}")
            password = input('enter password again: ')
while True:
    login = input('Login: ')
    password = input('Password: ')


    result = validate_login(login, password, users)
    print(result)

    if result.startswith('Logged in successfully.'):
        break
    