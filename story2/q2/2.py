from collections import deque
with open('input.txt')as f:
    data = deque(f.read() * 100)
rules = ["R","G","B"]
color_index = 0
count = 0
while data:
    cur = data[0]
    count += 1
    if cur == rules[color_index]:
        if data:
            opposite = len(data) / 2
            if opposite.is_integer():
                del data[int(opposite)]
            data.popleft()
        color_index = (color_index + 1) % 3
    else:
        data.popleft()
        color_index = (color_index + 1) % 3
print(count)