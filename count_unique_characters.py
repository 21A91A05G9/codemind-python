s=input()
s=list(s.lower())
k=0
for i in s:
    if(i!=' ' and s.count(i)==1):
        k+=1
print(k)