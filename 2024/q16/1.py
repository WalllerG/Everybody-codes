with open('input.txt')as f:
    pulls, faces = f.read().split('\n\n')
    
cats = {i:[] for i in range(1,5)}
pulls = list(map(int, pulls.split(',')))

for line in faces.splitlines():
    x, y, z, i = line[0:3], line[4:7], line[8:11], line[12:15]
    if x != '   ' and  x != '':
        cats[1].append(x)
    if y != '   ' and  y != '':
        cats[2].append(y)
    if z != '   ' and  z != '':
        cats[3].append(z)
    if i != '   ' and  i != '':
        cats[4].append(i)
        
cat1 = cats[1][(100 * pulls[0]) %  len(cats[1])]
cat2 = cats[2][(100 * pulls[1]) %  len(cats[2])]
cat3 = cats[3][(100 * pulls[2]) %  len(cats[3])]
cat4 = cats[4][(100 * pulls[3]) %  len(cats[4])]

print(" ".join((cat1, cat2, cat3, cat4)))