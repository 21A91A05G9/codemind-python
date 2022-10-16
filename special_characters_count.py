v=input()
r=0
for k in range(0,len(v)):
    if((ord(v[k])>32 and ord(v[k])<=47)or(ord(v[k])>=58 and ord(v[k])<=64)or(ord(v[k])>=91 and ord(v[k])<=96)or(ord(v[k])>=123 and ord(v[k])<=126)):
        r+=1
print(r)