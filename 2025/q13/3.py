import re
with open('input.txt')as f:
    data = [list(map(int, line.split('-'))) for line in f.read().splitlines()]
safe = [1]
left = []
right = []
for i in range(len(data)):
    if i % 2 == 0:
        right.append(data[i])
    else:
        left.append(data[i][::-1])
safe = safe + right + left[::-1]
total_len = 1 + sum(abs(x - y) + 1 for x, y in safe[1:])
index = 202520252025 % total_len
count = 0
for x, y in safe[1:]:
    if index > count + abs(x - y) + 1:
        count += abs(x - y) + 1
        continue
    else:
        print(x + index - count - 1 if x < y else x - (index - count - 1))
        break