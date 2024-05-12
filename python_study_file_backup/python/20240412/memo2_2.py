

COORD_SIZE = 5



def out_of_active_coordinate(x, y):
    return not(0 <= x <= COORD_SIZE) or not(0 <= y <= COORD_SIZE)

print(out_of_active_coordinate(6, 1))
print(out_of_active_coordinate(2, 8))
print(out_of_active_coordinate(0, 1))
