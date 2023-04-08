
# 카펫 크기
# 완전탐색
# brown으로 만들 수 있는 사각형
# 주어진 brown - 4 (모서리)
# brown/2 -> 숫자를 만들 수 있는 조합 확인
# if brown 10
# (24-4)/2 = 10
# (1,9) (2,8) (3,7) (4,6) (5,5) (가로 길이가 더 길기 때문에)
# 이렇게 나오는 조합의 가*세 == yellow 타일 개수
# 가세 정할 수 있음

def solution(brown, yellow):
    answer = [0, 0]
    
    num = (brown-4)//2
    
    # 만들 수 있는 가로 세로 조합 구하기
    com = [ ((num-i), i) for i in range( 1, num//2+1 ) ]
    print(com)
    
    for c in com:
        if c[0]*c[1] == yellow:
            answer = [c[0]+2, c[1]+2]
            break
    
    return answer


def solution1(brown, yellow):
    
    for i in range(1, int(yellow**(1/2))+1 ):
        if yellow%i == 0:
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]
            

print(solution(24, 24))
print(solution(8, 1))















