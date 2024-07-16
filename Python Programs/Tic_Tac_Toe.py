def printboard():
    print(f" 0 | 1 | 2 ")
    print(f" --------- ")
    print(f" 3 | 4 | 5 ")
    print(f" --------- ")
    print(f" 6 | 7 | 8 ")

if __name__== "__main__":
    xstate=[0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0]
    turn = 1 #1 for "X" and 0 for "O"
    print("Welcome to TIC_TAC_TOE")
    while(True):
        printboard()
        if(turn == 1):
            print("X's chance")
            value = int(input("Please enter a value."))
            xstate[value] = 1
        else:
            print("O's chance")
            value = int(input("Please enter a value."))
            zstate[value] = 1

