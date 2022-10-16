s1=list(set(input().lower()))
s2=list(set(input().lower()))
a=0
for i in s1+s2:
    if i==' ':
        continue
    elif(i not in s1 and i in s2)or(i not in s2 and i in s1):
        a+=1
print(a)