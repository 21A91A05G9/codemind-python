n=int(input())
for i in range(0,n):
    for j in range(0,n-i):
        print(chr(65+n-1-i),end=' ')
    print()