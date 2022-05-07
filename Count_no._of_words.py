s=input()
c=1
for i in range(0,len(s)):
    if(ord(s[i])==32):
        c+=1
print(c)