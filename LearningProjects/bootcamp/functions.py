
def dollarizer(wrd):
    altered = wrd.replace("s", "$")
    print(altered)
    
dollarizer("states")
    
def eurizer(euwrd):
    eualtered = euwrd.replace("e", "\N{euro sign}")
    print(eualtered)
        

eurizer("edetthere")

def replacer(word, orig, replac):
    altered = word.replace(orig, replac)
    print(altered)
    
replacer("alabama", "a", "@")

def wonky_text(word, s, e, l):
    altered = word.replace(s,"$")
    altered = altered.replace(e,"\N{euro sign}")
    altered = altered.replace(l,"\N{pound sign}")
    print(altered)
    
wonky_text("sleuths", "s", "e", "l")

def celsiusTofahrenheit():
    C = int(input("Enter a Celcius value: "))
    F = C * 9/5 + 32
    print(str(F))
    
celsiusTofahrenheit()

def ageinDays():
    years = int(input("Enter how many years old you are: "))
    print("You are " + str(years * 365) + " days old")
    
ageinDays()

def simple_interest(P, R, T):
    print("Your simple interest is: " + str((P * R * T)/100))

simple_interest(10000, 4, 10)

def plan_finances(P, R, T, goal):
    si = (P * R * T)/100
    if si > goal:
        print("Goal not reached")
    elif si < goal:
        print("Goal exceeded")
    else:    
        print("Goal reached")
        
plan_finances(10000, 3, 10, 2000)

        