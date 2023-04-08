
# sorted : 리스트, 딕셔너리 자료형 등을 입력받아서 정렬된 결과를 출력
# 집합 자료형, 딕셔너리 자료형을 입력받아도 반환되는 결과는 리스트 자료형
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)


# sort : 리스트 변수가 하나 있을 때 내부 원소를 바로 정렬할 수 있다.
# sort()는 리스트 객체의 내장 함수
# 별도의 정렬된 리스트 반환이 아닌, 내부 원소가 바로 정렬된다
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(array)


# 정렬 lib에서 key 활용
# 리스트의 데이터가 튜플로 구성되어 있을 때,
# 각 데이터의 두 번째 원소를 기준으로 설정하는 경우
array = [ ('바나나', 2), ('사과', 5), ('당근', 3) ]

def setting(data) :
    return data[1]

result = sorted(array, key=setting)
print(result)
# -> 구조 이해하기 어렵네 으윽

def set1(data) :
    return data[0]

result = sorted(array, key=set1)
print(result)


#정렬 lib 시간 복잡도

# 1. 정렬 lib로 풀 수 있는 문제
# 2. 정렬 알고리즘의 원리에 대해 물어보는 문제
# 3. 더 빠른 정렬이 필요한 문제

















