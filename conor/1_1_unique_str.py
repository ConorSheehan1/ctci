def unique(st):
    return len(set(st)) == len(st)


def unique_no_datastruct(st):
    st = sorted(st)
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            return False
    return True


data = input()
while data != "":
    print(unique(data))
    print(unique_no_datastruct(data))
    data = input()
