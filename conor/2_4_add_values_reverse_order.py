from LinkedList import LinkedList
from random import randint

def get_value(l):
    ans = 0
    for i, val in enumerate(l):
        # giv digits value in reverse order (3->4->5) = 543
        ans += val *(10**i)
    return ans

# example given
list1 = LinkedList()
list1.add(3)
list1.add(1)
list1.add(5)

list2 = LinkedList()
list2.add(5)
list2.add(9)
list2.add(2)


print(list1, list2)
print(get_value(list1) , "+", get_value(list2), "=",  get_value(list1) + get_value(list2))
print()

# random test
l1, l2 = LinkedList(), LinkedList()
for i in range(3):
    l1.add(randint(0, 9))
    l2.add(randint(0, 9))

print(l1, l2)
print(get_value(l1) , "+", get_value(l2), "=",  get_value(l1) + get_value(l2))


