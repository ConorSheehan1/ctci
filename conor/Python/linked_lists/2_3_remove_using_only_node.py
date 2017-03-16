from random import randint

from LinkedList import LinkedList


class HardMode(LinkedList):

    def __repr__(self):
        s = ""
        for node in self:
            s += str(node.val) + ", "
        # remove trailing comma
        return "[" + s[:-2] + "]"

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def remove_with_node(self, node):
        for i, val in enumerate(self):
            if val == node:
                self.remove(i)

    def other_remove_with_node(self, node):
        current = self.head
        # if you're removing the head
        if current == node:
            pass

        while current.next != node and current.next is not None:
            current = current.next
        try:
            current.next = current.next.next
        # if you're removing from the end of the list
        except AttributeError:
            current.next = None

if __name__ == "__main__":
    h = HardMode()
    for i in range(10):
        h.add(randint(10, 100))

    # both remove_with_node and other_remove_with_node do the same thing
    # this should remove from the start of the list until the list is empty
    for node in h:
        h.other_remove_with_node(node)
        print(h)



