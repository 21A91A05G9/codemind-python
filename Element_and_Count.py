n=int(input())
l=list(map(int,input().split()))[:n]
a=[]
b=[]
c=[]
for i in l:
    if i not in a:
        a.append(i)
        b.append(l.count(i))
for i in range(0,len(a)):
    c.append(a[i])
    c.append(b[i])
print(*c)
    