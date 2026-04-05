from collections import defaultdict
with open('input.txt') as f:
    data = list(map(int, f.read().split(',')))
count = defaultdict(int)
for num in data:
    count[num] += 1
print(max(count.values()))