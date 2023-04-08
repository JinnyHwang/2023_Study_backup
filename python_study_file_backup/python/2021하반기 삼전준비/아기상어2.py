
# 완전 잘못하고 있었다
# 아이구야!


# !!!! 중요 !!!!
# 원본을 변경하고 싶지 않을 때 튜플사용
# 불변형 데이터를 매개변수로 사용
# 함수의 매개변수로써 리스트가 쓰이면
# 참조 주소가 넘어가기 때문에 원본에도 영향을 끼침
# 불변형인 튜플이 쓰이면 값 그 자체를 넘기게 된다


# 배열 좌표
# list1 = [
#  [1, 2, 3, 4],
#  [5, 6, 7, 8]
# ]
# 원소 4의 위치는? list[0][3]
# y, x 값으로 좌표 만들어야 함!!!

def near_eat(can_eat, shark):
    
    can_eat_pos = [ list(e) for e in can_eat ]
    
    distance = []
    for ce in can_eat_pos:
        ce[0] -= shark[0]
        ce[1] -= shark[1]
        distance.append( abs(ce[0])+abs(ce[1]) )
    #print("can_eat_pos:",can_eat_pos)
    mindis = min(distance)
    minpos = []
    for i, dis in enumerate(distance):
        if dis == mindis:
            minpos.append(i)
    #print(minpos)
    # 거리가 가장 짧은 물고기 한마리, 위치값 바로 return
    if len(minpos) == 1:
        return minpos[0]
    # 여러마리 물고기
    else:
        # minpos 위치 물고기의 좌표값 비교
        minfish = minpos[0]
        for mp in minpos[1:]:
            # y값 비교
            if can_eat_pos[mp][0] == can_eat_pos[minfish][0]:
                # x값 비교
                if can_eat_pos[mp][1] < can_eat_pos[minfish][1]:
                    minfish = mp
            elif can_eat_pos[mp][0] < can_eat_pos[minfish][0]:
                minfish = mp
        return minfish

# shark[1]은 [0~n, 0~n] 범위 내 값을 가져야함
# 아기상어의 목표지점 구하기
# 먹으러 가야할 물고기 x,y 좌표를 return
def destination(space, shark):
    
    # 먹을 수 있는 물고기 좌표
    # 원형 유지를 위해 튜플로 저장
    can_eat = []
    
    for y, s1 in enumerate(space):
        for x, s2 in enumerate(s1):
            # 상어보다 크기가 작은 물고기 좌표 저장
            if s2 != 0 and s2 < shark[0]:
                can_eat.append((y,x))
                
    # 먹을 수 있는 물고기가 없음
    if len(can_eat) == 0:
        #print("1:[-1,-1]")
        return [-1,-1]
    # 먹을 수 있는 물고기 1마리, 좌표 바로 return
    elif len(can_eat) == 1:
        #print("2:",list(can_eat[0]))
        return list(can_eat[0])
    # 여러마리 있을 경우 그 중 가장 가까운 물고기 return
    else:
        # 먹을 수 있는 물고기 좌표, 상어 위치 매개변수
        # 몇번째 물고기를 먹어야 하는지 확인
        #print("can_eat:", can_eat)
        fishnum = near_eat(can_eat, shark[1])
        #print("3:",list(can_eat[fishnum]))
        return list(can_eat[fishnum])
        
def big_fish1(space, shark, des_y, des_x):
    sy = shark[1][0]
    sx = shark[1][1]
    
    dy = des_y
    dx = des_x
    
    # sy고정 -> dx고정 탐색
    for x in range(sx, dx+1):
        if space[sy][x] > shark[0]:
            break
    else:
        for y in range(sy, dy+1):
            if space[y][dx] > shark[0]:
                break
        else:
            print("1")
            return abs(dy-sy)+abs(dx-sx)
        
    
    # sx고정 -> dy고정 탐색
    for y in range(sy, dy+1):
        if space[y][sx] > shark[0]:
            break
    else:
        for x in range(sx, dx+1):
            if space[dy][x] > shark[0]:
                break
        else:
            print("2")
            return abs(dy-sy)+abs(dx-sx)
    
    # 갈 수 있는 최단거리 구하기
    print("3")
    return abs(dy-sy)+abs(dx-sx)


def big_fish(space, shark, des_y, des_x):
    sy = shark[1][0]
    sx = shark[1][1]
    
    dy = des_y
    dx = des_x
    
    for y in range(sy, dy+1):
        for x in range(sx, dx+1):
            print("space[{}][{}]:{} vs shark_size:{}".format(y, x, space[y][x], shark[0]))
            if space[y][x] > shark[0]:
                print("???????")
                break
    else:
        print("big1")
        return abs(dy-sy)+abs(dx-sx)
    
    # 갈 수 있는 최단거리 구하기
    print("big3")
    return abs(dy-sy)+abs(dx-sx)
    
def main():
    n = int(input())
    space = []
    # size, postion[y, x]
    shark = [2]
    
    for i in range(n):
        space.append(list(map(int, input().split())))
        if 9 in space[i]:
            for j, s in enumerate(space[i]):
                if s == 9:
                    # 좌표 y, x 입력
                    shark.append([i, j])
                    space[i][j] = 0
                    
    #print("입력 space:", space)
    #print("입력 shark:", shark)
    fish_cnt = 0
    time = 0
    while True:
        print("time:",time,"space:",space, "shark:",shark)
        
        eat_y, eat_x = destination(space, shark)
        print("eat_y:{}, eat_x:{}".format(eat_y, eat_x))
        
        if [eat_y, eat_x] == [-1, -1]:
            break
        
        # 가는길에 큰 물고기가 있는지 탐색
        # ( abs(eat_y-shark[1][0])+abs(eat_x-shark[1][1]) )
        time += big_fish(space, shark, eat_y, eat_x)
        
        shark[1] = [eat_y, eat_x]
        space[eat_y][eat_x] = 0
        fish_cnt += 1
        
        if shark[0] == fish_cnt:
            shark[0] += 1
            fish_cnt = 0
            
    
    return time
    
print(main())

'''
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
'''
    




