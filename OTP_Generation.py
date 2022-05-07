s=input()
for i in range(0,len(s)):
    x=ord(s[i])-48
    if(x%2==0):
        continue
    else:
        print(x*x,end='')