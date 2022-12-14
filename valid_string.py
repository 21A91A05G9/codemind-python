s=input()
a=[]
for i in s:
    a.append(s.count(i))
c=0
b=set(a)
b=list(b)
x=[]
for i in range(0,len(b)):
    x.append(a.count(b[i]))
if(len(x)>2):
    print("Not Valid")
elif(len(x)<2):
    print("Valid String")
else:
    if(x[0]==1 or x[1]==1):
        print("Valid String")
    else:
        print("Not Valid")