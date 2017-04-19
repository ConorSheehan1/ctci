# could modify set of stacks?
class Towers:
    def __init__(self, numtowers):
        self.size = numtowers
        # towers has n towers of n size
        self.towers = [[None] * numtowers for _ in range(numtowers)]

        # set up initial config
        for i in range(numtowers):
            self.towers[0][i] = i+1

    def __repr__(self):
        ans = ""
        for i in range(self.size):
            for j in range(self.size):
                ans += "{:10}".format(str(self.towers[j][i]))
            ans += "\n"
        return ans

    def put_on_tower(self, tower, item):
        t = self.towers[tower]
        for i in range(self.size-1, -1, -1):
            if t[i] is None:
                t[i] = item
                return True
        print("error, tower {} full".format(tower))
        return False

    def take_off_tower(self, tower):
        for i in range(self.size):
            current = self.towers[tower][i]
            if current is not None:
                to_return = current
                self.towers[tower][i] = None
                return to_return

    def solve(self):
        while True:
            pass


t = Towers(3)
print(t)
t.take_off_tower(0)
t.take_off_tower(0)
print(t)

t.put_on_tower(0, 10)
print(t)

t.put_on_tower(1, 10)
print(t)