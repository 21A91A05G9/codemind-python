n=int(input())
l=list(map(int,input().split()))[:n]
if(len(l)%2==0):
    print(*l)
else:
    l.append(0)
    print(*l)