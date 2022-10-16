n=int(input())
r=list(map(int,input().split()))
v=k=0
for i in range(len(r)):
    if i%2==0:
        v+=r[i]
    else:
        k+=r[i]
if abs(v-k)%4==0:
    print('X')
else:
    print('Y')