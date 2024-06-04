smallest = None

print("Before:", smallest)

for itervar in [ 41, 12, 9, 74, 15]:
    if (smallest is None) or (itervar < smallest):
        smallest = itervar
        break ##this is wrong, can you figure why?

    print("Loop:", itervar, smallest)
   
print("Smallest:", smallest)