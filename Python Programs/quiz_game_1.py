print("Welcome to the Computer quiz!")
playing = input("Do you want to play?: ")

if playing.lower() !="yes":
    quit()
else:
    print("Ok! Let's start the quiz.")

score=0

answer = input("What does CPU stands for? :  ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What does CD stands for? :  ")
if answer.lower()=="compact disk":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("Which is a versatile programming language? :  ")
if answer.lower()=="python":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("Which among all languages data structures and algorithms are useful? :  ")
if answer.lower()=="java":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")