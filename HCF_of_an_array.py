n=int(input())
l=list(map(int,input().split()))
d=max(l)
while(d):
    if(l[0]%d==0 and l[1]%d==0 and l[2]%d==0):
        print(d)
        break
    d-=1