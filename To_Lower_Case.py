n=input()
for i in range(0,len(n)):
    x=ord(n[i])
    if(x>=65 and x<=90):
        x=x+32
    print(chr(x),end='')