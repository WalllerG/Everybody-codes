with open('input.txt') as f:
    data = [int(line)for line in f.read().splitlines()]
target = sum(data) // len(data)
check = [num for num in data if num < target] 
ans = 0
for num in check:
    ans += target - num
print(ans)