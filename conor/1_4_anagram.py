def anagram(s1, s2):
    s2 = list(s2)
    for char in s1:
        if char in s2:
            s2.remove(char)
        else:
            return False
    return len(s2) == 0

print(anagram(input("enter a string"), input("enter another")))