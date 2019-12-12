n=int(input())
result=0
#while loop
while n>0:
    digit=n%10
    result=result+digit
    n=n//10
print(result)


#anthor method using for loop

n=int(input("enter the number"))
result=0
for i in range(len(str(n))):
     digit=n%10
     result=result+digit
     n=n//10
print("sum is",result)


