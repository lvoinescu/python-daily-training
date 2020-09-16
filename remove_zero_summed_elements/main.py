# Given a linked list of integers, remove all consecutive nodes that sum up to 0.

# Example:

# Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
# Output: 10

# The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed.
# 4 -> -4 also sums up to 0 too so that sequence should also be removed.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def get_size(node):
    current = node
    size = 0
    while current is not None:
        size += 1
        current = current.next
    return size


def remove_between(previous, current):
    previous.next = current.next if current.next is not None else None


def remove_consecutive_zero_sum_nodes(node):
    total_size = get_size(node)
    size = 1
    head = node
    while size < total_size:
        start = head
        previous = None
        while start is not None:
            counter = 0
            partial_sum = 0
            sum_element_node = start
            while counter < size and sum_element_node is not None:
                partial_sum += sum_element_node.value
                if partial_sum == 0:
                    if previous is None:
                        head = sum_element_node.next
                    else:
                        remove_between(previous, sum_element_node)
                    partial_sum = 0
                counter += 1
                sum_element_node = sum_element_node.next
            previous = start
            start = start.next
        size += 1
    return head


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = remove_consecutive_zero_sum_nodes(node)
while node:
    print(node.value)
    node = node.next
# 10
