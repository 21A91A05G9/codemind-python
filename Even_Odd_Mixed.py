n=int(input())
d=0
s=0
o=0
e=0
while(n>0):
    s+=1
    d=int(n%10)
    if(d%2==0):
        e+=1
    else:
        o+=1
    n=int(n/10)
if(e==s):
    print("Even")
elif(o==s):
    print("Odd")
else:
    print("Mixed")