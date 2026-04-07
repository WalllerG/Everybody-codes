with open('input.txt')as f:
    data = f.read().splitlines()
ans = 0
shineness = []
for line in data:
    nums, rules = line.split(':')
    rules = rules.split(' ')
    vals = [0,0,0,0]
    for i, color in enumerate(rules):
        bi = ""
        for char in color:
            if char.islower():
                bi += '0'
            else:
                bi += '1'
        vals[i] = int(bi, 2)
    shineness.append((int(nums), sum(vals[:-1]), vals[-1]))
shineness.sort(key=lambda x:x[1])
shineness.sort(key=lambda x:x[2], reverse=True)
print(shineness[0][0])

