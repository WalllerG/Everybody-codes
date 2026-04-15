with open('input.txt')as f:
    data = f.read().splitlines()
   
total = set()

for line in data:
    s = (0,0,0)
    seen = set()
    for op in line.split(','):
        rule, steps = op[0], int(op[1:])
        if rule == 'D':
            for i in range(1, steps+1):
                s = s[0], s[1] - 1, s[2]
                seen.add(s)
        elif rule == 'U':
            for i in range(1, steps+1):
                s = s[0], s[1] + 1, s[2]
                seen.add(s)
        elif rule == 'R':
            for i in range(1, steps+1):
                s = s[0] + 1, s[1], s[2]
                seen.add(s)
        elif rule == 'L':
            for i in range(1, steps+1):
                s = s[0] - 1, s[1], s[2]
                seen.add(s)
        elif rule == 'F':
            for i in range(1, steps+1):
                s = s[0], s[1], s[2] + 1
                seen.add(s)
        elif rule == 'B':
            for i in range(1, steps+1):
                s = s[0], s[1], s[2] - 1
                seen.add(s)
    total |= seen

print(len(total))