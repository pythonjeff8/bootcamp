# this is a test
def main():
    
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
    y = input("Number ")
    c = (int(y) / 2.5)
    print(type(c))
        
        
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
            
main()



    

