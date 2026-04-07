with open('input.txt')as f:
    data = [int(num) for num in f.read().split(',')]
cols_pos = {key:0 for key in range(1,91)}
for num in data:
    cur = num
    for i in range(cur, 91, num):
        cols_pos[i] += 1
print(sum(cols_pos.values()))