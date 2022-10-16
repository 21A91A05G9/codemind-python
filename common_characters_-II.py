s1=list(set(input().lower()))
s2=list(set(input().lower()))
a=0
for i in s1:
    if i==' ':
        continue
    elif i in s2:
        a+=1
print(a)