n=int(input())
l=list(map(int,input().split()))[:n]
for i in l:
    if i%2==0:
        continue
    else:
        print(False)
        break
else:
    print(True)