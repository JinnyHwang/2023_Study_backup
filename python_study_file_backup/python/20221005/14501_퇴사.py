
# 퇴사까지 남은 일 수
N = int(input())
print(N)

# 근무표
schedule = [ list(map(int, input().split())) for _ in range(N) ]
#print(schedule)

# schedule[i][0] : 걸리는 일 수
# schedule[i][1] : 보수

arr = set()

# 상담을 잡을 수 있는 모든 경우의 수 탐색
def cal_pay(day, pay):
    
    # 퇴사일을 넘기는가?
    if day >= N:
        arr.add(pay)
        return
    
    # 현재 날짜의 일을 받을 수 있는가? 퇴사일 안에 받을 수 있는 일인지 확인
    if day + schedule[day][0] - 1 <= N-1:
        cal_pay(day + schedule[day][0], pay+schedule[day][1])

    cal_pay(day+1, pay)
    
    
#print('??', arr)
cal_pay(0, 0)
#print('!!', arr)

print(max(arr))


