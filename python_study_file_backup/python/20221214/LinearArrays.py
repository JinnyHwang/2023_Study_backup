
#배열(arrays)
#원소들을 순서대로 늘어놓은 것. index 0 1 2 3 4...

#리스트(lists)
#data type을 섞어서 늘어놓을 수 있음. 길이 상관없음.

l = ['Bob', 'Cat', 'Spam', 'Programmers']
print(l[1])
print(l[-2])

#리스트(배열) 연산

# 순식간에 할 수 있는 일. 리스트 길이와 무관(상수시간) O(1)
#1.원소 덧붙이기
l.append('New')
print(l)
#2. 끝에서 꺼내기
print(l.pop())
print(l)


l2 = [20, 37, 58, 72, 91]
print(l2)
# 리스트 크기에 비례함
#3. 원소 삽입하기
l2.insert(3, 65)
print(l2)
'''
insert는 어떻게 동작하는가?
3번째에 삽입해야하기 때문에 위치를 찾음
맨 끝에 있는 원소를 하나 옮김. 20 37 58 72 91 91
다음 끝 원소를 하나 옮김. 20 37 58 72 72 91
해당 위치에 도달하면 원하는 원소를 넣음 20 37 58 65 72 91
'''

#4. 원소 삭제하기
del(l2[2])
print(l2)
'''
del은 어떻게 동작하는가?
2번째 원소를 삭제해야하기 때문에 위치를 찾음
해당 위치 원소를 다음 원소로 땡김 20 37 65 65 72 91
맨 끝자리까지 땡김 20 37 65 72 91 91
맨 끝 원소 삭제 20 37 65 72 91
'''








