a,b=map(int,input().split())
m=list(map(int,input().split()))[:a]
n=list(map(int,input().split()))[:b]
m=set(m)
n=set(n)
c=0
for i in m:
    if i not in n:
        c+=1
for i in n:
    if i not in m:
        c+=1
print(c)