n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
c=[]
for i in l:
    if (i<b and i<a)  or (i>a and i>b):
        c.append(i)
if len(c)==0:
    print("-1")
else:
    print(max(c))