class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.value)

tree = Node(5)
tree.left = Node(1)
tree.right = Node(4)
tree.left.left = Node(3)
tree.left.left.left = Node(7)
tree.left.left.right = Node(6)
tree.left.right = Node(8)
tree.right.left = Node(9)
tree.right.right = Node(2)

def get_tree(node,level = 0):
    if node != None:
        get_tree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        get_tree(node.right, level + 1)

get_tree(tree)

def invertTree(tree):
    if tree != None:
        tree.left, tree.right = invertTree(tree.right), invertTree(tree.left)
        return tree

invertTree(tree)

print("\n\n")
get_tree(tree)

def lca(root, j, k):
    path_to_j = path_to_x(root, j)
    path_to_k = path_to_x(root, k)

    lca_to_return = None
    while path_to_j and path_to_k:
        j_pop = path_to_j.pop()
        k_pop = path_to_k.pop()
        if j_pop is k_pop:
            lca_to_return = j_pop
        else:
            break
    return lca_to_return

def path_to_x(root, x):
    if root is None:
        return None
    if root.value == x:
        return [root]
    left_path = path_to_x(root.left, x)
    if left_path is not None:
        left_path.append(root)
        return left_path
    right_path = path_to_x(root.right, x)
    if right_path is not None:
        right_path.append(root)
        return right_path
    return None

print("\n\n")
print(lca(tree, 6, 8))