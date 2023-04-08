
# 1. 징검다리를 점점 높게
# 2. 징검다리를 점점 낮게
# 위 두 가지 경우를 구하고 조합?
# 어느 순간부터 낮은 칸으로 가는가?
# 맨 처음보다 높은거 , 맨 마지막보다 높은거: 가장 높은 돌?
# 어떤 돌에서 전환하는가?
import sys

#N = int(input())
N = int(sys.stdin.readline())

#rock_l = [ 0 for _ in range(N) ]
#rock_l = list(map(int, input().split()))
rock_l = list(map(int, sys.stdin.readline().split()))
cnt_rock = [ 1 for _ in range(N) ]


# 가장 고점의 index는 max_hi. 가장 고점까지 가는 경우의 수?
for i1 in range(1,N):
    for i2 in range(i1):
        if (rock_l[i2] < rock_l[i1]) and (cnt_rock[i1] < cnt_rock[i2]+1):
            cnt_rock[i1] = cnt_rock[i2]+1
       

# cnt_rock[max_hi]에는 갈 수 있는 경우의 수 저장
for i1 in range(1,N):
    for i2 in range(i1):
        if (rock_l[i2] > rock_l[i1]) and (cnt_rock[i1] < cnt_rock[i2]+1):
            cnt_rock[i1] = cnt_rock[i2]+1
            
print(max(cnt_rock))
            
