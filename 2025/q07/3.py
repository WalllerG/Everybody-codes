with open("input.txt") as f:
    p1, p2 = f.read().split('\n\n')
rules = {}
names = []
possible = set()
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
        names.append(word)
def generate(prefix):
    output = set()
    if len(prefix) >= 7: output.add(prefix)
    if len(prefix) >= 11: return output
    for next in rules.get(prefix[-1],[]):
        output |= generate(prefix + next)
    return output
for name in names:
    possible |= generate(name)
print(len(possible))
