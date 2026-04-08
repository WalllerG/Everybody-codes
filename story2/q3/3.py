import re
with open('input.txt')as f:
    data, grid = f.read().split('\n\n')

class Die():
    def __init__(self, id, faces, seed):
        self.id = id
        self.faces = faces
        self.seed = seed
        self.pulse = seed
        self.roll_num = 1
        self.face = 0
    
    def roll(self):
        spin = self.roll_num * self.pulse
        self.face = (spin + self.face) % len(self.faces)
        self.pulse += spin
        self.pulse %= self.seed
        self.pulse += 1 + self.roll_num + self.seed
        self.roll_num += 1
        return self.faces[self.face]
  
grid = [list(map(int, line)) for line in grid.splitlines()]
aggregate  = set()
dies = []

for line in data.splitlines():
    info = re.findall(r"-?\d+", line)
    id, faces, seed = int(info[0]), list(map(int, info[1:-1])), int(info[-1])
    dies.append(Die(id, faces, seed))

for die in dies:
    value = die.roll()
    possible = set((r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == value)
    aggregate |= possible
    while len(possible) > 0:
        value = die.roll()
        next_set = set()
        for r, c in possible:
            for nr, nc in [(r+1, c),(r-1,c),(r,c+1),(r,c-1),(r, c)]:
                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): continue
                if grid[nr][nc] != value: continue
                next_set.add((nr, nc))
        possible = next_set
        aggregate |= possible
print(len(aggregate))
     
     