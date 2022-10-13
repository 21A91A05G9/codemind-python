n=int(input())
l=list(map(int,input().split()))[:n]
a=[]
f=0
for i in l:
    if l.count(i)==i and i not in a:
        a.append(i)
        f=1
if(f==0):
    print("-1")
else:
    print(*a)   