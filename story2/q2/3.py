from collections import deque
with open('input.txt') as f:
    data = list(f.read() * 100000)

head = deque(data[0:len(data) // 2])
tail = deque(data[len(data) // 2:])

rules = ["R", "G", "B"]
color_index = 0
count = 0

while head:
    count += 1
    if (len(head) + len(tail)) % 2 == 1:
        head.popleft()
    else:
        if head[0] == rules[color_index]:
            tail.popleft()
            head.popleft()
        else:
            head.popleft()
            head.append(tail.popleft())
    color_index = (color_index + 1) % 3
print(count)