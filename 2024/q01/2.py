from collections import Counter
with open('input.txt')as f:
    data = list(f.read())

ans = 0
options = {'A':0, 'B':1, 'C':3, 'D':5, 'x':0}

for i in range(0, len (data), 2):
    pair = data[i] + data[i+1]
    if 'x' in pair:
        ans += options[pair[0]] +  options[pair[1]]
    else:
        ans += options[pair[0]] +  options[pair[1]] + 2
print(ans)