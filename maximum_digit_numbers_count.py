n=int(input())
l=list(map(int,input().split()))
m=0
a=[]
for i in l:
    if(len(str(i))>m):
        m=len(str(i))
        a=[]
    if(len(str(i))==m):
        a.append(i)
print(*a)