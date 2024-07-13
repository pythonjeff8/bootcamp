

quiz = [{"Question1":"What is the capitol of France?", "1":"London", "2":"Berlin", "3":"Paris", "Correct":"3"},
         
         {"Question2":"Which planet is known as the Red planet?", "1":"Earth", "2":"Mars", "3":"Jupiter", "Correct":"2"},
         
         {"Question3":"When was Python created?", "1":"1991", "2":"2002", "3":"1873", "Correct":"1"}]


quizLength = len(list(filter(lambda x: isinstance(x, dict), quiz)))

x = 0
correct = 0
answer = ""
answered = 0
right = []
wrong = []

while x < quizLength:
    for key, val in quiz[x].items():
        if "Question" in key:
            print(val)
            question = val
        elif "Correct" in key:
            next
        else:
            print(key +". " + val)
          
    answer = input("Your answer (1 / 2 / 3) ")
    answered = answered + 1
    if answer == quiz[x]["Correct"]:
        correct = correct + 1 
        right.append(question)
    else:   
        wrong.append(question)
    x = x + 1
    
print("Your final score is: " + str(correct) + "/" + str(answered))

print()
print("Questions you got right - ")
if len(right) == 0:
    print("You didn't get any questions right")
for i in right:
    print(i)

print()
print("Questions you got wrong - ")  
if len(wrong) == 0:
    print("You didn't get any questions wrong") 
for i in wrong:
    print(i)
print()
 
    

