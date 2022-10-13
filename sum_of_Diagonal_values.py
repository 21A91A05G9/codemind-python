n,m=map(int,input().split())
b=[]
max=0
for i in range(n):
    a = list(map(int,input().strip().split()))[:m]
    b.append(a)
for j in range(0,m):
    for i in range(0,n):
        if(i==j or i+j==n-1):
            max+=b[i][j]
print(max)