n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
s=0
for i in range(0,len(l)):
    if((l[i]>=a and l[i]<=b) or  (l[i]>=b and l[i]<=a) ):
        s+=l[i]
print(s)