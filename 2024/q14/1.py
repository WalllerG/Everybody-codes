with open('input.txt')as f:
    data = f.read().split(',')
   
s = (0,0)
ans = 0
for op in data:
    rule, steps = op[0], int(op[1:])
    if rule == 'L':
        s = s[0], s[1] - steps
    if rule == 'R':
        s = s[0], s[1] + steps
    if rule == 'U':
        s = s[0] + steps, s[1]
        ans = max(ans, s[0])
    if rule == 'D':
        s = s[0] - steps, s[1]
    
print(ans)