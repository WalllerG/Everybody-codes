from collections import defaultdict
from copy import deepcopy
with open('input.txt')as f:
    data = f.read().splitlines()

smallest = float('inf')
biggest = float('-inf')
graph = {}

for line in data:
    id, target = line.split(':')
    target = target.split(',')
    graph[id] = target

DP = {}
def dfs(remaining, person):
    if (remaining, person) in DP:
        return DP[(remaining, person)]
    if remaining == 0:
        return 1
    total = 0
    for neighbour in graph.get(person, []):
        total += dfs(remaining-1, neighbour)
    DP[(remaining, person)] = total
    return total

for p in list(graph):
    total = dfs(20, p)
    smallest = min(smallest, total)
    biggest = max(biggest, total)

print(biggest - smallest)
