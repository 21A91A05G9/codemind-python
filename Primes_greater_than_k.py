import math
def fun(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))[:n]
k=int(input())
c=0
s=0
for i in a:
    if(i>=k):
        if(fun(i)):
            s+=1
print(s)