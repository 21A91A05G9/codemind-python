s=''
for i in input():
    if i!=' ':
        s+=i
print(min(s),s.count(min(s)),max(s),s.count(max(s)))