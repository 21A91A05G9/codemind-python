s1=input().lower().split()
s2=input().lower().split()
k=[]
s=s2+s1
for i in s:
    if s.count(i)==2 and i not in k:
        k.append(i)
print(*k)