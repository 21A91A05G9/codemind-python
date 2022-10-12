n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
m=0
f=0
for i in l:
    if((i>=a and i<=b) or  (i>=b and i<=a) ):
        if(m<i):
            m=i
        f=1
if(f==1):
    print(m)
else:
    print("-1")