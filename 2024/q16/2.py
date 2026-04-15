from collections import Counter
with open('input.txt')as f:
    pulls, faces = f.read().split('\n\n')
    
cats = {i:[] for i in range(len(faces.splitlines()[0].split(' ')))}
pulls = list(map(int, pulls.split(',')))
total = 0

for line in faces.splitlines():
    for k in cats.keys():
        x = line[k*3+k:k*3+k+3]
        if x != '   ' and  x != '':
            cats[k].append(x)

seen = {}
for i in range(1, 202420242024+1):
    res = ""
    for id, faces in cats.items():
        res += cats[id][(i * pulls[id]) %  len(faces)][0] + cats[id][(i * pulls[id]) %  len(faces)][2]
    if res in seen:
        break
    score = Counter(res)
    seen[res] = sum((v-2) for v in score.values() if v >= 3)

vals = list(seen.values())
total += sum(vals) * (202420242024 - 202420242024 % len(seen)) // len(seen)
for i in range(202420242024 % len(seen)):
    total += vals[i]
    
print(total)