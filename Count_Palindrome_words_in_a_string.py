a=0
for i in (input().lower()).split(' '):
    if i==i[::-1]:
        a+=1
print(a)