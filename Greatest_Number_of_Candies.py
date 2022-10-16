n=int(input())
v=list(map(int,input().split()))
r=int(input())
for k in v:
    if k+r>=max(v):
        print('True',end=' ')
    else:
        print('False',end=' ')