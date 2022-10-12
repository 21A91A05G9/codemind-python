a=int(input())
l=list(map(int,input().split()))[:a]
k=[]
for i in range(0,len(l),2):
    x=l[i+1]
    while(x):
        k.append(l[i])
        x-=1
print(*k)