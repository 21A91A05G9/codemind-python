import math
def fun(n):
    if(n==1):
        return 1
    s=1+n
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            s+=i
            if(i*i!=n):
                s+=n/i
    return s
a=list(map(int,input().split(",")))
c=0
b=[]
for i in a:
    if fun(i) in a:
        b.append(i)
        c=1
if(c==0):
    print("-1")
else:
    b.sort()
    for i in b:
        print(i,end=' ')
    
        
    