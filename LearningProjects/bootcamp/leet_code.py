
def sum_two(numbs: list[int], target):
    if target not in numbs:
        print("No values in number string")
    if len(numbs) == 1 and numbs[0] == target:
        print("The item that equals the target is 0")
    
    x = 0
    nines = []
    print(len(numbs))
    print(numbs[0])
    while x < (len(numbs) - 1):
        if numbs[x] + numbs[x+1] == target:
            nines.append(numbs[x])
            nines.append(numbs[x + 1])              
        x += 1
    print(nines[1])

sum_two([2, 7, 8], 9)
            