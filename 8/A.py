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


def depth_tree(node):
    if node is None:
        return 0
    left_depth = depth_tree(node.left)
    right_depth = depth_tree(node.right)
    return max(left_depth, right_depth) + 1

s = input().split()
num = []
for i in s:
    if int(i) == 0:
        break
    num.append(int(i))

tree = Node(num[0])
for i in range(1, len(num)):
    tree.insert(num[i])
print(depth_tree(tree))