n=int(input())
s=0
x=n*n
while(x>0):
    d=int(x%10)
    s+=d
    x=x//10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")