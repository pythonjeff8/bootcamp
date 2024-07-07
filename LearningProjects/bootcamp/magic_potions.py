

from ast import Return


potions = { "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"] }

print("Welcome to the magic potion shop! ")
print("These are the potions we offer: ")    
    
for k, v in potions.items():
    print(k)
   
selection = input("Which potion would you like to buy ingrediants for? ")

print()
print("The ingrediants for " + selection + " are:")
if selection == "Invisibility Potion":
    for v in potions["Invisibility Potion"]:
        print(v)
elif selection == "Flying Potion":
    for v in potions["Flying Potion"]:
        print(v)
elif selection == "Healing Potion":
    for v in potions["Healing Potion"]:
        print(v)
else:
    print("Invalid option, please reenter")
    
print()

print("Let's start buying ingredients!")
x = 0
if selection == "Invisibility Potion":
    while x < len(potions["Invisibility Potion"]):
        yn = input("Do you want to buy " + potions["Invisibility Potion"][x] + "? (yes/no) ")
        if yn == "yes":
            print("You bought " + potions["Invisibility Potion"][x] + "!")
        else:
            print("You chose to stop shopping.")
            break 
        x += 1    
elif selection == "Flying Potion":
    while x < len(potions["Flying Potion"]):
        yn = input("Do you want to buy " + potions["Flying Potion"][x] + "? (yes/no) ")
        if yn == "yes":
            print("You bought " + potions["Flying Potion"][x] + "!")
        else:
            print("You chose to stop shopping.")
            break
        x += 1         
elif selection == "Healing Potion":
    while x < len(potions["Healing Potion"]):
        yn = input("Do you want to buy " + potions["Healing Potion"][x] + "? (yes/no) ")
        if yn == "yes":
            print("You bought " + potions["Healing Potion"][x] + "!")
        else:
            print("You chose to stop shopping.")
            break  
        x += 1 
    
if yn == "yes":
    print("Congratulations, you bought all the ingredients for Healing Potion!")  
         

    
