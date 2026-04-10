import re
with open('input.txt')as f:
    data = f.read().splitlines()

ans = 0

def move(x, y, length):
    if 100 % length == 0:
        return x + 100 * y
    x_pos = [a if a <= length else a % length for a in range(x,x+length)]
    y_pos = [a if a > 0 else a + length for a in range(y,y-length,-1)]
    return x_pos[100 % length] + 100 * y_pos[100 % length]

for line in data:
    x, y = list(map(int, re.findall(r"\d+", line)))
    cycle_len = x + y - 1
    ans += (move(x, y, cycle_len))

print(ans)

