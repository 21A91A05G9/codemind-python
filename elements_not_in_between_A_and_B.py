n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
c=[]
f=0
for i in l:
    if (i<b and i<a)  or (i>a and i>b):
        c.append(i)
        f=1
if(f==0):
    print("-1")
else:
    print(*c)