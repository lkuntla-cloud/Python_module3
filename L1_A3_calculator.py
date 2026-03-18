def add(Q,P):
   return Q+P 
def sub(Q,P):
    return Q-P
def mult(Q,P):
    return Q*P
def div(Q,P):
    return Q/P

print("Please select any below operation: ")
print("a. addition")
print("b: subtraction")
print("c. multiplication")
print("d. division")

choice=input("Please select your Option: ")
num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))

if choice=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",mult(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("Invalid option")