from collections import Counter
with open("input.txt") as f:
    data = f.read()
ans = 0
data *= 1000
for i ,char in enumerate(data):
    if char in 'abc':
        left = max(0, i-1000)
        right = i+1000
        string = data[left:right+1]
        ans += string.count(char.upper())
print(ans)
