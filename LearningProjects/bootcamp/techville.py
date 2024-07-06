

def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")
    
    
start_engine()
dest = input("What is your desired destination? ")

if dest == "library":
    move_forward()
    turn("Left")
    print("We have arrived at the Library")
elif dest == "tech park":
    move_forward()
    turn("Right")
    print("We have arrived at the Tech Park")
elif dest in ("hospital", "mall", "airport", "university", "stadium"):
    move_forward()
    print("entering roundabout")
    if dest == "hospital":
        follow_roundabout(1)
        print("We have arrived at the hospital")
    elif dest == "mall":
        follow_roundabout(2)
        move_forward()
        turn("Right")
        print("We have arrived at the mall")
    elif dest == "airport":
        follow_roundabout(3)
        print("We have arrived at the airport")
    elif dest in ("university", "stadium"):
        follow_roundabout(4)
        if dest == "university":
            turn("Left")
            print("We have arrived at the university")
        elif dest == "stadium":
            turn("Right") 
            print("We have arrived at the stadium")
else:
    print("This is not a valid destination")
    
stop_engine()

