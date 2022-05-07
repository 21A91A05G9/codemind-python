s=input()
c=0
for i in range(0,len(s)):
    x=ord(s[i])
    for j in range(0,len(s)):
        y=ord(s[j])
        if(x<y):
            break
    else:
        print(chr(x))
        break