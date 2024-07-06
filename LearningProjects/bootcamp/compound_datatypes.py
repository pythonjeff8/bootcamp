
from os import major


fruit = ["apple", "banana", "cherry", "date"]

fruit.append("elderberry")
fruit.remove("banana")

fruit.sort()
print(fruit)

#dictionary
student = {}

student = {"name":"John Doe", "age":25, "major":"Computer Science"}

print(student)

student.update({"major":"Electrical Engineering"})

print(student)

student["year"] = "Senior"

#for studentKeys in student:
print(student.keys())
    
print(student.values())

#Multiple Dictionaries
books = [{"title":"Harry Potter", "author":"Rowling", "year":"1997"},
         
         {"title":"Happy Hippo", "author":"Mary Jane", "year":"2970"},
         
         {"title":"My Little Pony", "author":"Jane Horsefeathers", "year":"1990"}]

print(books[1]["title"])

print(books[2]["year"])
    
res = len(list(filter(lambda x: isinstance(x, dict), books)))
x = 0

while x < res:
    print(books[x]["author"])
    print(books[x]["title"])
    x = x + 1
