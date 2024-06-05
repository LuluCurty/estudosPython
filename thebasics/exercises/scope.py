i_am_global: bool
i_am_global = True

def change_global():
    not_global: bool
    not_global = False
    print(f"global is: {i_am_global} and not global: {not_global}")
    return 0

#this does not works
#print(f"global is: {i_am_global} and not global: {not_global}")

change_global()

a: int 
a = 0
a =range(1, 10)

print(a)
a = change_global
print(a)
