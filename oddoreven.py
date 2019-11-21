x=int(input('start number'))
y=int(input('end number'))
print("even number")
for i in range(x,y):
    if i%2==0:
        print(i,end=" ")
print("\nodd number")
for j in range(x,y):
    if j%2!=0:
        print(j,end=" ")
