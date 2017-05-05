def replace_spaces(s)
	for i in 0..s.length()-1
		if s[i] == " "
			s[i] = "%20"
		end
	end
	return s
end

print(replace_spaces(gets().chomp()))