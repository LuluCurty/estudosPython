test:str
test ="I AM SIMPLY A TEST!"
print(f"{enumerate(test)}")
for i, v in enumerate(test):
    print(f"Indice {i} com valor {v}")

print(test.__len__())
print(len(test))
