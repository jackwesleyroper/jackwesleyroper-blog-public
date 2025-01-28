# vulnerable_script.py

# This function is intentionally vulnerable for testing purposes.
def execute_user_code(user_input):
    # WARNING: Using eval() with untrusted input is dangerous and can lead to code injection.
    result = eval(user_input)
    return result

# Test the function
if __name__ == "__main__":
    user_input = input("Enter a Python expression to evaluate: ")
    print("Result:", execute_user_code(user_input))
