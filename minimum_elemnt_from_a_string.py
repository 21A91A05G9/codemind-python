s=input().split(' ')
a=1
for i in s:
    if a==len(s):
        if (min(i).lower()) in i:
            print(min(i).lower())
        else:
            print(min(i))
    a+=1