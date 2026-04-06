with open('input.txt')as f:
    data = [int(line) for line in f.read().splitlines()]
safe = [1]
left = []
right = []
for i in range(len(data)):
    if i % 2 == 0:
        right.append(data[i])
    else:
        left.append(data[i])
safe = safe + right + left[::-1]
print(safe[2025 % len(safe)])