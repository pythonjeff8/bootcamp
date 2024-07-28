
def remodups(sortlist = []):
    x = 0
    strlen = len(sortlist) - 1
    while x < strlen:
        if sortlist[x] == sortlist[x+1]:
            del sortlist[x+1] 
            strlen -= 1
        else:
            x += 1
    print(sortlist)    

remodups([1,2,2,2,2,2,2,3,3,5,5,5,5,8])  
    