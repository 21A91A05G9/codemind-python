b=[]
vow=['a','e','i','o','u']
for i in (input().lower()).split():
    c=0
    for j in list(i):
        if j in vow:
            c+=1
    b.append(c)
print(b.count(min(b)))