with open('input.txt') as f:
    data = [int(line)for line in f.read().splitlines()]
def done_one(nums):
    return nums == sorted(nums)
count = 0
while not done_one(data):
    count += 1
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i] -= 1
            data[i+1] += 1
left_over = 10 - count
while count < 10:
    count += 1
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            data[i] += 1
            data[i+1] -= 1
ans = 0
for i, num in enumerate(data):
    ans += (i+1) * num
print(ans)