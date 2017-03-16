class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val=None):
        self.head = Node(val)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.val
            current = current.next

    def __repr__(self):
        s = ""
        for node in self:
            s += str(node) + ", "
        # remove trailing comma
        return "[" + s[:-2] + "]"

    def add(self, val):
        current = self.head
        if current.val is None:
            current.val = val
            return
        while current.next is not None:
            current = current.next
        current.next = Node(val)

    def remove(self, index=0):
        # will throw error if index is out of bounds of list
        if index == 0:
            to_return = self.head
            self.head = self.head.next
            return to_return.val

        i = 0
        current = self.head
        while i < index-1:
            current = current.next
            i += 1

        to_return = current
        current.next = current.next.next
        return to_return.val

    def size(self):
        count = 0
        for val in self:
            count += 1
        return count
