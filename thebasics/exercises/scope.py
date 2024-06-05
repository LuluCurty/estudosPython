i_am_global: bool
i_am_global = True

def change_global():
    not_global: bool
    not_global = False
    print(f"global is: {i_am_global} and not global: {not_global}")

#this does not works
#print(f"global is: {i_am_global} and not global: {not_global}")
