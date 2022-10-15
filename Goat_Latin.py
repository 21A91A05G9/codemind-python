s=list(input().split(' '))
vow=['a','e','i','o','u','A','E','I','O','U']
a=1
vk=''
for i in s:
    if i[0] in vow:
        vk+=str(i)
    else:
        vk+=str(i[1:len(i)])
        vk+=str(i[0])
    vk+='ma'
    vk+=a*'a'
    if(a==len(s)):
        break
    vk+=' '
    a+=1
print(vk)