user = input("enter a string")
for i in range(len(user)-1, -1, -1):
    print(user[i], end="")

# same thing
print(user[::-1])