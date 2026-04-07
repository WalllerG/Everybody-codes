with open('input.txt')as f:
    data = f.read().splitlines()
ans = 0
red_matte = []
red_shinny = []
green_matte = []
green_shinny = []
blue_matte = []
blue_shinny = []
for line in data:
    nums, rules = line.split(':')
    rules = rules.split(' ')
    vals = [['red', 0],['green', 0],['blue', 0],[None, 0]]
    for i, color in enumerate(rules):
        bi = ""
        for char in color:
            if char.islower():
                bi += '0'
            else:
                bi += '1'
        vals[i][1] = int(bi, 2)
    if vals[-1][1] <= 30:
        color = sorted(vals[:-1], key=lambda x:x[1], reverse=True)[0][0]
        top = sorted(vals[:-1], key=lambda x:x[1], reverse=True)[0][1]
        second = sorted(vals[:-1], key=lambda x:x[1], reverse=True)[1][1]
        if top > second:
            if color == 'red':
                red_matte.append(int(nums))
            elif color == 'green':
                green_matte.append(int(nums))
            elif color == 'blue':
                blue_matte.append(int(nums))
    elif vals[-1][1] >= 33:
        color = sorted(vals[:-1], key=lambda x:x[1], reverse=True)[0][0]
        top = sorted(vals[:-1], key=lambda x:x[1], reverse=True)[0][1]
        second = sorted(vals[:-1], key=lambda x:x[1], reverse=True)[1][1]
        if top > second:
            if color == 'red':
                red_shinny.append(int(nums))
            elif color == 'green':
                green_shinny.append(int(nums))
            elif color == 'blue':
                blue_shinny.append(int(nums))
total = [red_matte, red_shinny, green_matte, green_shinny, blue_matte, blue_shinny]
print(sum(sorted(total, key=len, reverse=True)[0]))
