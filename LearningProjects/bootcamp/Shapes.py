import math

#Calculate Area of Rectangle
length = int(input("Enther rectangle length: "))
height = int(input("Enter rectangle height: "))
area = length * height
print("The retangle's area is " + str(area))


#Calculate area of Circle
radius = int(input("Enter the Circles radius: "))
circleArea = math.pi * (radius * radius)
print("The Circle's area is " + str(format(circleArea,".2f")))


#Calculate area of a Triangle 
base = int(input("Enter the triangle base: "))
triangleHeight = int(input("Enter triangle height: "))
triArea = (base * height) / 2 
print("The triangle's area is " + str(triArea))

