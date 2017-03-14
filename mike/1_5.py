# replace all spaces in a string with '%20'
# have to find all space characters, then remove and replace them.
# edge cases: empty string, no spaces, all spaces. none of these seem problematic.


string = 'hi there my name is craig'

string = string.replace(' ', '%20')

print(string)
