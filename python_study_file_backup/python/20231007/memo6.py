
# 구슬을 한 칸씩 움직이면서 시뮬레이션하지 않음
# 모든 구슬 쌍에 대해 충돌이 일어나는지? 언제 일어나는지? 각각 구해서
# 먼저 충돌이 일어나는 구슬쌍부터 확인하는 방식으로 해결

# 1. 두 구슬의 이동 방향이 동일하면 충돌 일어날 수 없음
# 2. 이동 방향이 반대. x or y가 동일. 두 구슬의 거리를 반으로 나눈만큼 움직였을 때 같은 위치로 도달
# 3. 이동 방향이 ㄱ,ㄴ x,y좌표차이가 일치해야함

# 각 구슬쌍에 대해 전부 충돌시간을 구함

# 구슬 번호가 작은 순서면 n을 역순으로 돌리면 됨

'''
for n in range(N):
    x, y, w, d = tuple(input().split())
    x, y, w = int(x), int(y), int(w)
    marbles.append((x,y,w,mapper[d],n))
    
# 우선순위 정렬
marbles = sorted(marbles, key=lambda x : (x[2], x[4]), reverse = True)
'''












