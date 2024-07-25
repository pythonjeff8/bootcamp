import sys

MINI_CHAR = 7
SPEC_CHAR = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "?"]
MYNUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

attempts = 0

print("Welcome to the password checker!")
print("A stong password must meet the following criteria:")
print("- At least 7 characters long")
print("- Include at least one special character")
print("- Include at least one number")

def enterpwd():
    pwd = input("Enter your password: ")
    global attempts
    attempts += 1
    if attempts > 3:
            print("Too many attempts, try again later")
            sys.exit()
    check_length(pwd)
    spec_char(pwd)
    hasnumeric(pwd)

def check_length(pwd):
    if len(pwd) < MINI_CHAR:
        print("Password must be at least 7 characters long")
        enterpwd()
            
def spec_char(pwd): 
        x = 0     
        for element in pwd:
            if element in SPEC_CHAR:
                x =+ 1
        if x == 0:
            print("Password must contain a special character")
            enterpwd()
        
def hasnumeric(pwd):
    y = 0
    for letter in pwd:
        if letter.isdigit():
            y =+ 1
    if y == 0:
            print("Password must contain at least one number")
            enterpwd()  
    
enterpwd()
            
print("You have a valid strong password")
