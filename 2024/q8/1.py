
with open('input.txt')as f:
    data = int(f.read())

possible = []
s = 1
gap = 1

for i in range(10000):
    possible.append((s, gap))
    gap += 2
    s += gap
    
for num in possible:
    if num[0] > data:
        print((num[0] - data) * num[1])
        break
