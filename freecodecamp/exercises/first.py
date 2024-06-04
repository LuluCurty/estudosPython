#excepetions:


a = "5 b's"

try:
    b= float(a/5)
except:
    if a.__contains__('5'):
        b = 0.0

print(b)