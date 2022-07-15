def pal(n):
    s=str(n)
    r=''.join(reversed(s))
    if(r==str(n)):
        return 1
    else:
        return 0
def pri(n):
    if(n==1):
        return 0
    if(n==2):
        return 2
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
import math
n=int(input())
n+=1
while(n):
    if(pal(n) and pri(n)):
        print(n)
        break
    n+=1