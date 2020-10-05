# Given a binary tree, return all values given a certain height h.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_leveled_nodes(node, height, current_level, result):
    if current_level == height:
        result.append(node.value)
        return
    if node.left is not None:
        get_leveled_nodes(node.left, height, current_level + 1, result)
    if node.right is not None:
        get_leveled_nodes(node.right, height, current_level + 1, result)


def values_at_height(root, height):
    result = []
    get_leveled_nodes(root, height, 1, result)
    return result


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7
#          \
#           8

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(values_at_height(a, 3))
# [4, 5, 7]
