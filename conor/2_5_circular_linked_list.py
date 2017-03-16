from LinkedList import LinkedList, Node
from random import randint

class CircularList(LinkedList):

    def __repr__(self):
        s = ""
        visited = []
        for node in self:
            if visited.count(node) > 1:
                break

            # add pipe to show repeated values
            elif visited.count(node) > 0:
                s += "|"

            s += str(node.val) + ", "
            visited.append(node)
        # remove trailing comma
        return "[" + s[:-2] + " ...]"

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def get(self, index):
        for i, val in enumerate(self):
            if i == index:
                return val

    def add_helper(self, node):
        current = self.head
        if current.val is None:
            self.head = node
            return
        while current.next is not None:
            current = current.next
        current.next = node

    def add(self, val):
        # if val is a node, pass in
        if type(val) == type(Node()):
            self.add_helper(val)
        # otherwise cast to node
        else:
            self.add(Node(val))

    def find_loop_start(self):
        visited = []
        for node in self:
            if node in visited:
                return "node at index {} with value {} starts the loop".format(visited.index(node), node.val)
            visited.append(node)

c = CircularList()
# n = Node(4)
# c.add(n)

for i in range(5):
    c.add(randint(1, 100))

# get node from list
loop_start = c.get(randint(0, c.size()-1))
c.add(loop_start)
print(c)

print(c.find_loop_start())




