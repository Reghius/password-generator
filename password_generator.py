import random

signs = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()'
lenght = int(input('How many sings do you want your password to be? '))
password = ''.join(random.sample(signs, lenght))
print(password)