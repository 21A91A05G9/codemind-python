n=int(input())
c=0
a=list(map(int,input().split()))[:n]
for i in range(len(a)-1):
    if(a[i]<a[i+1]):
        c+=1
if(c==n-1):
    print("yes")
else:
    print("no")