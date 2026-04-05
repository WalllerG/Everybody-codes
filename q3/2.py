with open('input.txt') as f:
    data = set(map(int, f.read().split(',')))
nums = sorted(data)[0:20]
print(sum(nums))