n=input()
s=0
for i in range(0,len(n)):
    x=ord(n[i])
    for j in range(48,58):
        if(x==j):
            s+=x-48
print(s)