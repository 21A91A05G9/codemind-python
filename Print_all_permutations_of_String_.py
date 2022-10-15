from itertools import permutations
vk=permutations(list(input()))
for i in vk:
    print(*i,sep='')