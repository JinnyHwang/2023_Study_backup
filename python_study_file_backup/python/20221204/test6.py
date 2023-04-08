
# 강의가 끝나는 시간을 기준으로 sort:O(NlogN) + 강의 개수:O(N)
# 강의가 끝나는 시간을 기준으로 sort? 강의가 빨리 끝날수록 배정할 수 있는 강의 수 커짐
N = int(input())
c = [list(map(int, input().split())) for _ in range(N)]
#print(c)
c.sort(key = lambda x : (x[1], x[0]))
#print(c)

# 해당 강의를 선택했을 때 들을 수 있는 강의의 수 누적
max_c = 1
end_t = c[0][1]

for i in range(1,N):
    if c[i][0] >= end_t:
        end_t = c[i][1]
        max_c += 1
        #print(max_c, c[i])

print(max_c)

