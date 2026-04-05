from collections import Counter
with open("input.txt") as f:
    data = f.read()
ans = 0
data = [char for char in data if char in "Aa"]
for i, m in enumerate(data):
    if m == 'A':
        for j in range(i+1, len(data)):
            if data[j] == 'a':
                ans += 1
print(ans)