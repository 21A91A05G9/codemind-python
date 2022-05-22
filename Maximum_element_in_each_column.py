n,m = map(int,input().split())
b=[]
max=0
for i in range(n):
    a = list(map(int,input().strip().split()))[:m]
    b.append(a)
for j in range(0,m):
    max=0
    for i in range(0,n):
        if b[i][j]>max:
            max=b[i][j]
    print(max)