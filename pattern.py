x=input('enter the value')
for i in range(int(x)):
    for j in range(i+1):
        print("*",end=" ")
    print("\r")

    #reverse pattern
for i in range(int(x),0,-1):
    for j in range(i-1):
        print("*",end=" ")
    print("\r")
