string_true = 'uniqae'
string_false = 'unique'

def unique_str(string):
    if len(string) == len(set(string)):
        return True
    return False

print(unique_str(string_true), 'should be true')
print(unique_str(string_false), 'should be false')
