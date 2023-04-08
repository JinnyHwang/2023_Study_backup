
# 하드 코딩
#for i in array2 :
#    flag = 0
#    for j in array :
#        if i == j :
#            flag = 1
#            break
#    if flag :
#        print('yes')
#    else :
#        print('no')

def binary_search( array, target, start, end ) :
    while start <= end :

        mid = (start + end) // 2

        if array[mid] == target :
            return mid
        elif array[mid] < target :
            start = mid + 1
        else :
            end = mid - 1

    return None
    
n = int(input())
array = list(map(int, input().split()))

m = int(input())
array2 = list(map(int, input().split()))


for i in array2 :
    result = binary_search(array, i, 0, len(array)-1)
    if result != None :
        print('yes', end=' ')
    else :
        print('no', end=' ')
print('\n')
















