#Priyanshu Dubey
#8/10/2020
#Password Generator: Just enter the length of password,
#                   it will give you a strong and unique password.


import random
import string

req_length = int(input("Enter the length of password: "))

letters = string.ascii_letters
number = '0123456789'
special_char = '+-*%&$!_'
combination = letters + number + special_char

password = "".join(random.sample(combination, req_length))

print(password)
