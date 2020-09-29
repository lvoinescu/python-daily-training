# You are given an array of k sorted singly linked lists.
# Merge the linked lists into a single sorted linked list and return it.


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    done = False
    last = None
    result = None
    while not done:
        the_minimum = None
        the_minimum_index = -1
        for i in range(0, len(lists)):
            head = lists[i]
            if (the_minimum is None and head is not None) or (
                    the_minimum is not None and head is not None and head.val < the_minimum.val):
                the_minimum = head
                the_minimum_index = i

        if the_minimum is not None:
            if last is None:
                last = the_minimum
                result = the_minimum
            else:
                last.next = the_minimum
                last = the_minimum
            lists[the_minimum_index] = the_minimum.next
            the_minimum.next = None
        else:
            done = True
    return result


a = Node(1, Node(3, Node(5, Node(7))))
print(a)
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 1234567
