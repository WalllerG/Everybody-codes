
with open('input.txt')as f:
    data = f.read().splitlines()

level = {'+':1, '-':-1, '=':0}
orders = {}

for line in data:
    power = 10
    id, ops = line.split(':')
    rules = ops.split(',')
    re = 0
    for i in range(10):
        power += level[rules[i % len(rules)]]
        re += power
    orders[id] = re
    
print("".join(sorted(orders, key=lambda x:orders[x], reverse=True)))