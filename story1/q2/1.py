from collections import defaultdict
with open('input.txt')as f:
    data = f.read().splitlines()

class Node():
    def __init__(self, rank, symbol):
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

tree1 = None
tree2 = None
root = None

for line in data:
    op, id, left, right = line.split(' ')
    id = int(id.split('=')[1])
    left_rank, left_symbol = left.split('=')[1][1:-1].split(',')
    right_rank, right_symbol = right.split('=')[1][1:-1].split(',')
    if root == None:
        tree1 = Tree(Node(int(left_rank), left_symbol))
        tree2 = Tree(Node(int(right_rank), right_symbol))
        root = 0
    else:
        tree1.add(Node(int(left_rank), left_symbol), tree1.root)
        tree2.add(Node(int(right_rank), right_symbol), tree2.root)

t1_m = "".join(max(tree1.messages(tree1.root, 0).values(), key=len))
t2_m = "".join(max(tree2.messages(tree2.root, 0).values(), key=len))
print(t1_m + t2_m)