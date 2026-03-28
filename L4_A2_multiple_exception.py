try:
    num1,num2=eval(input("Enter two numbers seperated by a comma: "))
    result=num1/num2
    print("The result of the numbers is =", result)
except SyntaxError:
    print("The syntax is wrong! You have to give a comma between the numbers!")
except ZeroDivisionError:
    print("The number is divisble by Zero!")
except:
    print("The input is wrong!")
else:
    print("There is no exception")
finally:
    print("The code finally will always be executed")