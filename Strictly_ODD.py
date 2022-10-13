n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(0,len(l)):
    if(l[i]%2==1 and i%2!=1):
        print(False)
        break
else:
    print(True)