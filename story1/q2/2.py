from collections import defaultdict
with open('input.txt')as f:
    data = f.read().splitlines()

class Node():
    def __init__(self, id, rank, symbol):
        self.id = id
        self.rank = rank
        self.symbol = symbol
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.rank}, {self.symbol}, {self.left}, {self.right}"

class Tree():
    def __init__(self, root):
        self.root = root

    def add(self, n, cur):
        if n.rank < cur.rank:
            if cur.left is None:
                cur.left = n
            else:
                self.add(n, cur.left)
        else:
            if cur.right is None:
                cur.right = n
            else:
                self.add(n, cur.right)

    def messages(self, cur, level, seen=None):
        if seen == None:
            seen = defaultdict(list)
        if cur == None:
            return seen
        seen[level].append(cur.symbol)
        self.messages(cur.left, level + 1, seen)
        self.messages(cur.right, level + 1, seen)
        return seen
    
    def find_parent(self, root, target):
        if root is None or root == target:
            return None
        if root.left == target or root.right == target:
            return root
        res = self.find_parent(root.left, target)
        if res: return res
        return self.find_parent(root.right, target)
    
tree1 = None
tree2 = None
root = None

def swap(tree_a, node_a, tree_b, node_b):
    parent_a = tree_a.find_parent(tree_a.root, node_a)
    parent_b = tree_b.find_parent(tree_b.root, node_b)
    if parent_a:
        if parent_a.left == node_a:
            parent_a.left = node_b
        else:
            parent_a.right = node_b
    else:
        tree_a.root = node_b
    if parent_b:
        if parent_b.left == node_b:
            parent_b.left = node_a
        else:
            parent_b.right = node_a
    else:
        tree_b.root = node_a
    temp_left = node_b.left
    temp_right = node_b.right
    node_b.left, node_b.right = node_a.left, node_a.right
    node_a.left, node_a.right = temp_left, temp_right

pairs = {}
for line in data:
    op = line.split(' ')[0]
    if op.startswith("ADD"):
        op, id, left, right = line.split(' ')
        id = int(id.split('=')[1])
        left_rank, left_symbol = left.split('=')[1][1:-1].split(',')
        right_rank, right_symbol = right.split('=')[1][1:-1].split(',')
        if root == None:
            lr = Node(id, int(left_rank), left_symbol)
            rr = Node(id, int(right_rank), right_symbol)
            tree1 = Tree(lr)
            tree2 = Tree(rr)
            pairs[id] = [lr, rr, tree1, tree2]
            root = 0
        else:
            node1 = Node(id, int(left_rank), left_symbol)
            node2 = Node(id, int(right_rank), right_symbol)
            tree1.add(node1, tree1.root)
            tree2.add(node2, tree2.root)
            pairs[id] = [node1, node2, tree1, tree2]
    else:
        id = int(line.split(' ')[1])
        n1 = pairs[id][0]
        n2 = pairs[id][1]
        swap(pairs[id][2], n1, pairs[id][3], n2)
        temp = pairs[id][2]
        pairs[id][2] = pairs[id][3]
        pairs[id][3] = temp

t1_m = "".join(max(tree1.messages(tree1.root, 0).values(), key=len))
t2_m = "".join(max(tree2.messages(tree2.root, 0).values(), key=len))
print(t1_m + t2_m)