# import os

# def read_file(filename):
#   """
#   Reads the contents of a file and returns them as a string.

#   Args:
#     filename: The name of the file to read.

#   Returns:
#     The contents of the file as a string.
#   """
#   try:
#     with open(filename, 'r') as f:
#       return f.read()
#   except FileNotFoundError:
#     return ""

# def write_file(filename, data):
#   """
#   Writes data to a file.

#   Args:
#     filename: The name of the file to write to.
#     data: The data to write to the file.
#   """
#   with open(filename, 'w') as f:
#     f.write(data)

# def process_input(user_input):
#   """
#   Processes user input and performs actions based on the input.

#   Args:
#     user_input: The user input string.
#   """
#   if user_input.startswith("read_file"):
#     filename = user_input.split(" ")[1]
#     file_contents = read_file(filename)
#     print(file_contents)
#   elif user_input.startswith("write_file"):
#     filename, data = user_input.split(" ")[1], " ".join(user_input.split(" ")[2:])
#     write_file(filename, data)
#   else:
#     print("Invalid command.")

# if __name__ == "__main__":
#   while True:
#     user_input = input("Enter a command: ")
#     process_input(user_input)
