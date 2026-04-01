import random
x=True
number=str(random.randint(0,9))
print("I have a number from 0 to 9 in my mind!Guess it!")
while x:
    Guess=input("Enter a number: ")
    if Guess==number:
        print("You have guessed the number the number is ",number)
        break
    else:
        print("Your guess was wrong! try again!")