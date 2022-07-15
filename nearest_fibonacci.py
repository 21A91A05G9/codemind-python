def pri(n):
    x,y=0,1
    while(1):
        t=y
        y,x=x+t,y
        if(y>n):
            if(n-x<y-n):
                print(x)
            elif(n-x>y-n):
                print(y)
            else:
                print(x,y)
            break
import math
n=int(input())
pri(n)