n=int(input())
s=0
c=0
a=list(map(int,input().strip().split()))[:n]
for i in a:
    if i%2==0:
        c+=1
    else:
        s+=1
print(c,s)