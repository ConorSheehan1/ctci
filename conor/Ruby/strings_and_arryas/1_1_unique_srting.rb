require 'set'

def is_unique(s)
	# convert string to arry, convert array to set
	# if set length is same as string length, return true
	return s.split("").to_set.length == s.length
end

print is_unique(gets().chomp())