n,k=map(int,input().split())
a=list(map(int,input().split()))[:n]
c=0
for i in range(0,n):
    s=0
    for j in range(i,n):
        s+=a[j]
        if(s==k):
            c+=1
print(c)
        
    