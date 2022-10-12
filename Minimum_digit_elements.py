n=int(input())
import math
l=list(map(int,input().split()))
x=min(l)
y=int(math.log10(x))+1
c=0
for i in l:
    if(int(math.log10(i)+1)==y):
        c+=1
print(c)