with open('input.txt') as f:
    data = set(map(int, f.read().split(',')))
nums = sorted(data,reverse=True)
print(sum(nums))