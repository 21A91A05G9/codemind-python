def sub(vk,o,a):
    for a in range(a+1,len(o)):
            vk.append(o[a])
def arrange(vk,e,o):
    m=min(len(e),len(o))
    for i in range(m):
        vk.append(e[i])
        vk.append(o[i])
        a=i
    if(len(o)>len(e)):
        sub(vk,o,a)
    else:
        sub(vk,e,a)
v=input()
r=0
e,o=[],[]
for k in range(0,len(v)):
    if((ord(v[k])>32 and ord(v[k])<=47)or(ord(v[k])>=58 and ord(v[k])<=64)or(ord(v[k])>=91 and ord(v[k])<=96)or(ord(v[k])>=123 and ord(v[k])<=126)):
        r+=1
    if(v[k]>='0' and v[k]<='9'):
        if int(v[k])%2==0:
            e.append(v[k])
        else:
            o.append(v[k])
vk=[]
if r%2==0:
   arrange(vk,e,o)
else:
    arrange(vk,o,e)
print(*vk,sep='')