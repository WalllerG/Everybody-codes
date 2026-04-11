
with open('input.txt')as f:
    data = int(f.read())

total = 20240000
MOD = 1111
blocks = 1
thickness = 1
gap = 3
layers = 1
while blocks < total:
    thickness = (thickness * data) % MOD
    blocks += thickness * gap
    gap += 2
    layers += 1

print((layers * 2 - 1) * (blocks-total))