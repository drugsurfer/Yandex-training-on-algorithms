class Node():
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

    def insert(self, node):
        if self.node:
            if node < self.node:
                if self.left is None:
                    self.left = Node(node)
                else:
                    self.left.insert(node)
            elif node > self.node:
                if self.right is None:
                    self.right = Node(node)
                else:
                    self.right.insert(node)
        else:
            self.node = node

    def print_node(self, tree):
        if tree:
            self.print_node(tree.left)
            print(tree.node)
            self.print_node(tree.right)

s = input().split()
num = []
for i in s:
    if int(i) == 0:
        break
    num.append(int(i))
tree = Node(num[0])
for i in range(1, len(num)):
    tree.insert(num[i])
tree.print_node(tree)
