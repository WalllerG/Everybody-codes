with open('input.txt')as f:
    data = [int(line) for line in f.read().splitlines()]
    
re = min(data)
ans = 0

for num in data:
    if num != re:
        ans += abs(num - re)
        
print(ans)