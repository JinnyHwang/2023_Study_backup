
# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range( len(array) ) :
    min_index = i
    for j in range( i+1, len(array) ) :
        if array[min_index] > array[j] :
            min_index = j
            
    # swap = array[i]
    # array[i] = min
    # array[index] = swap

    # 파이썬 swap
    array[min_index], array[i] = array[i], array[min_index]

print(array)

# swap
# array[i], array[j] = array[j], array[i]


# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(array)
for i in range(1, len(array)) :
    # i부터 0까지 -1씩 감소하면서
    for j in range(i, 0, -1) :
        # 바로 왼쪽 원소랑 비교하여 값이 작으면 swap
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]
        # 바로 왼쪽 원소랑 비교하여 값이 크면 정렬 종료
        else :
            break

print(array)


# 퀵 정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치 변경
# 피벗(pivot) : 큰 숫자와 작은 숫자를 교환할 때의 기준
# 대표적 분할 방법 : 호어 분할 (Hoare Partition)

# 퀵정렬 전 피벗을 어떻게 설정할 것인지 미리 명시해야한다


# 1. 리스트에서 첫 번째 데이터를 피벗으로 설정
list = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_1 (array, start, end) :
    if start >= end : # 원소가 1개인 경우 종료
        return

    # 피벗은 첫 번째 원소
    pivot = start
    left = start+1
    right = end

    while left <= right :

        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot] :
            left += 1

        while right >= start+1 and array[right] >= array[pivot] :
            right -= 1

        # 엇갈린 경우. array[left] > array[right]
        # pivot과 작은 값 swap
        if left > right :
            array[pivot], array[right] =  array[right], array[pivot]
        # 엇갈리지 않았을 경우 left, right swap
        else :
            array[left], array[right] = array[right], array[left]

    # 한차례 정렬이 끝난 뒤 pivot을 기준으로 좌우 quick_sort 진행
    quick_sort_1(array, start, right - 1)
    quick_sort_1(array, right + 1, end)

quick_sort_1(array, 0, len(array) - 1 )
print('\n기본 퀵정렬\n', array)


# 파이썬의 장점을 살린 퀵정렬
list = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_2 (array) :

    # 리스트가 한개 이하 원소를 담고있을 경우 종료
    if len(array) <= 1 :
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [ x for x in tail if x <= pivot ] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot ] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽부분, 오른쪽부분 각각 정렬 수행, 전체 리스트 반환
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

print('\n파이썬 퀵정렬\n', quick_sort_2(array))


# 계수 정렬 Count Sort
# 특정 조건이 부합할 때만 사용할 수 있는 매우 빠른 정렬 알고리즘

print('\n계수 정렬')
# 리스트 탐색하여 원소가 리스트에 포함된 횟수를 count
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * ( max(array) + 1 )

for i in range( len(array) ) :
    count[ array[i] ] += 1 # 각 데이터에 해당하는 인덱스 값 증가

for i in range( len(count) ) :
    for j in range(count[i]) :
        print(i, end=' ')































