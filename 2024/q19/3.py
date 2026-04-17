with open('input.txt')as f:
    key, G = f.read().split('\n\n')

G = G.split('\n')
R = len(G)
C = len(G[0])

def get_permutation():
    G = [[(r, c) for c in range(C)] for r in range(R)]
    mi = 0
    for r in range(R):
        for c in range(C):
            if r > 0 and r < R - 1 and c > 0 and c < C - 1:
                k = key[mi]
                mi = (mi+1)%len(key)
                M = {
                    (-1, -1): (-1, 0),
                    (-1, 0): (-1, 1),
                    (-1, 1): (0, 1),
                    (0, 1): (1, 1),
                    (1, 1): (1, 0),
                    (1, 0): (1, -1),
                    (1, -1): (0, -1),
                    (0, -1): (-1, -1)
                }
                OLD = {(dr, dc): G[r+dr][c+dc] for dr, dc in M.keys()}
                if k == 'R':
                    for (sr, sc), (fr, fc) in M.items():
                        G[r+fr][c+fc] = OLD[(sr, sc)]
                if k == "L":
                    for (fr, fc), (sr, sc) in M.items():
                        G[r+fr][c+fc] = OLD[(sr, sc)]
                        
    RET = {}
    for r in range(R):
        for c in range(C):
            RET[(r, c)] = G[r][c]
    return RET

def permutation_multiply(P, Q):
    C = {}
    for k in P.keys():
        C[k] = P[Q[k]]
    return C

def permutation_power(P, N):
    if N == 1:
        return P
    elif N % 2 == 0:
        return permutation_power(permutation_multiply(P, P), N//2)
    else:
        return permutation_multiply(P, permutation_power(P, N-1))
    
P = get_permutation()
P2 = permutation_power(P, 1048576000)

def apply_permutation(P, G):
    new_G = [['?' for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            pr, pc = P[(r, c)]
            new_G[r][c] = G[pr][pc]
    return new_G

new_grid = apply_permutation(P2, G)
for r in new_grid:
    print("".join(r))