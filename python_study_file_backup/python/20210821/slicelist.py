
numbers = list(range(10))
print(numbers)

del numbers[0]
print(numbers)

#[1, 2, 3, 4, 5, 6, 7, 8, 9]
#시작 index data는 무조건  삭제됨
#del numbers[::-3] #9부터 삭제
del numbers[::3] #1부터 삭제
print(numbers)

print(numbers[1:3])

numbers[1:3] = [77, 88]
print(numbers)

numbers[1:3] = [77, 88, 99, 1010]
print(numbers)

numbers[1:3] = [8]
print(numbers)


