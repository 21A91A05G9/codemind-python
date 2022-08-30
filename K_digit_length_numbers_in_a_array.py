n,k=map(int,input().split())
l=list(map(int,input().split()))[:n]
c=0
for i in l:
    t=str(abs(i))
    if(len(t)==k):
        c+=1
print(c)