from collections import Counter
with open('input.txt')as f:
    data = list(f.read())

ans = 0
options = {'A':0, 'B':1, 'C':3, 'D':5, 'x':0}

for i in range(0, len (data), 3):
    pair = data[i] + data[i+1] + data[i+2]
    x_count = Counter(pair)
    if x_count['x'] > 1:
        ans += options[pair[0]] +  options[pair[1]] + options[pair[2]]
    elif x_count['x'] == 1:
        ans += options[pair[0]] +  options[pair[1]] + options[pair[2]] + 2
    else:
        ans += options[pair[0]] +  options[pair[1]] + options[pair[2]] + 6

print(ans)