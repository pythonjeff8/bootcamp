
testval = input("Enter your value to check for palindrome: ")

def paltest(x):
    palval = ""
    for y in x:
        palval = y + palval
    
    if x == palval:
        print("True - this is a palindrome value")
    else:
        print("False - this is not a palindrome value")
    return 

paltest(testval)
