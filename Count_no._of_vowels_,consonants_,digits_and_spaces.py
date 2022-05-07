s=input()
w=0
v=0
c=0
d=0
y=1
for i in range(0,len(s)):
    y=1
    if(ord(s[i])==32):
        w+=1
        y=0
    for j in range(0,10):
        x=ord(s[i])-48
        if(x==j):
            d+=1
            y=0
            break;
    if(s[i]=='a' or s[i]=='i' or s[i]=='o' or 
    s[i]=='u' or s[i]=='e'):
        v+=1
        y=0
    if(y==1):
        c+=1
print("Vowels: ",end='')
print(v)
print("Consonants: ",end='')
print(c)
print("Digits: ",end='')
print(d)
print("White spaces: ",end='')
print(w)