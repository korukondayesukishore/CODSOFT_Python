import random

print("Password Generator")
print("Created by Ramana")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*"

all_values = letters + digits + symbols

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password = password + random.choice(all_values)

print("Your password is:", password)
print("Password generated successfully")
