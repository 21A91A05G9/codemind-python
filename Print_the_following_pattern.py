n=int(input())
for i in range(n):
    x=i;
    y=1;
    for j in range(i+n):
        if(j>=n-i-1):
            if(j>n-1):
               print(chr(x+64),end='')
               x-=1;
            if(j==n-1):
               print(chr(64+i+1),end='')
            if(j<n-1):
                print(chr(y+64),end='')
                y+=1;
        else:
            print(" ",end='')
    print()