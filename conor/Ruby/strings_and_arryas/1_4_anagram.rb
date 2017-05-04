def is_anagram(s1, s2)
	# convert to lowercase, convert to array, sort, check if arrays are same
	arr1 = s1.downcase().split("").sort()
	arr2 = s2.downcase().split("").sort()
	return arr1 == arr2
end

print(is_anagram(gets().chomp(), gets().chomp()))