n,m=map(int,input().split())
nn=list(map(int,input().split()))[:n]
mm=list(map(int,input().split()))[:m]
for i in mm:
    if i not in nn:
        print("No")
        break
    nn.remove(i)
else:
    print("Yes")