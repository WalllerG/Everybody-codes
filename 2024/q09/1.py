with open('input.txt')as f:
    data = [int(line) for line in f.read().splitlines()]

stamps = [10,5,3,1]
ans = 0

for num in data:
    index = 0
    cur = num
    while cur > 0:
        if stamps[index] > cur:
            index += 1
        else:
            cur -= stamps[index]
            ans += 1
            
print(ans)