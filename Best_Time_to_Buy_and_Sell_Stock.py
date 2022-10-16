n=int(input())
a=list(map(int,input().split()))
minn=a[0]
for i in range(n):
    if minn>a[i]:
        minn=a[i]
        idx=i
        break
maxx=max(a[idx:n])
print(maxx-minn)