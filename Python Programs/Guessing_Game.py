secret_number = 6
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    Guess = int(input("Guess the Number: "))
    guess_count+= 1
    if Guess==secret_number:
        print("You guessed it right!")
        break
else:
    print("Try again!")
