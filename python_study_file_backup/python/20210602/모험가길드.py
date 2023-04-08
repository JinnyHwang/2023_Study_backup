
# 공포도 측정
# 공포도가 X인 모험가는 X명 이상으로 길드 구성
# 여행을 떠날 수 있는 그룹수의 최댓값?
# 최소한의 모험가 수

n = input()
group = list( map(int, input().split()) )
#group_s = sorted(group)
group.sort()

#print(group_s)
#print(group)

result = 0  # 총 그룹수
count  = 0  # 그룹에 포함된 모험가 수

for i in group :
    count += 1 # 현재 그룹에 포함될 사람 수
    if count >= i :
        result += 1
        count = 0

print(result)










