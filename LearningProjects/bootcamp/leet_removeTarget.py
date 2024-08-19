
def removeElement(nums = [int], val = int) :
    if val not in nums:
        return len(nums)
    if len(nums) == 1 and val in nums:
        return 0
    idx = 0
    j = len(nums) -1
    while idx <= j:
        if nums[idx] == val:
            del nums[idx]
            j -= 1
        else:
            idx += 1
    
    print(nums)
    return  nums

print(removeElement([2,8,6,3,3,5,3,2], 3))

