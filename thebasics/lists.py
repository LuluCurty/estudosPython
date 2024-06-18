from random import sample
import copy 

"""

list1 = sample(range(0, 80 ), 15)
print (f"This is the LIST:\n{list1}")

# Sorting the list
list1.sort() 
print(f"This is the sorted list:\n{list1}")

# Reversing the list
list1.reverse()
print(f"This is the reversed list:\n{list1}")

# Extending the list
list1.extend(range(5))
print(f"This is the extended list:\n{list1}")

# .append only puts one element while extend can be used for iterated 

list1.append(range(2)) 
print(f"This is the appended list:\n{list1}")
print(f"This is a little test:\n{type(list1[list1.__len__()-1])}")

# Another list
list2 = sample(range(0,33), 5)

# Adding lists
list3 = list1 + list2
print(f"This is the added list:\\n{list3}")

# Copy list to another list. 
# Assignment statements do not copy objects, they create bindings between a target and an object
list2 = list3.copy()

print(f"Coppied list:\n{list2}")

list1.reverse() 
print(f"Normalizing the first list:\n{list1}")



# Copy method from copy module:

# usage:

li1 = sample(range(0, 99), 5)
print(f"The content of li1 is: {li1} while it's id is: {id(li1)}")

# Trying to use assigment satement to copy

li2 = li1
print(f"The content of li2 is: {li2} while it's id is: {id(li2)}")

# shallow copy

li2 = copy.copy(li1)
print(f"The content of li1 is: {li1} while it's id is: {id(li1)}")
print(f"The content of li2 is: {li2} while it's id is: {id(li2)}")

# modifying the lists and to see the results:

li1.append(2)
li2.append(3)

print(f"The content of li1 is: {li1} while it's id is: {id(li1)}")
print(f"The content of li2 is: {li2} while it's id is: {id(li2)}")

print(f"li: id:value")
for index in range(len(li1)):
    print(f"Li1 The id and value are: {id(li1[index])}:{li1[index]}")

for index in range(len(li2)):
    print(f"Li2 The id and value are: {id(li2[index])}:{li2[index]}")

for o, c in zip(li1, li2):
    if(c is o):
        print(f"This {c} is a copy of {o}")
        
# deep copy:
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)

for index in range(len(li1)):
    print(f"Li1 The id and value are: {id(li1[index])}:{li1[index]}")

for index in range(len(li3)):
    print(f"Li3 The id and value are: {id(li3[index])}:{li3[index]}")

for o, c in zip(li1, li3):
    if(c is o):
        print(f"This {c} is a copy of {o}")
    else:
        print(f"This {c} is NOT a copy of {o}")

"""


