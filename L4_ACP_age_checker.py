try:
    n=int(input("Enter your age: "))
    x="valid"
except ValueError:
    print("That cannot be your age because your input was not a number")
    x="invalid"
if x=="valid":
    if n%2==0:
        print("Your age is even")
    else:
        print("Your age is odd")
else:
    print("Your input was wrong so we can't check if the number is odd or even")