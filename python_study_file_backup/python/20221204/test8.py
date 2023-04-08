
import heapq

# 강의가 끝나는 시간을 기준으로 sort:O(NlogN) + 강의 개수:O(N)
# 강의가 끝나는 시간을 기준으로 sort? 강의가 빨리 끝날수록 배정할 수 있는 강의 수 커짐
N = int(input())
#c = [list(map(int, input().split())) for _ in range(N)]
#print(c)
#c.sort(key = lambda x : (x[1], x[0]))
#print(c)
c = []

for _ in range(N):
    s, e = list(map(int, input().split()))
    # end, start 기준으로 list 정렬
    heapq.heappush(c, (e,s))
#print(c)    

max_c = 0
end_t = 0

while c:
    ce, cs = heapq.heappop(c)
    # 넣을 강의의 start time과 마지막원소 end time 비교
    if cs >= end_t:
        max_c += 1
        end_t = ce

print(max_c)
