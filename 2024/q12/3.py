from collections import defaultdict
with open('input.txt')as f:
    nums = [list(map(int, line.split(' '))) for line in f.read().splitlines()]

A = (0,0)
B = (0,1)
C = (0,2)
c_range = defaultdict(list)
b_range = defaultdict(list)
a_range = defaultdict(list)
ans = 0
            
def get_range():
        for i in range(1, 4000): #time
            sx, sy = C[0], C[1]
            #going up
            for _ in range(i):
                sx, sy = sx+1, sy+1
                c_range[i].append((sx, sy))
            #going forward
            for _ in range(i):
                sx, sy = sx+1, sy
                c_range[i].append((sx, sy))
            #going down
            while sy > 0:
                sx, sy = sx+1, sy-1
                c_range[i].append((sx, sy))

        for i in range(1, 4000): #time
            sx, sy = B[0], B[1] 
            #going up
            for _ in range(i):
                sx, sy = sx+1, sy+1
                b_range[i].append((sx, sy))
            #going forward
            for _ in range(i):
                sx, sy = sx+1, sy
                b_range[i].append((sx, sy))
            #going down
            while sy > 0:
                sx, sy = sx+1, sy-1
                b_range[i].append((sx, sy))
                
        for i in range(1, 4000): #time
            sx, sy = A[0], A[1]  
            #going up
            for _ in range(i):
                sx, sy = sx+1, sy+1
                a_range[i].append((sx, sy))
            #going forward
            for _ in range(i):
                sx, sy = sx+1, sy
                a_range[i].append((sx, sy))
            #going down
            while sy > 0:
                sx, sy = sx+1, sy-1
                a_range[i].append((sx, sy))
        
get_range()

for x, y in nums:
    rank = float('inf')
    
    #for c
    cx, cy = C
    t = (x - cx) / 2
    if t.is_integer():
        for power, vals in c_range.items():
            if len(vals) >= t:
                if vals[int(t)-1][1] == y - int(t):
                    rank = min(rank, power * 3)
                    break      
    else:
        t = (x-1 - cx) / 2
        if t.is_integer():
            for power, vals in c_range.items():
                if len(vals) >= t:
                    if vals[int(t)-1][1] == y - 1 - int(t):
                        rank = min(rank, power * 3)
                        break
                    
    #for b
    cx, cy = B
    t = (x - cx) / 2
    if t.is_integer():
        for power, vals in b_range.items():
            if len(vals) >= t:
                if vals[int(t)-1][1] == y - int(t):
                    rank = min(rank, power * 2)
                    break           
    else:
        t = (x-1 - cx) / 2
        if t.is_integer():
            for power, vals in b_range.items():
                if len(vals) >= t:
                    if vals[int(t)-1][1] == y - 1 - int(t):
                        rank = min(rank, power * 2)
                        break
                    
    #for a
    cx, cy = A
    t = (x - cx) / 2
    if t.is_integer():
        for power, vals in a_range.items():
            if len(vals) >= t:
                if vals[int(t)-1][1] == y - int(t):
                    rank = min(rank, power)
                    break        
    else:
        t = (x-1 - cx) / 2
        if t.is_integer():
            for power, vals in a_range.items():
                if len(vals) >= t:
                    if vals[int(t)-1][1] == y - 1 - int(t):
                        rank = min(rank, power)
                        break
    ans += rank
    
print(ans)