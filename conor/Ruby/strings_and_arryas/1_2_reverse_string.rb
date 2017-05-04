def reverse(s)
	a = ""
	for i in (s.length-1).downto(0)
		a = a + s[i]
	end
	return a
end

print reverse(gets().chomp())