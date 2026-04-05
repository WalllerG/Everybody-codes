with open('input.txt') as f:
    one, two, three = f.read().split('\n')
child = three.split(':')[1]
mom = one.split(':')[1]
dad = two.split(':')[1]
m = 0
d = 0
for x, y, z in zip(child, mom, dad):
    if x == y:m += 1
    if x == z:d += 1
print(m * d)