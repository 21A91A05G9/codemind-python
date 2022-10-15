x=0
for i in range(int(input())):
    y=input()
    if '++' in y:
        x+=1
    elif '--' in y:
        x-=1
print(x)