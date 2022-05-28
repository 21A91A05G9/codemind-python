n=int(input())
for i in range(n):
    for j in range(i+n):
        if(j>=n-i-1):
            print(i+1,end='')
        else:
            print(" ",end='')
    print()