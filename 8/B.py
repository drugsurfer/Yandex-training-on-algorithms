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


def depth_node(tree, key, depth = 0):
    depth += 1
    if key == tree.node:
        return depth
    elif key > tree.node:
        return depth_node(tree.right, key, depth)
    else:
        return depth_node(tree.left, key, depth)

s = input().split()
num = []
for i in s:
    if int(i) == 0:
        break
    num.append(int(i))
result = []
check = {}
tree = Node(num[0])
for i in range(1, len(num)):
    tree.insert(num[i])
for i in range(len(num)):
    if num[i] in check.keys():
        continue
    result.append(depth_node(tree, num[i]))
    check[num[i]] = True
print(*result)