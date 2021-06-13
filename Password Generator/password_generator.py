import random

string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%^&*()_+"

pass_len = int(input("Enter the password length : "))

password = ""
password = "".join(random.sample(string,pass_len))

print(f"Your generate password is : {password}")
