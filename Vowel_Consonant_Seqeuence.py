vow=['a','e','i','o','u']
vk=list(input())
v=[vk[0]]
k=0
for i in range(1,len(vk)):
    if(v[k] in vow)and(vk[i] in vow):
        continue
    elif(v[k] not in vow)and(vk[i] not in vow):
        continue
    else:
        v.append(vk[i])
        k+=1
r=''
for k in v:
    if k in vow:
        r+='V'
        continue
    r+='C'
print(r)