class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"


def evaluate(node):
    if node.val in (PLUS, MINUS, TIMES, DIVIDE):
        left_operand = evaluate(node.left)
        right_operand = evaluate(node.right)
        if node.val == PLUS:
            return left_operand + right_operand
        if node.val == MINUS:
            return left_operand - right_operand
        if node.val == TIMES:
            return left_operand * right_operand
        if node.val == DIVIDE:
            return left_operand / right_operand
    else:
        return node.val


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45
