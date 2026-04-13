from collections import defaultdict
with open('input.txt')as f:
    data, track = f.read().split('\n\n')
    
plans = []
for i, line in enumerate(track.splitlines()):
    if i == 2:
        plans += list(line)[::-1]
    else:
        plans += list(line)
        
plans *= 10     
level = {'+':1, '-':-1, '=':0}
orders = {}

for line in data.splitlines():
    power = 10
    id, ops = line.split(':')
    rules = ops.split(',')
    re = 0
    for j in range(len(plans)):
        if plans[j] not in '-+':
            power += level[rules[j % len(rules)]]
            re += power
        else:
            power += level[plans[j]]
            re += power
    orders[id] = re

print("".join(sorted(orders, key=lambda x:orders[x], reverse=True)))