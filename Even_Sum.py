n=int(input())
a=list(map(int,input().split()))[:n]
e=0
for i in range(0,n):
    if a[i]%2==0:
        e+=a[i]
print(e)