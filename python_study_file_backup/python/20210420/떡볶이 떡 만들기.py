
# n : 떡 개수 / m : 떡 길이(떡 높이의 총 합)
# 떡의 개별 높이
# 적어도 m만큼의 떡을 집에 가져갈 수 있도록
# 절단기에서 설정할 수 있는 높이의 최댓값>
# 파라메트릭 서치 유형 문제 : 최적화 문제를 결정 문제로

# 이진 탐색
# start = 0
# end = 가장 긴 떡 길이

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 시작
result = 0
while start <= end :
    total = 0
    mid = (start + end) // 2

    for x in array :
        if x > mid :
            total += (x - mid)

    if total < m :
        end = mid - 1
    else :
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 mid 기록
        start = mid + 1

print(result)




