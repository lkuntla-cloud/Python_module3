a=input("Enter a name: ")
b=input("Enter a letter which you want to search: ")
for i in a:
    if i==b:
        print(b," is found")
        break
    else:
        print(b," is not found")