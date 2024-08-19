
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

print()

#for studentKeys in student:
print(student.keys())
    
print(student.values())

#Multiple Dictionaries
books = [{"title":"Harry Potter", "author":"J K Rowling", "year":"1997"},
         
         {"title":"Happy Hippo", "author":"Mary Jane", "year":"2970"},
         
         {"title":"My Little Pony", "author":"Jane Horsefeathers", "year":"1990"}]

print()

print(books[1]["title"])

print(books[2]["year"])

print()

res = len(list(filter(lambda x: isinstance(x, dict), books)))
x = 0

while x < res:
    print("Author: " + books[x]["author"] + " - Title: " + books[x]["title"])
    
    x = x + 1
print()


courses = [{"Name":"Math", "Student1":"JK Rowling", "Student2":"John Jones"},
         
         {"Name":"History", "Student1":"Mary Jane", "Student2":"George Jamison", "Student3":"Mary Mary"},
         
         {"Name":"Chemistry", "Student1":"Jane Horsefeathers", "Student2":"James John"}]

courses[0]["Student3"] = "Jimmy Johnson"
courses[0]["Student4"] = "Janey Johns"
courses[0]["Student5"] = "Joan Howard"
courses[0]["Student6"] = "Bobby Billings"
courses[0]["Student7"] = "Jim Johanson"

print(courses)

del courses[1]["Student2"]

print("- After del -")
print()

print(courses)

print()

print(courses[2])

courses.append({"Name":"Physics", "Student1":"George Jones", "Student2":"Fred Flintstone", "Student3":"Betty Rubble", "Student4":"Barney Dino"})

print()
print(courses[3])
