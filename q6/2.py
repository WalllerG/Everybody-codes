from collections import Counter
with open("input.txt") as f:
    data = f.read()
aces = [char for char in data if char in "Aa"]
bs = [char for char in data if char in "Bb"]
cs = [char for char in data if char in "Cc"]
def pairs(lst, upper, lower):
    re = 0
    for i, m in enumerate(lst):
        if m == upper:
            for j in range(i+1, len(lst)):
                if lst[j] == lower:
                    re += 1
    return re
print(pairs(aces, 'A', 'a') + pairs(bs, 'B', 'b') + pairs(cs, 'C', 'c'))