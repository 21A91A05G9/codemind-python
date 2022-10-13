n=int(input())
l=list(map(int,input().split()))[:n]
k=int(input())
s=set(l)
f=0
for i in s:
    if l.count(i)==k:
        print(i,end=' ')
        f=1
if(f==0):
    print("-1")