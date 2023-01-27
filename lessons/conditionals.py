"""Checks light, if green, says go"""

light: str = input("What color is the light? ").lower()

if (light == "green"):
    print("Go!")
    print("Drive safe!")
else:
    if (light != "red"):
        if (light == "yellow"):
            print("Slow down!")
        else:
            print("This is a problem")
    else: 
        print("stop!")
print("Don't look at your phone")