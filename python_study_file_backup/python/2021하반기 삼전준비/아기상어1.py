
# pass by assignment
# 여기서 eat_fish 값을 변경하면 새로운 메모리에
# call한 function에서 해당 func에서 만들어진 메모리 주소값으로
# 기존 변수를 덮어쓰기 하지 않는 한
# 매개변수로 준 eat_fish는 원형이 기존 메모리에 살아있음
    
# 먹을 수 있는 물고기들의 좌표 리스트, 아기상어 좌표
# 깊은 복사를 사용해서 원본 리스트를 해치지 않도록
def search_fish(eat_fish, shark_pos):
    eat_fish_cp = [ e for e in eat_fish ]
    print(id(eat_fish_cp), id(eat_fish))
    distance = []
    for ef in eat_fish_cp:
        ef[0] -= shark_pos[0]
        ef[1] -= shark_pos[1]
        distance.append(abs(ef[0]) + abs(ef[1]))
        
    #print("distance:",distance)
    
    # 1. x좌표 절댓값 + y좌표 절대값 작은 것
    # 2. y값이 가장 작은 것 우선
    # 3. x값이 가장 작은 것 우선
    mindis = min(distance)
    minpos = []
    for i, d in enumerate(distance):
        if d == mindis:
            minpos.append(i)
            
    #print("minpos:", minpos)
    
    
    if len(minpos) == 1:
        return eat_fish[minpos[0]]
    else:
        nearnum = minpos[0]
        nearpos = eat_fish[minpos[0]]
        #print("nearpos:",nearpos)
        for mp in minpos[1:]:
            #print("mp:",mp)
            # y좌표 비교
            if nearpos[1] == eat_fish[mp][1]:
                #print("1")
                # x좌표 비교
                if nearpos[0] > eat_fish[mp][0]:
                    #print("2")
                    nearpos = eat_fish[mp]
                    nearnum = mp
            elif nearpos[1] > eat_fish[mp][1]:
                #print("3")
                nearpos = eat_fish[mp]
                nearnum = mp
        # y, x 좌표를 봤을 때 가장 가까운 물고기의 position 값 return
        return nearnum
    
# shark[1]은 [0~n, 0~n] 범위 내 값을 가져야함
# 아기상어의 목표지점 구하기
# 먹으러 가야할 물고기 x,y 좌표를 return
def destination(space, shark):
    
    eat_fish = []
    
    # 배열을 모두 확인하여 지금 상어 크기보다 작은 물고기가 있는 지점 확인
    for i, s1 in enumerate(space):
        for j, s2 in enumerate(s1):
            # 0값이 아니고, 상어 크기보다 작은 물고기는 eat_fish에 append
            if s2 != 0 and shark[0] > s2:
                eat_fish.append((i,j))
                
    #print(eat_fish)
    
    # 현재 상어보다 작은 물고기가 없을 때 return -1, -1 없는 좌표
    # 엄마 물고기 호출 신호
    if len(eat_fish) == 0:
        return [-1, -1]
    
    # 먹으러 갈 물고기가 1마리 일 때
    elif len(eat_fish) == 1:
        return eat_fish[0]
    
    else:
        # 먹을 수 있는 물고기 여러마리일 때
        # 몇번째 물고기가 가장 가까이에 있는지 return
        #print("??")
        eat_fish_cp = [ list(e) for e in eat_fish ]
        
        print("eat_fish:{}  id(eat_fish):{}".format(eat_fish, id(eat_fish_cp)))
        fish = search_fish(eat_fish_cp, shark[1])
        #print("fish:", fish)
        print("fish:{}, eat_fish_cp:{}, eat_fish:{}, eat_fish[fish]:{}, id(eat_fish):{}".format(fish, eat_fish_cp, eat_fish, eat_fish[fish],id(eat_fish_cp)))
        return list(eat_fish[fish])

def main():
    # 첫째 줄 공간 크기 N (2~20)
    # 물고기 있는 공간
    # 9 : 아기상어 위치

    # 공간 크기
    n = int(input())
    space = []
    # 크기, [x좌표, y좌표]
    shark = [2]

    # 아기상어 위치 확인, 9 없애기
    for i in range(n):
        space.append( list(map(int, input().split())) )
        if 9 in space[i]:
            for j, s in enumerate(space[i]):
                if s == 9:
                    shark.append([i, j])
                    space[i][j] = 0
            
    print("space\n{} \nshark:{}".format(space, shark))
    
    fish_count = 0
    time = 0
    
    while True:
        print("space:",space, "shark:",shark)
        
        # 먹으러갈 물고기 좌표
        eat_fish_x,eat_fish_y  = destination(space, shark)
        print("eat_fish_x:{}, eat_fish_y:{}".format(eat_fish_x, eat_fish_y))
        if [eat_fish_x,eat_fish_y] == [-1, -1]:
            break
        
        #eat_size = space[eat_fish_x][eat_fish_y]
        space[eat_fish_x][eat_fish_y] = 0
        # 먹으러가는 거리 == 걸리는 시간
        time += (abs(shark[1][0]-eat_fish_x) + abs(shark[1][1]-eat_fish_y))
        shark[1][0] = eat_fish_x
        shark[1][1] = eat_fish_y
        fish_count += 1
        
        if shark[0] == fish_count:
            shark[0] += 1
            fish_count = 0
            
    return time

main()
