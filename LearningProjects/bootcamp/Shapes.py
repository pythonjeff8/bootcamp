import math

#Calculate Area of Rectangle
def rectArea():
    length = int(input("Enther rectangle length: "))
    height = int(input("Enter rectangle height: "))
    area = length * height
    print("The retangle's area is " + str(area))


#Calculate area of Circle
def circArea():
    radius = int(input("Enter the Circles radius: "))
    circleArea = math.pi * (radius * radius)
    print("The Circle's area is " + str(format(circleArea,".2f")))


#Calculate area of a Triangle 
def triangArea():
    base = int(input("Enter the triangle base: "))
    triangleHeight = int(input("Enter triangle height: "))
    triArea = (base * height) / 2 
    print("The triangle's area is " + str(triArea))

def square_perimeter():
    length = int(input("Enter the length of one side of the square: "))
    print("the perimeter is: " + str(length * 4))
    
square_perimeter()
    
def circle_details(radius):
    circleArea = math.pi * (radius * radius)
    print("The Circle's area is " + str(format(circleArea,".2f")))
    circlecircumference = 2 * math.pi * radius 
    print("The circles circumference is: " + str(circlecircumference))
    
circle_details(5)

def geometry(length, radius):
    
    squarArea = length * 2
    squarLength = length * 4
    
    circleArea = math.pi * (radius * radius)
    circleCircumference = 2 * math.pi * radius 
    
    if squarArea > circleArea:
        print(squarArea)
        print("The square area is larger")
    else:
        print(circleArea)
        print("The circle perimeter is larger")
    
    if squarLength > circleCircumference:
        print(squarLength)
        print("The square perimeter is larger")
    else:
        print(circleCircumference)
        print("The circle perimieter is larger")
    
    
geometry(4,5)

        