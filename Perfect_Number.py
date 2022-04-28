n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
    i+=1
if(s==n):
    print("True")
else:
    print("False")