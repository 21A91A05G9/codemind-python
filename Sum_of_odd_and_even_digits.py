n=int(input())
e=0
o=0
a=list(map(int,input().strip().split()))[:n]
for i in range(0,n):
    if(i%2==0):
        e+=a[i]
    else:
        o+=a[i]
if(abs(e-o)==0):
    print("YES")
else:
    print("NO")
    