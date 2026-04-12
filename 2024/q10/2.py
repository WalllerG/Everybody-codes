with open('input.txt')as f:
   data = f.read().split('\n\n')


values = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
total = 0

for part in data:
    for a in range(15):
        ans = ""
        grid = []
        for line in part.splitlines():
            line = line.split(' ')
            grid.append(list(line[a]))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '.':
                    row = set(grid[i])
                    col = []
                    for x in range(len(grid)):
                        col.append(grid[x][j])
                    col = set(col)
                    intersect = col & row
                    for inter in intersect:
                        if inter != ".":
                            ans += inter
                            break
        for c, letter in enumerate(ans, start=1):
            total += c * values[letter]
    
print(total)