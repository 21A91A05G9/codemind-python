n=input()
z=0
o=0
for i in range(0,len(n)):
    x=ord(n[i])
    if(x==122):
        z+=1
    else:
        o+=1
if(2*z==o):
    print("Yes")
else:
    print("No")