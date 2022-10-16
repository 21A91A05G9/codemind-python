n=int(input())
v=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
r=[]
for i in range(len(v)):
    r.insert(k[i],v[i])
print(*r)