from collections import defaultdict
with open('input.txt')as f:
    data = f.read().splitlines()

nodes = defaultdict(list)

class Node:
    NODES_BY_ID = defaultdict(list)
    def __init__(self, id, weight, letter, left=None, right=None):
        self.id = id
        self.weight = weight
        self.letter = letter
        self.left = left
        self.right = right
        self.NODES_BY_ID[id].append(self)

    def __repr__(self):
        return f"Node({self.id!r}, {self.weight!r}, {self.letter!r}{'' if self.left is None else f', left={self.left!r}'}{'' if self.right is None else f', right={self.right!r}'})"
    def __lt__(self, other: "Node"):
        return self.weight < other.weight
    
    @classmethod
    def swap_nodes(cls, id):
        nodes = cls.NODES_BY_ID[id][-2:]
        l, r = nodes
        l.weight, r.weight = r.weight, l.weight
        l.letter, r.letter = r.letter, l.letter
    
    @classmethod
    def swap_branches(cls, id):
        nodes = cls.NODES_BY_ID[id][-2:]
        l, r = nodes
        l.weight, r.weight = r.weight, l.weight
        l.letter, r.letter = r.letter, l.letter
        l.left, r.left = r.left, l.left
        l.right, r.right = r.right, l.right
    
    @classmethod
    def reset(cls):
        cls.NODES_BY_ID.clear()

class Tree:
    def __init__(self, root=None):
        self.root = root
    def add(self, node: Node):
        if self.root is None:
            self.root = node
            return
        root = self.root
        while True:
            if node < root:
                if root.left is None:
                    root.left = node
                    return
                root = root.left
            else:
                if root.right is None:
                    root.right = node
                    return
                root = root.right
    def __repr__(self):
        return f"Tree({self.root!r})"
    def at_depth(self, n):
        return "".join(self._nodes_depth(self.root, n))
    @staticmethod
    def _nodes_depth(node, depth):
        if node is None: return
        if depth < 0: return
        if depth > 0:
            yield from Tree._nodes_depth(node.left, depth - 1)
            yield from Tree._nodes_depth(node.right, depth - 1)
        else:
            yield node.letter

tree1 = Tree()
tree2 = Tree()

for line in data:
    op = line.split(' ')[0]
    if op.startswith("ADD"):
        op, id, left, right = line.split(' ')
        id = int(id.split('=')[1])
        left_rank, left_symbol = left.split('=')[1][1:-1].split(',')
        right_rank, right_symbol = right.split('=')[1][1:-1].split(',')
        tree1.add(Node(id, int(left_rank), left_symbol))
        tree2.add(Node(id, int(right_rank), right_symbol))
    else:
        id = int(line.split(' ')[1])
        Node.swap_branches(id)

print(max((tree1.at_depth(i) for i in range(10)), key = len)+max((tree2.at_depth(i) for i in range(10)), key = len))