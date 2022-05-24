n=int(input())
c=0
a=list(map(int,input().strip().split()))[:n]
for i in a:
    if(a.count(i)==1):
        c=1
        print(i,end=" ")
if(c==0):
    print("-1")