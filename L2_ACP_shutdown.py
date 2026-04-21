def shutdown():
    print("system shutting down")
    SystemExit
for i in range(2):
    #asking the question twice incase the person made a mistake
    x=input("Do you want to exit the system? Type yy if this is second time we are asking this question (y/n/yy): ")
    if x=="y":
        print("are you sure?")
        i=+1
    elif x=="yy":
        shutdown()
    else:
        print("shutdown abort")
        break