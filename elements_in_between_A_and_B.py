n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
f=0
for i in range(0,len(l)):
    if((l[i]>=a and l[i]<=b) or  (l[i]>=b and l[i]<=a) ):
        print(l[i],end=' ')
        f=1
if(f==0):
    print("-1")