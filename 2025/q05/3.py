with open('input.txt') as f:
    data = f.read().split('\n')
def quality(id, nums):
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
    quality = int("".join(str(segment[1]) for segment in identifier))
    level = [int("".join("" if item is None else str(item) for item in segment))for segment in identifier]
    return [quality, level, id]
origin = []
compare = []
for line in data:
    left, right = line.split(':')
    left = int(left)
    origin.append(left)
    right = list(map(int, right.split(',')))
    compare.append(quality(left, right))
compare = sorted(compare, reverse=True)
ans = 0
for x, y in zip(origin, compare):
    ans += x * y[-1]
print(ans)