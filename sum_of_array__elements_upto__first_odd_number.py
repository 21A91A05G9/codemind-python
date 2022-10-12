n=int(input())
l=list(map(int,input().split()))[:n]
s=0
for i in range(0,len(l)):
    if(l[i]%2==1):
        break
    s+=l[i]
print(s)