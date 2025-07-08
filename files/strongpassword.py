import re

print('Please enter your new password')

upper = re.compile(r'[A-Z]+')
lower = re.compile(r'[a-z]+')
digit = re.compile(r'\d+')

def strongpassword():
    while True:
        password = input()

        if lower.search(password) == None:
            print('No lower case character found')
            continue
        if upper.search(password) == None:
            print('No upper case character found')
            continue
        if digit.search(password) == None:
            print('No digit found')
            continue
        if len(password) < 8:
            print('length of password should be atleast 8')
            
        print('Password is strong!')
        break

strongpassword()
