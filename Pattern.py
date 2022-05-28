n=int(input())
for i in range(n):
    x=i;
    y=1;
    for j in range(i+n):
        if(j>=n-i-1):
            if(j>n-1):
               print(x,end='')
               x-=1;
            if(j==n-1):
               print(i+1,end='')
            if(j<n-1):
                print(y,end='')
                y+=1;
        else:
            print(" ",end='')
    print()