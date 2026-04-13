from collections import defaultdict, Counter
import heapq
with open('input.txt')as f:
    data = f.read().splitlines()

tree = {}

for line in data:
    root, branches = line.split(':')
    branches = branches.split(',')
    for fruit in branches:
        tree[root] = branches

def dfs(cur, visited, path, all_paths):
    path.append(cur)
    visited.add(cur)
    if cur == '@':
        all_paths.append(list(path))
    else:
        for branch in tree.get(cur, []):
            if branch not in visited:
                dfs(branch, visited, path, all_paths)
    path.pop()
    visited.remove(cur)
    return all_paths
     

print("".join(char[0] for char in (dfs('RR', set(), [], [])[5])))