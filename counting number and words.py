#counting numbers
n=int(input("enter the no:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("the number are", count)
#counting letter in sentence
string=input("enter the sentence")
count=0
for i in range(len(string)):
    count=count+1
print(count)

#counting the both numbers and letter
string=input("enter the number and letter")
count1=0
count2=0
for i in string:
    if(i.isdigit()):
        count1=count1+1
    count2=count2+1
print("number of digit:",count1)
print("number of letter:",count2)
