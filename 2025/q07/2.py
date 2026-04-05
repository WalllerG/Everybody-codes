with open('input.txt') as f:
    p1, p2 = f.read().split('\n\n')
rules = {}
ans = 0
for rule in p2.split('\n'):
    bigger, smaller = rule.split(' > ')
    rules[bigger] = smaller.split(',')
for j, word in enumerate(p1.split(',')):
    valid = True
    for i in range(len(word)-1):
        left = word[i]
        right = word[i+1]
        if right not in rules[left]:
            valid = False
            break
    if valid:
        ans += j + 1
print(ans)