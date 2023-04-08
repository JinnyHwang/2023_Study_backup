
'''
회전시킬 톱니와 맞닿아있는 톱니의 극을 확인
극이 다르면 반대 방향으로 회전시키기
극이 같으면 냅두기

어떤 구조로 만드는게 가장 좋을까?
맞닿아있는 톱니에 영향을 주며
회전은 연쇄적으로 일어날 수 있다

K번 반복
1. 회전할 톱니 번호와 방향 모두 확인
2. 한 번에 회전시키기 (1: 시계, -1: 반시계)

12시를 index 0으로
각 톱니의 0번 index를 확인해서 점수 계산

N극: 0
S극: 1
'''

def print_wheel():
    for value in wheel:
        print(value)


wheel = [ input() for _ in range(4)]
print(wheel)
print_wheel()

'''
# 반시계
wheel[0] = wheel[0][1:]+wheel[0][0]
print('? ', wheel[0])

wheel[0] = wheel[0][1:]+wheel[0][0]
print('? ', wheel[0])

wheel[0] = wheel[0][1:]+wheel[0][0]
print('? ', wheel[0])


print(wheel[1][-1])

# 시계
wheel[1] = wheel[1][-1]+wheel[1][:-1]
print('! ', wheel[1])

wheel[1] = wheel[1][-1]+wheel[1][:-1]
print('! ', wheel[1])

wheel[1] = wheel[1][-1]+wheel[1][:-1]
print('! ', wheel[1])
'''

K = int(input())
act = []
for _ in  range(K):
    n,d = map(int, input().split())
    act.append((n-1,d)) # index번호로 사용하기 위해 -1
print(act)

# 톱니의 왼쪽은   index 6
# 톱니의 오른쪽은 index 2
for n, d in act:
    a = [0,0,0,0]
    # n번을 기준으로 톱니 전체적으로 탐색
    a[n] = d
    print('1? ',a)
    
    # 오른쪽먼저
    for i in range(n+1, 4):
        print('i-1:{}, i:{}, wheel[i-1]:{}, wheel[i]:{}'.format(i-1, i, wheel[i-1], wheel[i]))
        if wheel[i-1][2] != wheel[i][6]:
            print('??? ',wheel[i-1][2], wheel[i][6])
            a[i] = d*((-1)**(i-n))
        else: # 회전 안하는 바퀴 만나면 바로 break
            break
    print('2? ',a)

    # 왼쪽도 확인
    for i in range(n-1, -1, -1):
        print('i+1:{}, i:{}, wheel[i+1]:{}, wheel[i]:{}'.format(i+1, i, wheel[i+1], wheel[i]))
        if wheel[i+1][6] != wheel[i][2]:
            a[i] = d*((-1)**(n-i))
        else:
            break
    print('3? ',a)
    
    print(a)
    
    print('before?')
    print_wheel()
    # 회전 진행
    for ai, ad in enumerate(a):
        if ad == 1: #시계방향회전
            wheel[ai] = wheel[ai][-1]+wheel[ai][:-1]
        elif ad == -1:
            wheel[ai] = wheel[ai][1:]+wheel[ai][0]
    
    print('after?')
    print_wheel()
            
    
hap = 0
for wi, w in enumerate(wheel):
    hap += int(w[0])*(2**wi)

print(hap)








