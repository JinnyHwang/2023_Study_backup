
# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range( len(array) - 1) :
    min_index = i
    for j in range( i+1, len(array) ) :
        if array[min_index] > array[j] :
            min_index = j

    if min_index != i :
        array[min_index], array[i] = array[i], array[min_index]

print('선택 정렬 : ', array, '\n')


# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range( 1, len(array) ) :
    for j in range(i, 0, -1) : #range(i, 0, -1)는 i ~ 1 까지
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]


print('삽입 정렬 : ', array, '\n')
            

# 퀵 정렬 : 리스트의 맨 첫 번 째 원소가 pivot
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array) :

    if len(array) <= 1 :
        return array

    pivot = array[0]
    tail = array[1:]

    left = [ x for x in tail if x < pivot ]
    right = [x for x in tail if x > pivot ]

    return quick_sort(left) + [pivot] +  quick_sort(right)

print('퀵 정렬', quick_sort(array), '\n')

