# solution using counting dictionaries
# anagrams must have the same length, character set and relative character frequency
# function tests length, then creates dictionary of values in original string
# next loop checks that character exists and decrements if so
# if this value is less than 0, character frequency is not equal and so returns false
# if character does not exist, character set is not equal and so false
# if loop terminates, length, set and frequency are all upheld and string is an anagram


orig = 'abba'
anag = 'baba'
nonag = 'babb'
diff_letters = 'babc'
diff_length = 'a'

def anagram_test(orig, test):
    if len(orig) != len(test):
        return False

    count_dict = {}
    for char in orig:
        if char in count_dict.keys():
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    for char in test:
        if char in count_dict.keys():
            count_dict[char] -= 1
            if count_dict[char] < 0:
                return False
        else:
            return False

    return True

print(anagram_test(orig, anag), '== True') # actual anagram
print(anagram_test(orig, nonag), '== False') # same letters, different frequencies
print(anagram_test(orig, diff_letters), '== False') # different letters, same length
print(anagram_test(orig, diff_length), '== False') # different length
print(anagram_test('', ''), ' ==True') # empty string
