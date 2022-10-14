s=input()
k=''
s=set(s.lower())
for i in s:
    if(i!=' '):
        k+=i
k=''.join(sorted(k))
print(k)