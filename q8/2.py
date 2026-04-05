with open('input.txt') as f:
    data = list(map(int, f.read().split(',')))
strings = []
total = 0
for x, y in zip(data, data[1:]):
    for a, b in strings:
        if x == a or x == b or y == a or y == b: continue
        if (a < x < b) != (a < y < b):
            total += 1
    strings.append(sorted([x, y]))
print(total)