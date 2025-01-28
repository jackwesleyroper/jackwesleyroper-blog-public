# For testing purposes only
password = "your_hardcoded_password"

# Sample usage in your code
def authenticate(user_input):
    if user_input == password:
        print("Authentication successful")
    else:
        print("Authentication failed")

# Test the function
user_input = input("Enter the password: ")
authenticate(user_input)
