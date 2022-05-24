n=int(input())
b=[]
c=[]
s=0
a=list(map(int,input().strip().split()))[:n]
for i in a:
    if i not in c:
        b.append(a.count(i))
        c.append(i)
for i in b:
    s+=i//2
print(s)
