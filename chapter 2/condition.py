light = input("Enter traffic light color (red, green, yellow): ")
mode = input("Enter mode (day/night): ")


if light == "red":
    print("Stop")
elif light == "green":
    print("Go")
elif light == "yellow":
    print("Caution")
else:
    print("Invalid light color")
if mode == "night":
    print("Night mode")
else:
    
    print("Day mode") 