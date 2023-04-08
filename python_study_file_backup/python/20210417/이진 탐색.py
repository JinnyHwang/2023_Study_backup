
# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례로 확인
def sequential_search (n, target, array) :
    # 각 원소를 하나씩 확인하며
    for i in range(n) :
        if array[i] == target :
            return i
    
#input_data = input().split()
#n = int(input_data[0])
#name = input_data[1]

#array = list( input().split() )
#print( sequential_search(n, name, array) + 1 )


# 이진 탐색 : 반으로 쪼개면서 탐색하기
# 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있음
# 위치를 나타내는 변수 3개 사용 : 시작점, 끝점, 중간점
# 찾으려는 데이터와 중간점(Middle) 위치에 있는 데이터를 반복적으로 비교

#graph = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#s = 0
#e = len(graph)-1
#m = len(graph)/2
#target = 4
#
#while True :
#    if s >= e :
#        print('데이터 없음')
#        break
#    
#    if graph[m] > target:
#        e = m
#        m = (e+s)/2
#    elif graph[m] < target :
#        s = m
#        m = (e+s)/2
#    else :
#        print('target index : ',m,'\n')
#        break


def binary_search1 (graph, target, start, end) :
    while start <= end :
        mid = (start+end) // 2
        if graph[mid] > target :
            end = mid - 1
        elif graph[mid] < target :
            start = mid + 1
        else :
            return mid
    return None

graph = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print( binary_search1(graph, 10, 0, len(graph)-1) )


def binary_search(array, target, start, end):
    if start > end :
        return None

    # 나누고 몫만 원할 경우 몫 연산자 // 를 사용
    mid = (end+start)//2

    if array[mid] > target :
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target :
        return binary_search(array, target, mid+1, end)
    else :
        return mid

n, target = map(int, input().split())

array = list(map(int, input().split()))

print( binary_search( array, target, 0, len(array)-1 ) +1 )













