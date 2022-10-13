s=input()
c=0
for i in s:
    if(i==' '):
        print(c,end=' ')
        c=0
        continue
    c+=1
print(c)