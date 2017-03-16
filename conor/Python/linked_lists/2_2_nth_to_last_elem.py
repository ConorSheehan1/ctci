from random import randint

from LinkedList import LinkedList


class BetterList(LinkedList):
    def get(self, index):
        for i, val in enumerate(self):
            if i == index:
                return val

    def get_nth_to_last(self, n):
        if n > self.size():
            return "index out of bounds"
        else:
            return self.get(self.size()-n-1)


if __name__ == "__main__":
    b = BetterList()
    for i in range(10):
        b.add(randint(1, 10))
    print(b)

    # should print list in reverse
    for i in range(b.size()):
        print(b.get_nth_to_last(i), ", ", end="")