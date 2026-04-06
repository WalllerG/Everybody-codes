with open('input.txt') as f:
    data = [int(line)for line in f.read().splitlines()]
def done_one(nums):
    return nums == sorted(nums)
def is_balanced(nums):
    return set(nums) == {nums[0]}
count = 0
while not done_one(data):
    count += 1
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i] -= 1
            data[i+1] += 1
while not is_balanced(data):
    count += 1
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            data[i] += 1
            data[i+1] -= 1
print(count)