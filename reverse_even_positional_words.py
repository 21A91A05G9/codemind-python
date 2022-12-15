s=input()
l=s.split()
t='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'
for i in range(0,len(l)):
    if(i%2==0):
        t+=''.join(reversed(l[i]))
        if(i!=len(l)-1):
            t+=" "
    else:
        t+=''.join(l[i])
        if(i!=len(l)-1):
            t+=" "
print(t)