n=int(input())
l=list(map(int,input().split()))[:n]
x=max(l)
import math
c=0
y=int(math.log10(x))+1
for i in l:
    if(int(math.log10(i))+1==y):
        c+=1
print(c)