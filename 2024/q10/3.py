from collections import Counter
import re
with open('input.txt')as f:
   grid = [list(line) for line in f.read().splitlines()]

values = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
total = 0

def solve():
    global total
    while True:
        changes_this_round = 0
        for y in range(0, len(grid) - 7, 6):
            for x in range(0, len(grid[0]) - 7, 6): 
                for i in [2, 3, 4, 5]:
                    for j in [2, 3, 4, 5]:
                        if grid[y+i][x+j] == '.':
                            row_symbols = [grid[y+i][x+k] for k in range(8) if grid[y+i][x+k] not in '.?']
                            col_symbols = [grid[y+k][x+j] for k in range(8) if grid[y+k][x+j] not in '.?']
                            row_set = set(row_symbols)
                            col_set = set(col_symbols)
                            common = row_set & col_set
                            if len(common) == 1:
                                grid[y+i][x+j] = list(common)[0]
                                changes_this_round += 1
                for i in range(8):
                    for j in range(8):
                        if grid[y+i][x+j] == '?':
                            row = [grid[y+i][x+k] for k in range(8)]
                            col = [grid[y+k][x+j] for k in range(8)]
                            if '*' not in row:
                                dots = [(y+i,x+k) for k in range(8) if grid[y+i][x+k] == '.']
                                if len(dots) == 1:
                                    dot_col = Counter(grid[y+k][dots[0][1]] for k in range(8))
                                    opts = [k for k, v in dot_col.items() if v == 1 and k != '.']
                                    if len(opts) == 1:
                                        grid[y+i][x+j] = list(opts)[0]
                                        changes_this_round += 1
                            if '*' not in col:
                                dots = [(y+k,x+j) for k in range(8) if grid[y+k][x+j] == '.']
                                if len(dots) == 1:
                                    dot_row = Counter(grid[dots[0][0]][x+k] for k in range(8))
                                    opts = [k for k, v in dot_row.items() if v == 1 and k != '.']
                                    if len(opts) == 1:
                                        grid[y+i][x+j] = list(opts)[0]
                                        changes_this_round += 1                          
        if changes_this_round == 0:
            break
    for y in range(0, len(grid) - 7, 6):
        for x in range(0, len(grid[0]) - 7, 6):
            seq = ""
            for i in range(2, 6):
                seq += "".join(grid[i+y][x+2:x+6])
            print(seq)
            if '.' not in seq:
                for i, char in enumerate(seq,start=1):
                    total += values[char] * i

solve()
print(total)