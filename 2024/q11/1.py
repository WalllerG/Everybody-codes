from collections import defaultdict
from copy import deepcopy
with open('input.txt')as f:
    data = f.read().splitlines()

population = ['A']
graph = defaultdict(list)

for line in data:
    id, target = line.split(':')
    target = target.split(',')
    for t in target:
        graph[id].append(t)

for _ in range(4):
    new_pop = []
    for person in population:
        new_pop += graph[person]
    population = new_pop

print(len(population))