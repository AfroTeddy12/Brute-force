import random
import string 

def password_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    try: 
        password_length = int(input("Enter length for password: "))
        if password_length <= 0:
            print("Please enter a positive number: ")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid Length")

print("Generated Password:", password_generate(password_length))