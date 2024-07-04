
upper = input("Enter a sentence: ")
print(f"Your sentence corrected {upper.upper()}")

wordCount = input("Enter a paragraph: ")
print(f"You used {len(wordCount.split())} words")

numString = input("enter a numerical string: ")
print(numString.isnumeric())

replaceString = input("Enter a string: ")
print(replaceString.replace("a", "o"))

initials = input("Enter your name: ")
for x in initials.split():
    print(x[0], end="")

print("") 
    
strLength = input("Enter a string: ")
print(len(strLength))
    
    

