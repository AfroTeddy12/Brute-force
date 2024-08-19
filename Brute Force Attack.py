import random
import string 
import time
from itertools import product

def password_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def brute_force_attack(target_password):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    for length in range(1, len(target_password) + 1):
        for guess in product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target_password:
                return attempts, guess


# Ask the user for password length
while True:
    try: 
        password_length = int(input("Enter length for password: "))
        if password_length <= 0:
            print("Please enter a positive number: ")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid Length")

#Generate the passoword
password = password_generate(password_length)
print("Generated password: ", password)

#simulate atttack

start_time = time.time()
attempts, cracked_password = brute_force_attack(password)
end_time = time.time()

#Results
print(f"Password Cracked: {cracked_password}")
print(f"Number of attempts: {attempts}")
print(f"Time Taken: {end_time - start_time} seconds")

