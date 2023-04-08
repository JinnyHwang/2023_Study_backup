areas = []
for i in range(1, 11):
    areas = areas + [i*i]
print("areas : ", areas)

areas2 = [ i*i for i in range(1, 11) ]
print("areas2 : ", areas2)

areas3 = []
for i in range(1, 11):
    if i%2 == 0:
        areas3 = areas3 + [i*i]
print("areas3 : ", areas3)

areas4 = [ i*i for i in range(1, 11) if i%2==0 ]
print("areas4 : ", areas4)

list1 = [ (x, y) for x in range(3) for y in range(3) ]
print(list1)

