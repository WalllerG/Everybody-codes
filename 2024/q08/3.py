
with open('input.txt')as f:
    data = int(f.read())

total = 202400000
MOD = 10
blocks = 1
thickness = 1
col_height = [1]

while True:
    thickness = (thickness * data) % MOD + MOD
    new_height = [thickness] + [x + thickness for x in col_height] + [thickness]
    blocks = sum(new_height)
    remove = sum((data * len(new_height)) * x % MOD for x in new_height[1:-1])
    after = blocks - remove
    col_height = new_height
    if after > total:
        print(after - total)
        break