s=input().split(' ')
vow=['a','e','i','o','u','A','E','I','O','U']
b=[]
for i in s:
    a=0
    for j in i:
        if j in vow:
            a+=1
    b.append(a)
print(min(b))