s=input()
s=list(s.lower())
k=''
for i in s:
    if(i!=' ' and s.count(i)==1):
        k+=i
k=''.join(sorted(k))
print(k)