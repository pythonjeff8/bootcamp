
def rom2int(s) -> int:
    
    romhash = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    intval = 0
    
    for i in range(len(s)):
        if i < len(s) - 1 and romhash[s[i]] < romhash[s[i+1]]:
            intval -= romhash[s[i]]
        else:
            intval += romhash[s[i]]   
    return intval

x = input("Enter roman numeral: ")
print(rom2int(x))
