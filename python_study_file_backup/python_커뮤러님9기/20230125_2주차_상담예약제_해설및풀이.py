
'''
Merge Sort(병합 정렬) 알고리즘 사용
병합 정렬은 안정정렬, 분할정복알고리즘
분할 정복(divide and conquer) 방법
문제를 작은 2개의 문제로 분리하고 각각 해결 후
결과를 모아서 원래의 문제를 해결하는 전략
대게 순환호출(재귀)을 이용해서 구함

merge sort의 단계
1. 분할(divide): 입력 배열을 같은 크기의 2개 부분 배열로 분할
2. 정복(conquer): 부분 배열을 정렬. 부분 배열의 크기가 충분히 작지 않으면
순환 호출을 이용해서 다시 분할 정복 방법을 적용
3. 결합(combine): 정렬된 부분 배열들을 하나의 배열에 합병한다

merge단계에서 비교가 이루어진다
2개의 인접한 배열 list[left,...,mid] 와 list[mid+1,..., right] 합병
'''

'''
알고리즘을 큰 그림에서 보면
분할(split) / 병합(merge)
단순히 mid index를 찾아 분할하는 비용 보다
모든 값을 비교해야하는 병합 비용이 더 크다
비교를 위한 반복의 수는 점점 절반으로 줄어든다 때문에 O(logN) 시간 복잡도를 갖는다
그리고 병합할 때 모든 값을 비교해야 하므로 O(N) 시간 복잡도를 갖는다
(+) 두 개 배열을 병합할 때 결과를 담는 배열이 추가로 필요 때문에 공간 복잡도는 O(N)
단, 다른 정렬 알고리즘처럼 인접한 값들 간의 상호 자리 교대(swap)은 일어나지 않는다
'''

# 파이썬은 arr[start:end] 리스트 슬라이스를 쓸 수 있음.
# 하지만 slice할 때 배열 복제가 일어나므로 메모리 사용 효율에는 좋지 않다!

# code로 구현
def merge_sort1(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    
    merged_arr = []
    l = h = 0
    
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

# 최적화 code
# 병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고
# 인덱스 접근을 이용해서 입력 배열을 계속 업데이트하면
# 메모리 사용량을 대폭 줄일 수 있다 (In-place sort)
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        
        mid = (low + high)//2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
        
    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        
        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h +=1
        
        while l < mid:
            temp.append(arr[l])
            l += 1
            
        while h < high:
            temp.append(arr[h])
            h += 1
        
        for i in range(low, high):
            arr[i] = temp[i-low]
    
    return sort(0, len(arr))
        
        
'''
merge sort 공부했으니 이젠 풀제 풀이
1. 시간을 숫자로 바꿔주는 작업 필요
(+) 예외처리를 줄이기 위해 booked/unbooked 끝에 dummy data 추가
'''

def parse_time(t):
    # 와.. 나는 slice로 배열복제하면서 했는데..
    # map, split 활용하자!
    h, m = map(int, t.split(':'))
    return h*60 + m

def solution(booked, unbooked):
    
    # 문자열로 표현된 시간을 int형으로 변경해서 배열 초기화 + dummy(나올 수 있는 시간 최대값이 1430(23:50)여서 2000으로 잡음  )
    # 시간을 int로 바꿔서 진행하니까 중간중간 계산을 위해서 변경하는 code를 없앨 수 있다!
    booked = [ (parse_time(t), name) for t, name in booked ] + [(2000,None)]
    unbooked = [ (parse_time(t), name) for t, name in unbooked ] + [(2000,None)]
    # 각 배열은 도착시간 순으로 정렬되어 주어지는데 sort가 필요할까?
    #booked.sort()
    #unbooked.sort()
    b, u, t, answer = 0, 0, 0, []
    
    # merge sort랑 유사한 부분!
    while b < len(booked) and u < len(unbooked):
        
        t1, t2 = booked[b][0], unbooked[u][0]
        
        # booked와 unbooked 비교
        if t1 <= t:
            # (case1) else문타서 t1이 min 값일 때
            # (case2) booked 손님이 업무시간 중 방문
            answer.append(booked[b][1])
            b += 1 # 다음 booked 탐색을 위함
            # (case1) t1시간이 업무 시작시간. 업무 종료시간은 +10분
            # (case2) 바로 예약 고객 업무 진행하니까 지금 진행 시간에서 + 10분
            t += 10
        elif t2 <= t:
            # (case1) else문타서 t2이 min 값일 때
            # (case2) 업무 시간 중 unbooked 손님 방문(booked손님은 방문ㄴㄴ)
            answer.append(unbooked[u][1])
            u += 1 # 다음 unbooked 탐색을 위함
            # (case1) t2시간이 업무 시작시간. 업무 종료시간은 +10분
            # (case2) 바로 업무 진행 예정이므로 지금 진행 시간에서 + 10분
            t += 10
        else:
            # t가 현재 t1, t2값과 비교가 진행되지 않을 때
            # Ex1) 마지막 업무 진행 시간과 현재 탐색하는 업무 시간에 텀이 있을 때
            t = min(t1, t2)
    
    # 각 배열의 마지막에 dummy를 넣어주었기 때문에
    # 한 쪽 배열의 인덱스가 끝에 도달해서 while문이 끝났을 때를 위해
    # 아직 맨 끝 index에 도달하지 못한 배열을 복사해서 answer에 넣어주는 과정이 필요 없음
    # 한 쪽 배열이 맨 끝 dummy값에 도달하면 무조건 남은 배열보다 값이 크므로 값이 다 들어감
    # 둘 다 dummy data index에 도달하면 맨 처음 조건문을 통해 answer에 dummy data를 넣어주고
    # b == len(booked)로 while문이 종료
    # answer의 맨 끝 값에 들어간 dummy data를 pop해주는 과정이 필요
    
    print(answer)
    answer.pop()
    return answer 

