vk=0
for i in input():
    if i=='R' or i=='U':
        vk+=1
    else:
        vk-=1
if(vk==0):
    print('True')
else:
    print('False')