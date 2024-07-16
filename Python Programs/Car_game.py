#Building a car game
command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car has already started.")
        else:
            started=True
            print("Car has started!You are ready to go...")
    elif command=="stop":
        if not started:
            print("Car has already stopped!")
        else:
            started=False
            print("Car has stopped.")
    elif command=="help":
        print("""
        start-To start the car.
        Stop-To stop the car.
        quit-to quit""")
    elif command=="quit":
        break
    else:
        print("Sorry!I don't understand...")