with open('input.txt') as f:
    data = f.read().split('\n')
def quality(nums):
    identifier = []
    for num in nums:
        for segment in identifier:
            if num < segment[1] and segment[0] is None:
                segment[0] = num
                break
            if num > segment[1] and segment[2] is None:
                segment[2] = num
                break
        else:
            identifier.append([None,num,None])
    return int("".join(str(segment[1]) for segment in identifier))
worst = float('inf')
best = 0
for line in data:
    left, right = line.split(':')
    left = int(left)
    right = list(map(int, right.split(',')))
    best = max(best, quality(right))
    worst = min(worst, quality(right))
print(best - worst)