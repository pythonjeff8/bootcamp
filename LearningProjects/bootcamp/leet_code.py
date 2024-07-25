import sys

def sum_two(numbs: list[int], target):
    
    #if len(numbs) == 1 and numbs[0] == target:
    #print("The item that equals the target is the first value")
    
    x = 0
    y = 0
    nines = []
    #print(len(numbs))
    #print(numbs[0])
    while x < (len(numbs) - 1):
        y = x
        while y < (len(numbs) - 1):
            if numbs[x] + numbs[y+1] == target:
                nines.append(x)
                nines.append(y + 1) 
            y += 1             
        x += 1
    
    pos = 0
    pairs = ""
    
    if (len(nines) == 0):
        print("No value pairs equal target in number string")
        sys.exit()
        
    while pos < (len(nines) - 1):
        if pos == (len(nines) - 2):
            pairs = pairs + "" + str(nines[pos]) + "," + str(nines[pos + 1])
        else:
            pairs = pairs + "" + str(nines[pos]) + "," + str(nines[pos + 1]) + " - "
        pos += 2
        
    print("The value pairs that equal the target are positions: " + pairs)

      
sum_two([2, 7, 5, 8, 1, 4], 9)
            