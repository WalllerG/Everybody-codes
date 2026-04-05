from collections import defaultdict
with open('input.txt') as f:
    people = f.read().split('\n')
parents = defaultdict(list)
def is_parent(d1,d2,d3):
    for x, y, z in zip(d1,d2,d3):
        if x not in y+z:return False
    return True
def similarity(child, mom, dad):
    sim1 =  sum(x == y for x, y in zip(child, mom))
    sim2 = sum(x == z for x, z in zip(child, dad))
    return sim1 * sim2
for person in people:
    id1, dna  = person.split(':')
    for m in people:
        id2, m_dna = m.split(':')
        for d in people:
            id3, d_dna = d.split(':')
            if id1 != id2 and id1 != id3 and id2 != id3:
                if is_parent(dna, m_dna, d_dna) :
                    parents[(m_dna, d_dna)].append(dna)
ans = 0
seen = set()
for parent, kids in parents.items():
    for kid in kids:
        if kid not in seen:
            ans += similarity(kid, parent[0], parent[1])
            seen.add(kid)
print(ans)