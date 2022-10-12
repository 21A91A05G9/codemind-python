a,b=map(int,input().split())
m=list(map(int,input().split()))[:a]
n=list(map(int,input().split()))[:b]
c=0
p=[]
q=[]
for i in m:
    if i not in  p:
        p.append(i)
for i in n:
    if i not in q:
        q.append(i)

for i in p:
    if i not in q:
        print(i,end=' ')
for i in q:
    if i not in p:
        print(i,end=' ')