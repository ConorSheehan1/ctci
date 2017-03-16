from Python.linked_lists.LinkedList import Node
# return min must be O(1)
# keep track of min using variable


class MinStack:
    def __init__(self, val=None):
        new_node = Node(val)
        self.head = new_node
        self.min = new_node

    def __iter__(self):
        current = self.head
        if current is None:
            return
        while current.next is not None:
            yield current
            current = current.next

    def __repr__(self):
        m = self.get_min()
        if m.val is None:
            return "empty stack"

        string = ""
        for node in self:
            string += str(node.val) + " "
        return "[" + string + "] min = " + str(m.val)

    def push(self, val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp

        if self.min.val is None or self.head.val < self.min.val:
            self.min = self.head

    def pop(self):
        temp = self.head
        if temp.val is not None:
            self.head = self.head.next

            # if the old head was the min, set the min as the new head, then iterate over stack and change min as needed
            if temp.val is self.min.val:
                self.min = self.head
                self.find_new_min()
            return temp
        raise IndexError("can't pop an empty stack")

    def get_min(self):
        return self.min

    def find_new_min(self):
        for node in self:
            if node.val < self.min.val:
                self.min = node

s = MinStack()
print(s)

for i in range(10):
    s.push(-i)
    print(s)

print()
for i in range(10):
    s.pop()
    print(s)

# should throw exception
# s.pop()
