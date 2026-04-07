import re
from functools import lru_cache
from collections import defaultdict
with open('input.txt')as f:
    data = f.read().split('\n\n')
graph = {id+1: [0, [], []] for id in range(len(data))}
for i, plant in enumerate(data):
    plant_id = i + 1
    lines = plant.splitlines()
    nums = re.findall(r"\d+", lines[0])
    graph[plant_id][0] = int(nums[1]) if len(nums) > 1 else int(nums[0])

    for connections in lines[1:]:
        if "free" in connections:
            continue
        else:
            target_id, thickness = re.findall(r"\d+", connections)
            graph[plant_id][1].append(int(target_id))
            graph[plant_id][2].append(int(thickness))
@lru_cache(None)
def get_energy(p_id):
    if not graph[p_id][1]:
        return graph[p_id][0]
    incoming_total = 0
    sources = graph[p_id][1]
    branch_thicknesses = graph[p_id][2]
    for src_id, branch_thick in zip(sources, branch_thicknesses):
        incoming_total += get_energy(src_id) * branch_thick
    plant_threshold = graph[p_id][0]
    if incoming_total >= plant_threshold:
        return incoming_total
    else:
        return 0
final_plant_id = len(data)
print(get_energy(final_plant_id))