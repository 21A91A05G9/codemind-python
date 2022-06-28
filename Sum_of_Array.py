n=int(input())
a=list(map(int,input().split()))[:n]
e=0
for i in range(0,n):
    e+=a[i]
print(e)