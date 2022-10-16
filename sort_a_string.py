s=input()
vk=[]
for i in s:
    if i.isalpha():
        vk.append(i)
vk.sort()
r=0
for i in s:
    if i.isalpha():
        i=vk[r]
        r+=1
    print(i,end='')