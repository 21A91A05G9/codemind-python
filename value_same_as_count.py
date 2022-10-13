n=int(input())
l=list(map(int,input().split()))[:n]
a=[]
c=0
s=set(l)
for i in s:
    if l.count(i)==i and i not in a:
        c+=1
print(c) 