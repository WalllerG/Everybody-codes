with open('input.txt') as f:
    data = f.read().split('\n')
nums = [int(x) for x in data]
turns = 1
cur = nums[0]
for num in nums[1:]:
    ratio = cur / num
    turns *= ratio
    cur = num
print(10000000000000 // turns + 1)
