name_testing: str

name_testing = 'strings and characters'

string_stripped = name_testing.split()

print(f"{name_testing.split()}")

print(f"{string_stripped}")

print(f"I can do this: {string_stripped[0]}")

# i can even  do this:

print(f"{name_testing[0:6]}") #this  is a slice of a string

#there is a funny thing here: if we have for in that uses range() than what we have in the strings? well:

#every string is an array (wow! C language really is everywhere)
print(f"{name_testing.__len__()}")

#and we can "use" range inside the brackets
# something like this: 
# print(f"{name_testing[range(0,name_testing.__len__(), -1)]}")
# this does not work, well it would be messy if it did

#but this works!
print(f"{name_testing[::-1]}")
#cool!

name_testing = list(name_testing)

print(f"{name_testing.__reversed__()}") #gives the memory address, there is no other method to reverse a string
