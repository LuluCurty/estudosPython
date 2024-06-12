from random import sample

list1 = sample(range(0, 80 ), 15)

print (list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
list1.extend(range(5))
print(list1)

# .append only puts one element while extend can be used for iterated 

list1.append(range(2)) 
print(list1)
print(type(list1[list1.__len__()-1]))

list2 = sample(range(0,33), 5)

list3 = list1 + list2
print(list3)

list2 = list3.copy()

print(list2)

print(list1)

list1.reverse() 
print(list1)

