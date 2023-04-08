
#string과 문자열
my_list = [1, 2, 3, 4, 5, 6]
print(my_list[0])
print(my_list[1])

str = "Hello World"
print(str[0])
print(str[1])

print(3 in my_list)
print(30 in my_list)

print("H" in str)
print("Z" in str)

print(my_list.index(5))
print(str.index("r"))

characters = list(str)
print(characters)

words = "안녕 지금은 11시54분"
word_list = words.split()
print(word_list)

time_str = "10:35:27"
time_list = time_str.split(":")
print(time_list)
# join
print(":".join(time_list))

print(" ".join(word_list))

