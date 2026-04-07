with open('input.txt')as f:
    data = f.read().splitlines()
ans = 0
for line in data:
    nums, rules = line.split(':')
    rules = rules.split(' ')
    vals = [0,0,0]
    for i, color in enumerate(rules):
        bi = ""
        for char in color:
            if char.islower():
                bi += '0'
            else:
                bi += '1'
        vals[i] = int(bi, 2)
    if max(vals) == vals[1] and vals[1] != vals[0] and vals[1] != vals[2]:
        ans += int(nums)
print(ans)