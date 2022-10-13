s=input()
c=0
m=999
for i in s:
    if(i==' '):
        if(m>c):
            m=c
            c=0
        continue
    c+=1
if(m>c):
    m=c
print(m)