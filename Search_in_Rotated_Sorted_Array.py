n=int(input())
v=list(map(int,input().split()))
r=int(input())
for k in range(len(v)):
    if v[k]==r:
        print(k)
        break
else:
    print(-1)
