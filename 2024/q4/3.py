with open('input.txt')as f:
    data = [int(line) for line in f.read().splitlines()]

median = sorted(data)[len(data) // 2]
ans = 0

for num in data:
    ans += abs(num - median)
    
print(ans)