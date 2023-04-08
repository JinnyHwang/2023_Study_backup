
# 그리디 알고리즘 가장 대표적 예시 : 거스름돈
# 1이 될 때까지 연산

#p.102
def AAA() :
    n, k = map(int, input().split())
    result = 0

    while True :

        # (n == k로 나누어 떨어지는 수)가 될 때까지 -1씩 빼기
        target = (n // k)*k
        
        # 나누어 떨어지지 않을 때 -1 해야하는 횟수
        result += (n - target)

        # 몫
        n = target

        # 더이상 나눌 수 없을 때
        if n < k :
            break

        # 나눈 횟수 count
        result += 1
        n //= k

    result += (n-1)
    print(result)


# p.311

# 모험가 길드
def q1() :
    n = int(input())
    group = list(map(int, input().split()))

    group_sort = sorted(group)

    result = 0 # 총 그룹 수
    count = 0 # 현재 그룹에 포함된 모험가의 수

    for i in group_sort : # 공포도가 낮은 것부터 확인
        count += 1 # 현재 그룹에 모험가 포함
        if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 그룹 결성
            result += 1 # 총 그룹 수 증가
            count = 0 # 다음 그룹 count를 위해 현재 그룹 멤버수 초기화

    print(result)
    
#q1()


def q2() :
    data = input()

    data_int = []
    
    for i in range(len(data)) :
        data_int.append( int(data[i]) )    

    result = 0
    for j in data_int :
        if result == 0 or j == 0:
            result += j
        else :
            result *= j

    print(result)


def q3() :
    data = input()

    count_1 = 0
    count_0 = 0
    
    for i in range(len(data)) :
        if int(data[i]) == 1 and int(data[i-1]) != 1 :
            count_1 += 1
        elif int(data[i]) == 0 and int(data[i-1]) != 0 :
            count_0 += 1


    if count_0 < count_1 :
        print(count_0)
    else :
        print(count_1)

def q4() :
    n = int(input())

    coin = []
    coin = list(map(int, input().split()))

    coin.sort()

    result = 1

    # 작은 수 부터 차례로 sum.
    # 이전 coin 합으로 만들 수 없는 수.
    # 다음 coin 단위가 만들 수 없는 수 보다 크다면 절대 만들 수 없다
    # 이전 coin 합으로 만들 수 있는 수보다 작은 수는 언제든 만드는것이 가능
    for i in coin :
        if result < i :
            break
        result += i

    print(result)


def q5 () :

    n, m = map(int, input().split())
    
    ball = []
    ball = list(map(int, input().split()))

    count = 0
    
    for i in range(n-1) :
        for j in range(i+1, n) :
            if ball[i] != ball[j] :
                count += 1

    print(count)


def q5_1() :
    
    n, m = map(int, input().split())
    ball = list(map(int, input().split()))

    # 1부터 10까지의 무게를 담을 수 있는 리스트
    weight = [0]*11

    # 각 무게에 해당하는 볼링공 개수 count
    for x in ball :
        weight[x] += 1

    result = 0

    # 1부터 m까지의 각 무게 처리
    for i in range(m+1) :
        n -= weight[i] # 현재 탐색하는 무게의 공 개수는 제외
        result += weight[i]*n # 현재 탐색하는 무게의 공 개수 * 탐색하지 않은 공 개수

    print(result)


def start_food_fail (food_times, k) :

    food_count = len(food_times)

    i = 0
    time = 0
    
    while True :

        if sum(food_times) == 0 :
            i = -1
            break

        i %= food_count
        print('index: ',i, '. food_count : ', food_count, 'time : ', time)

        if food_times[i] != 0 :
            food_times[i] -= 1
            time += 1

        if time == k :
            break
        else :
            i += 1

    return i + 1


# 우선 순위 큐 활용
# 먹는데 적게 걸리는 음식 부터
# 
def start_food (food_times, k) :

    import heapq

    if sum(food_times) < k :
        return -1

    q = []
    
    for i in range(len(food_times)) :
        heapq.heappush(q, (food_times[i], i+1))    

    total_time = 0 # 먹는데 소요되는 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수

    # total_time + (현재 음식 시간 - 직전 음식 시간)*현재 음식 개수
    # 미리 시간 내에 먹을 수 있는 음식인지 확인
    while total_time + ((q[0][0] - previous)*length) <= k :
        # 시간 내 먹을 수 있는 음식이라면 계산
        now = heapq.heappop(q)[0] # 현재 음식 시간
        total_time += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key= lambda x : x[1])
    return result[ (k - total_time)%length ][1]
    
    
def q6 ():

#    food_times = [3, 1, 2]
#    food_times = [0, 0, 0]
    food_times = [1, 1, 9]
    k = 5

    print(start_food(food_times, k))


def q7 () :

    data = input()

   # left_sum = 0
   # right_sum = 0
    summary = 0
    for i in range(len(data)//2) :
    #    left_sum += int(data[i])
        summary += int(data[i])

    for j in range((len(data)//2), len(data)) :
     #   right_sum += int(data[j])
         summary -= int(data[j])

    #if left_sum == right_sum :
    if summary == 0 :
        print("True")
    else :
        print("False")


def q8_old() :
    data = input()
    #print(data.sort())

    sort_data = []
    for i in range(len(data)) :
        sort_data.append(int(data[i]))

    sort_data.sort()

    for j in sort_data :
        print(str(j), end='')


def q8() :
    data = input()
    result = []
    value = 0

    for i in data :
        if i.isalpha() :
            result.append(i)
        else :
            value += int(i)

    result.sort()

    if value != 0 :
        result.append(str(value))

    # 리스트를 문자열로 변환
    print(''.join(result))
    # ''.join(result)
#q8()

def q9_solution(s) :
    answer = len(s)

    # 1개 step부터 압축 단위를 최대 len(s)/2 까지
    for step in range(1, len(s)//2 +1) :

        # step에서 나올 문자열
        compressed = ""
        
        # step 크기 만큼 문자열 추출
        prev = s[0:step]
        
        count = 1
        
        # 다음 문자열 다음 인덱스부터 step 크기만큼 탐색
        for j in range(step, len(s), step) :
            if prev == s[j:j+step] :
                count += 1
            # 다른 문자열이면 재탐색
            else :
                # ?? 어케 동작하는거지
                # 앞쪽에 쓰고 뒤에 조건문. 조건문 안 맞으면 else문에 있는거로 write
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1

        # 반복문 완료 후 남은 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(compressed))

    return answer
            
        

def q9() :
    data = input()
    print(q9_solution(data))
    
#q9()

# 이차원 리스트 90도 회전
def rotate_a_matrix_by_90_dgree(a) :
    n = len(a) # 행
    m = len(a[0]) #열

    # 90도 뒤집으면 행렬이 바뀌니까
    result = [ [0]*n for _ in range(m) ]

    for i in range(n) : # 행
        for j in range(m) : #열
            result[j][n - i - 1] = a[i][j]

    return result

# 자물쇠 중간 부분이 모두 1인지 확인
# 자물쇠의 가로세로 3배크기 되는 배열에서 확인하기 때문에 중간 위치는 /3
def check(new_lock) :
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length*2) :
        for j in range(lock_length, lock_length*2) :
            if new_lock[i][j] != 1 :
                return False
    return True

def q10_solution(key, lock) :
    n = len(lock)
    m = len(key)
    
    # 자물쇠 크기 3배로 변환
    new_lock = [ [0]*(n*3) for _ in range(n*3) ]

    for i in range(n) :
        for j in range(n) :
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해 확인
    for rotation in range(4) :
        key = rotate_a_matrix_by_90_dgree(key) #열쇠 회전

        # 열쇠를 위치시킬 수 있는 시작점 범위
        for x in range(n*2) :
            for y in range(n*2) :

                # 열쇠 값 new_lock에 플러스
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True :
                    return True

                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] -= key[i][j]

    return False
        

def q10():
    key = [ [0, 0, 0], [1, 0, 0], [0, 1, 1] ]
    lock = [  [1, 1, 1], [1, 1, 0], [1, 0, 1] ]
    
    print(q10_solution(key, lock))



# 방향을 틀었을 때 dx, dy에 접근해야하는 
def turn(direction, c) :

    if c == 'L' :
        direction = (direction - 1) % 4
    elif c == 'D' :
        direction = (direction + 1) % 4
    else :
        return 1000
    return direction


def q11() :
    n = int(input())
    apple = int(input())

    data = [ [0]*(n+1) for _ in range(n+1) ]
    info = [] # 방향 회전 정보

    for _ in range(apple) :
        a, b = map(int, input().split())
        data[a][b] = 1 # 사과가 있는 위치

    count = int(input())

    for _ in range(count) :
        time, direct = input().split()
        info.append((int(time), direct))

    print('입력끝')
    print(data)
    print(info)

    # x : 행 / y : 열
    # 인덱스 - L : -1방향 / D : 1방향
    dx = [0, 1, 0, -1 ]
    dy = [1, 0, -1, 0 ]

    x, y = 1, 1 # 뱀 시작 위치
    data[x][y] = 2 # 뱀이 위치하는 곳은 2로 표시
    direction = 0 # 처음에는 동쪽을 봄
    time = 0 # 게임을 시작한 시간
    index = 0 # 다음에 회전할 정보 -> info 접근 index

    q = [] # 뱀이 차지하고 있는 위치 정보
    # deque 사용하지 않고, pop(0)으로 queue처럼 사용

    while True :
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 뱀이 맵 범위 안에 있고, 뱀의 몸통이 없는 위치인지 판별
        if (1 <= nx and nx <= n) and (1 <= ny and ny <= n) and (data[nx][ny] != 2) :

            # 사과가 없는 경우 이동 후 꼬리 제거
            if data[nx][ny] == 0 :
                data[nx][ny] = 2
                q.append((nx, ny))
                qx, qy = q.pop(0)
                data[qx][qy] = 0

            # 사과가 있는 경우 꼬리 그대로 전진
            elif data[nx][ny] == 1 :
                data[nx][ny] = 2
                q.append((nx, ny))

        else : # 뱀이 벽이나 몸통에 부딪힌 경우 다음 time 값 표현을 위해 +1 후 반복문 break
            time += 1
            break
,
        x, y = nx, ny # 다음 위치로 이동
''        time += 1

        if index < count and info[index][0] == time :
            direction = turn(direction, info[index][1])
            index += 1

    print(time)
                
q11()





















