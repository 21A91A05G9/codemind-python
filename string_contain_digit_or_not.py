s=input()
c=0
for i in range(0,len(s)):
    x=ord(s[i])-48
    for j in range(0,10):
        if(x==j):
            c+=1
            break
if(c>0):
    print("Contains ",end="")
    print(c,end='')
    print(" digit")
else:
    print("Doesn't contain digit")