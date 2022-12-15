n=int(input())
c=0
l=list(map(int,input().split()))[:n]
for i in range(0,len(l)-2):
    if((l[i]%2==0 and l[i+2]%2==1) or
       (l[i]%2==1 and l[i+2]%2==0)):
           c+=1
if((l[len(l)-2]%2==1 and l[0]%2==0) or
    (l[len(l)-2]%2==0 and l[0]%2==1)):
        c+=1
if((l[len(l)-1]%2==1 and l[1]%2==0) or
    (l[len(l)-1]%2==0 and l[1]%2==1)):
        c+=1
print(c)