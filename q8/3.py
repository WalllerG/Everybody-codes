with open('input.txt') as f:
    data = list(map(int, f.read().split(',')))
memo = [[0] * 256 for _ in range(256)]
def add(r1, c1, r2, c2):
    if r1 < 1: return
    if c1 < 1: return
    if r1 > 256: return
    if c1 > 256: return
    memo[r1-1][c1-1] += 1
    if c2 < 256: memo[r1-1][c2] -= 1
    if r2 < 256: memo[r2][c1-1] -= 1
    if c2 < 256 > r2: memo[r2][c2] += 1
for x, y in zip(data, data[1:]):
    a, b = sorted([x, y])
    add(a+1, b+1, b-1, 256)
    add(1, a+1, a-1, b-1)
for r in range(1, 256):
    for c in range(256):
        memo[r][c] += memo[r-1][c]
for r in range(256):
    for c in range(1, 256):
        memo[r][c] += memo[r][c-1]
print(max(map(max,memo)))  