n=int(input())
l=list(map(int,input().split()))[:n]
a=[]
b=[]
for i in l:
    if(i%2==0):
        a.append(i)
    else:
        b.append(i)
a.extend(b)
print(*a)