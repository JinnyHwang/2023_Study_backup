
# 가장 낮은 컴퓨터
# 기준치 맞출 때 드는 비용
# 기준치보다 낮은 컴퓨터들
# (기준-성능)^2의 합이 비용을 넘지 않을 때 까지

'''
작은수에서 하나하나 늘려가는 방식이 아니라
성능값을 하나하나 찾아가는 방식
구해야하는 성능은 이진트리 방식으로 탐색
결국 그 성능이 답이기 때문

컴퓨터 정보는?
컴퓨터의 성능을 key값
컴퓨터 개수를 value값
dictionary 방식으로 저장
'''
import sys

N, B = map(int, sys.stdin.readline().split())
com_list = list(map(int, input().split()))
com_dic = {}

# 내림차순
com_list.sort(reverse=True)

# 성능 초기 탐색 값
left = com_list[-1] #가장 작은 성능 값
#컴퓨터가 가질 수 있는 가장 큰 성능값 + 비용으로 만들 수 있는 가장 큰 성능 값
right = 2*(10**9)

for ci in com_list:
    if ci not in com_dic.keys():
        com_dic[ci] = 1
    else:
        com_dic[ci] += 1


# 이진 탐색 : right가 큰 값일 때만 반복
# 즉 마지막에 mid로 초기화된 left가 최대 효율 값
while (right - left > 1):
    mid = (right+left)//2 # 중간값
    cost = 0
    flag = 1
    for k, v in com_dic.items():
        if k < mid:
            cost += v*((mid-k)**2)
            if cost > B: # 비용 부족
                right = mid # 기준값 바꿔서 다음 이진 트리 탐색
                flag = 0
                break
    # 비용이 남음
    if flag:
        left = mid

print(left)

