n=int(input())
matrix=[]
c=0
s=0
for i in  range(n):
    a=list(map(int,input().split()))[:n]
    matrix.append(a)
for i in range(n):
    for j in range(n):
        if(i==j):
            c+=matrix[i][j]
        if(i+j==(n-1)):
            s+=matrix[i][j]
print("Principal Diagonal:",end='')
print(c)
print("Secondary Diagonal:",end='')
print(s)