def prime(n):
    c=0
    i=1
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    else:
        if(n!=1):
            return True
n=int(input())
r=0
x=0
if(prime(n)):
    while(n>0):
        x+=1
        d=n%10
        if(prime(d)):
            r+=1
        n=n//10
    if(x==r):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")