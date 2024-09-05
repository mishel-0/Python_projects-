import random

letters = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the Password Generator!")


nr_letters = int(input("How many letters do you prefer in your password? ;)\n"))
nr_numbers = int(input("How many numbers do you prefer in your password? , hang on tight! :)\n"))
nr_symbols = int(input("How many symbols do you prefer in your password? , it's gonna be ready anytime! :)\n"))

# Easy level
password = ""

# Adding letters to the password
for char in range(nr_letters):
    password += random.choice(letters)

# Adding numbers to the password
for char in range(nr_numbers):
    password += random.choice(numbers)

# Adding symbols to the password
for char in range(nr_symbols):
    password += random.choice(symbols)

print(f"Congratulations!! your generated password is : {password}")
