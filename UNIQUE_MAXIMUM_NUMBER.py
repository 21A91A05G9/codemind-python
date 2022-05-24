n=int(input())
b=[]
c=0
a=list(map(int,input().strip().split()))[:n]
for i in a:
    if(a.count(i)==1):
        c=1
        b.append(i)
if(c==1):
    print(max(b))
else:
    print("-1")