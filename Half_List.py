n=int(input())
b=n
a=list(map(int,input().strip().split()))[:n]
while(n>b//2):
    print(a[n-1],end=' ')
    n-=1
for i in range(0,b//2):
    print(a[i],end=' ')
    
    