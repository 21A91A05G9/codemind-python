n=int(input())
l=list(map(int,input().split()))[:n]
c=0
for i in range(0,len(l)-2):
    if l[i]%2==1 and l[i+1]%2==1 and l[i+2]%2==1:
        c+=1
print(c)