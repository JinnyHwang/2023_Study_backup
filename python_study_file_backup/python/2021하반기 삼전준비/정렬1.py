def solution(array, commands):
    
    answer = [ 0 for _ in range(len(commands))]
    answer_arr = []
    for i, c in enumerate(commands):
        print("c:",c)
        print("arr:",array[c[0]-1 : c[1]])
        answer_arr = sorted(array[c[0]-1 : c[1]])
        print("arr sort:",answer_arr)
        answer[i] = answer_arr[c[2]-1]
        print("answer[i]:",answer[i])
    
    return answer

# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

# map( 함수 , commands)
# commands의 원소를 함수를 통해 뽑은 원소로 map하여 리스트 생성
# commands의 원소 x는 아래 식을 통해 가공
# 정렬한 list의 [x[2]-1]번째 값
# lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1]
def solution1(array, commands):
    
    return list( map( lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1] , commands ) )
    


a1 = [1, 5, 2, 6, 3, 7, 4]
c1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution1(a1, c1))

