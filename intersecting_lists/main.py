# You are given two singly linked lists.
# The lists intersect at some node.
# Find, and return the node. Note: the lists are non-cyclical.

# Example:

# A = 1 -> 2 -> 3 -> 4
# B = 6 -> 3 -> 4

# This should return 3 (you may assume that any nodes with the same value are the same node).

def naive_intersection(a, b):
    while a is not None:
        b_iterator = b
        while b_iterator is not None:
            if b_iterator.val == a.val:
                return b_iterator
            else:
                b_iterator = b_iterator.next
        a = a.next


def hashes_intersection(a, b):
    finished = False
    hashes = {}
    while not finished:
        finished = True
        if a is not None:
            if a.val not in hashes:
                hashes[a.val] = a.val
            else:
                return a
            finished = False
            a = a.next

        if b is not None:
            if b.val not in hashes:
                hashes[b.val] = b.val
            else:
                return b
            finished = False
            b = b.next


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def pretty_print(self):
        c = self
        while c:
            print(c.val)
            c = c.next


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = naive_intersection(a, b)
c.pretty_print()
# 3 4

d = hashes_intersection(a, b)
d.pretty_print()
