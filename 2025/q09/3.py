import networkx as nx
from collections import defaultdict
with open('input.txt') as f:
    people = f.read().split('\n')
graphs = defaultdict(set)
def is_parent(d1,d2,d3):
    for x, y, z in zip(d1,d2,d3):
        if x not in y+z:return False
    return True
seen = []
for person in people:
    id1, dna  = person.split(':')
    for m in people:
        id2, m_dna = m.split(':')
        for d in people:
            id3, d_dna = d.split(':')
            if id1 != id2 and id1 != id3 and id2 != id3:
                if is_parent(dna, m_dna, d_dna):
                    graphs[id1].add(id2)
                    graphs[id1].add(id3)
                    graphs[id2].add(id1)
                    graphs[id3].add(id1)
G = nx.Graph(graphs)
largest_component_nodes = max(nx.connected_components(G), key=len)
total_sum = sum(int(node) for node in largest_component_nodes)
print(total_sum)