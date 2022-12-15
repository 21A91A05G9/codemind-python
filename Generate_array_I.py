n=int(input())
a=[]
l=list(map(int,input().split()))
for i in range(0,len(l),2):
    while(l[i+1]):
        a.append(l[i])
        l[i+1]-=1
print(*a)