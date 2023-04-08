
# 리스트 연산 (선형 배열)

# 원소 덧붙이기, 맨 끝 원소 가져오기
L = ['Bob', 'Cat', 'Spam', 'Jinny']
print(L)
L.append('New')
print(L)
a1 = L.pop()
a2 = L.pop()
print(L, a1, a2)
# --> 리스트 길이와 무관하게 상수시간에 할 수 있는 연산 : O(1)

# 리스트 길이에 따라 연산 시간이 길어지는 유형
# 원소 삭제하기, 삽입하기
L = [20, 37, 58, 72, 91]
L.insert(3, 65)
print(L)
del(L[2]) # 리스트의 특정 위치에 있는 원소 삭제
# b1 = del(L[2]) #SyntaxError
print(L)
b2 = L.pop(2) # return 값으로 삭제 원소를 받을 수 있음
print(L, b2)

# 원소 탐색하기
L = ['Bob', 'Cat', 'Spam', 'Jinny']
print(L.index('Spam'))




