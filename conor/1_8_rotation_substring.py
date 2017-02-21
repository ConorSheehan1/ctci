def is_substring(s1, s2):
    return s1 in s2


# only works if you don't encounter duplicate letter at start of string
# when un-rotating (eg "wowhow, howwow" wouldn't work
def rotation(s1, s2):
    for i in range(len(s2)-1):
        # move last character to front of string
        last_char = s2[-1]
        s2 = last_char + s2[:-1]
        if last_char == s1[0]:
            print(s1, s2)
            return is_substring(s1, s2)

print(rotation("waterbottle", "erbottlewat"))
print(rotation("wowhow", "howwow"))