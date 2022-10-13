n=int(input())
l=list(map(int,input().split()))[:n]
x=sum(l)//len(l)
c=0
for i in l:
    if i<=x:
        c+=1
print(c)