n=int(input())
v=list(map(int,input().split()))
v=list(set(v))
v.sort()
if n<3:
    print(max(v))
else:
    print(v[-3])