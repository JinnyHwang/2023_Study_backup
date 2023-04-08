'''
공의 개수가 같은 구간을 구하는 방법

빨간색 공 : 1 / 초록색 공 : 2
-> 해당 값을 -1, 1로 치환

각 공의 누적값을 구한다 : 0번째 ~ i번째
누적 리스트에서 i번째 값은 i번째까지 어떤 공이 더 많았는지를 알 수 있다
즉, 누적 리스트에서 값이 동일한 index는 같은 색상의 공임을 의미하고
사이 구간을 구성하는 공은 빨간색, 초록색 공의 개수가 동일함을 의미한다.

+,- 진행해서 결국 같은 공의 정보를 나타내는 위치로 온것이니까!

값을 치환하고
누적 값을 구해서
원소 값이 동일한 구간의 최대 길이를 구하면
가장 길게 자른 장식 길이를 알 수 있다
'''
def solution1(bell): # 풀이 안보고 혼자 작성 한 code. 시간초과!
    #bell = [1, 2, 1, 1, 1, 2, 2, 1]
    #print(bell)
    bell = [ -1 if b == 1 else 1 for b in bell ]
    #print(bell)
    
    # bell이 하나도 없는 0번째부터 시작
    # 누적값을 구하는데 list 길이가 최대 10^6 굉장히 오래 걸린다
    bell_cal = [0]
    for b in bell:
        bell_cal.append(bell_cal[-1]+b)
    #print(bell_cal)
    
    bell_max = 0
    
    # 불필요한 탐색이 많음
    for i in range(len(bell)):
        for j in range(i+1,len(bell)+1):
            if bell_cal[i] == bell_cal[j]:
                #print('i:{} j:{} len:{} bell_max:{}'.format(i, j, j-i, bell_max))
                bell_max = max(bell_max, j-i)
    
    return bell_max


# 풀이 확인 후 작성
# 누적 결과를 반환하는 accumulate 사용
from itertools import accumulate

def solution(bell):
    
    # key값은 accumulate로 구한 누적 리스트의 원소
    # value값은 해당 원소의 index값
    deco_start = {} # 특정 누적값(key)이 등장하는 가장 앞 부분 index를 value로 저장
    deco_end = {} # 특정 누적값(key)이 나타나는 가장 마지막 부분 index를 value로 저장
    
    # 맨 앞에 원소 0을 포함. 해당 누적값 리스트를 가지고 바로 for문 진행
    # accumulate( [0] + [ -1 if b == 1 else 1 for b in bell ] )
    for bi, bv in enumerate( accumulate( [0] + [ -1 if b == 1 else 1 for b in bell ] ) ):
        # bv 값이 처음 등장. 즉 deco_start의 key값으로 존재하지 않는 경우
        if bv not in deco_start:
            deco_start[bv] = bi # 해당 key값이 등장하는 가장 앞부분 index를 value로 초기화
        deco_end[bv] = bi # 값이 등장할 때마다 value로 index 정보 저장. 최종적으로 가장 맨 끝 index 저장
    
    # 특정 x값(deco_end가 있는 key값)에서 deco_end[x] - deco_start[x] 값이 가장 큰 것을 retrun
    # max() 쓸 때는 항상 2개 인자값 비교만 했었는데.. 좀 더 다양한 활용법이 있구만
    return max( deco_end[key] - deco_start[key] for key in deco_end )

