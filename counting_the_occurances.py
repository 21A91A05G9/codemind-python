s=input()
z=input()
c=0
for i in range(0,len(s)):
    if(s[i]==z):
        c+=1

if(c==0):
    print("-1")
else:
    print(c)