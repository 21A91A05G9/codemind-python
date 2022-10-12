n=int(input())
l=list(map(int,input().split()))[:n]
c=0
for i in l:
    i=str(i)
    x=''.join(reversed(i))
    if(x==i):
        c+=1
print(c)
