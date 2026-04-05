with open('input.txt') as f:
    data = f.read().split('\n')
nums = [(int(data[0]), int(data[0]))]
for num in data[1:-1]:
    left, right = list(map(int, num.split('|')))
    nums.append((left, right))
nums.append((int(data[-1]), int(data[-1])))
turns = 1
cur = nums[0][0]
for left, right in nums[1:]:
    ratio = cur / left
    turns *= ratio
    cur = right
print(int(turns * 100))