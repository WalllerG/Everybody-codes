from collections import deque
with open('input.txt')as f:
    data = deque((f.read()))
rules = ["R","G","B"]
color_index = 0
count = 0
while data:
    cur = data.popleft()
    count += 1
    if cur == rules[color_index]:
        if data:
            n = data.popleft()
            while data and n == rules[color_index]:
                n = data.popleft()
        color_index = (color_index + 1) % 3
    else:
        color_index = (color_index + 1) % 3
print(count)