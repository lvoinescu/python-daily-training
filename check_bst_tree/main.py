# You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise.
# Recall that a binary search tree has the property that all values in the left subtree are
# less than or equal to the root, and all values in the right subtree are greater than or equal to the root.


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        return self.key


def is_bst(node):
    print(node.key, end=" ")
    if (node.left is not None and node.left.key > node.key) \
            or (node.right is not None and node.right.key < node.key):
        return False
    left_ok = True if node.left is None else is_bst(node.left)
    right_ok = True if node.right is None else is_bst(node.right)
    return left_ok and right_ok


#        5
#       / \
#      3   7
#     / \  /
#     1 4 6
a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#        5
#       / \
#      3   7
#     / \  /
#     1 4 8

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(8)
print(is_bst(a))
