with open('input.txt') as f:
    line = list(map(int, f.read().split(',')))
pairs = {}
ans = 0
for i in range(1, 17):
    pairs[i] = i+16
for i in range(32, 16, -1):
    pairs[i] = i-16
print(pairs)
for i in range(len(line)-1):
    n = line[i+1]
    if line[i] in pairs:
        if n == pairs[line[i]]:
            ans += 1
print(ans)