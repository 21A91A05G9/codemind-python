vow=['a','e','i','o','u','A','E','I','O','U']
for i in (input()).split():
    c=0
    for j in i:
        if j in vow:
            c+=1
    print(c,end=' ')