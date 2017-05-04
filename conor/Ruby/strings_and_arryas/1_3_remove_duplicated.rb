require 'set'

def remove_duplicates(s)
	# convert string to array, then to set to remove duplicates, then back to array to convert to string using join
	# set has no join method. could be point to use monkey patch?
	return s.split("").to_set().to_a().join()
end

print(remove_duplicates(gets().chomp()))