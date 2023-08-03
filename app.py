command = " "
starts = False
while True:
    command = input("> ").lower()
    if command == "start":
        if starts:
            print("car already started..")
        else:
            starts = True
            print("car started..")
    elif command == "stop":
        if not starts:
            print("car is already stopped")
        else:
            starts = False
            print("car -- stoped")
    elif command == "help":
        print("""
    start --- to start the car
    stop --- to stop the car
    quit --- to exit 
        """)
    elif command == "quit":
        break
    else:
       print("sorry i don't understand that")
