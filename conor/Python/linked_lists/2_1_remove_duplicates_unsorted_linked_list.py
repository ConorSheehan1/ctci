from random import randint

from LinkedList import LinkedList


def remove_duplicates(some_list):
    s = set()
    new_list = LinkedList()
    # add values to set
    for val in some_list:
        s.add(val)

    # copy set back into list
    for unique in s:
        new_list.add(unique)

    return new_list


# create an unsorted linked list with random numbers 1-3
l = LinkedList()
for i in range(20):
    l.add(randint(1, 3))
print(l, l.size())

print(remove_duplicates(l))
