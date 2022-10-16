i=int(input())
v=list(map(int,input().split()))
k=[]
for i in v:
    if v.count(i)>1:
        k.append(i)
k=list(set(k))
print(*k)