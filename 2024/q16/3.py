from collections import Counter
with open('input.txt')as f:
    pulls, faces = f.read().split('\n\n')
    
cats = {i:[] for i in range(len(faces.splitlines()[0].split(' ')))}
pulls = list(map(int, pulls.split(',')))
total = 0
indexs = [0,0,0,0,0]

for line in faces.splitlines():
    for k in cats.keys():
        x = line[k*3+k:k*3+k+3]
        if x != '   ' and  x != '':
            cats[k].append(x)

memo_max = {}
memo_min = {}

def get_score_logic(current_indices):
    res = ""
    for i, idx in enumerate(current_indices):
        face_str = cats[i][idx % len(cats[i])]
        res += face_str[0] + face_str[2]
    counts = Counter(res)
    return sum((v - 2) for v in counts.values() if v >= 3)

def solve(pull_num, target, current_indices, is_max=True):
    state = (pull_num, tuple(current_indices))
    cache = memo_max if is_max else memo_min
    if state in cache:
        return cache[state]
    if pull_num == target:
        return 0
    results = []
    for shift in [-1, 0, 1]:
        shifted = [(idx + shift) % len(cats[i]) for i, idx in enumerate(current_indices)]
        next_indices = [(shifted[i] + pulls[i]) % len(cats[i]) for i in range(len(pulls))]
        score = get_score_logic(next_indices)
        results.append(score + solve(pull_num + 1, target, next_indices, is_max))

    final_val = max(results) if is_max else min(results)
    cache[state] = final_val
    return final_val

target_pulls = 256
memo_max, memo_min = {}, {}

print(f"{solve(0, target_pulls, indexs, is_max=True)} {solve(0, target_pulls, indexs, is_max=False)}")