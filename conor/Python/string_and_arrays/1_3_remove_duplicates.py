# strings are immutable in python so this doesn't really work without a separate buffer
# can do something like this, but order isn't preserved, and string is casted to set
def rem_dup(some_string):
    return "".join(set(some_string))


# can do something like this (cast string to list, which is mutable)
# can't use for loop because range won't update when length of list changes
def rem_dup_arr(arr):
    arr = list(arr)
    i = 0
    while i < len(arr)-1:
        current = arr[i]
        j = i+1
        while j < len(arr):
            if arr[j] == current:
                # remove index from list
                arr.pop(j)
            j += 1
        i += 1
    return "".join(arr)

user = input("enter a string to remove duplicates from")
print(rem_dup(user))
print(rem_dup_arr(user))



