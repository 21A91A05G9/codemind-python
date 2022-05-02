n=int(input())
m=int(input())
import math
f=0
for i in range(n,m+1):
    f=0
    if(i==1):
        continue;
    for j in range(2,i):
        if(i%j==0):
            f=1
            break;
    if(f==0):
        print(i)