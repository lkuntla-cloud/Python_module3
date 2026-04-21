def due(X,Y):
    return X-Y
P=int(input("How much did you pay?: "))
H=int(input("How much was the actual bill?: "))
print("You paid the shop: ",P," and the actual bill was: ",H," The due amount is: ",due(P,H))
x=due(P,H)
if x<0:
    print("You have to pay this amount to the shop")
else:
    print("The due amount is what the shop has to pay you")