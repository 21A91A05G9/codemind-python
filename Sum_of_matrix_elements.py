n=int(input())
m=int(input())
b=[]
max=0
for i in range(n):
    a = list(map(int,input().strip().split()))[:m]
    b.append(a)
for j in range(0,m):
    for i in range(0,n):
        max+=b[i][j]
print(max)