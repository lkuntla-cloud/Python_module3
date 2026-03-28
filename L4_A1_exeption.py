try:
    number=int(input("Enter a integer number: "))
    print("The integer number is: ",number)
except ValueError as VE:
    print("The type of exception is", VE)
    