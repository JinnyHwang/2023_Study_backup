
def map_print(m):
    for mm in m:
        print(mm)
    print()

'''
https://www.youtube.com/watch?v=pFAsz4NIikk&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=8
0행렬
M*N 행렬의 한 원소가 0일경우s
해당 원소가 속한 행과 열의 모든 원소를 0으로 설정

행렬문제는 모든 원소를 순회한다
1. 전체 스캔, 0값 좌표 기록
2. 0으로 변환

'''
test_m1 = [[1,1,1],[1,0,1],[1,1,1]]
test_m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def zeroMatrix(m):
    # 순서 상관없음 set() 사용!
    rowSet = set()
    colSet = set()
    
    # 전체스캔, 0값 좌표 기록
    for r in range(len(m)):
        for c in range(len(m[0])):
            if not m[r][c]:
                rowSet.add(r)
                colSet.add(c)
    
    print(rowSet)
    print(colSet)
    
    # 0으로 변환
    for r in range(len(m)):
        for c in range(len(m[0])):
            # set()에 해당 원소가 존재하는지 확인
            if r in rowSet or c in colSet:
                m[r][c] = 0
            
    return m
'''
map_print(zeroMatrix(test_m1))
map_print(zeroMatrix(test_m2))
'''

'''
https://www.youtube.com/watch?v=Wm7DfRN34mI&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=9
문자열 회전

1. 한글자 한글자 하나씩 비교...
s1의 각 글자 순회,
매 회 맨 앞글자를 우측으로 보내서(회전) 새로운 문자로 변환
변환된 문자열이 s2와 같은지 체크

2. 문자열의 구간을 만들기
s1 = abcde  / s2 = deabc
x:abc / y:de
s1 == xy  /  s2 == yx
x'yx'y
yx는 xyxy의 부분 문자열

즉, s1(xyxy)을 두 개 이어붙인다
s2(yx)가 xyxy의 부분 문자열인지 확인!
'''
def isSubstring(s1, s2):
    i = 0
    while i < len(s1):
        s1 = s1[1:] + s1[0]
        if s1 == s2:
            return True
        i += 1
        
    return False


def isSubstring2(s1,s2):
    '''
    if s2 in s1+s1:
        return True
    return False
    '''
    # .find()는 없을 경우 -1 return
    # .index()는 없을 경우 errir return
    if (s1+s1).find(s2) == -1:
        return False
    
    return True
    
    

def strRotation(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    #return isSubstring(s1,s2)
    return isSubstring2(s1,s2)
'''
print(strRotation("waterbottle","erbottlewat"))
print(strRotation("abcde","cdeab"))
print(strRotation("abcde","abced"))
print(strRotation("moon","moon"))
'''


# 연결리스
'''
https://www.youtube.com/watch?v=AkLhT1FOJNQ&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=10
중복없애기(Remove Dups)

배열로 풀 때와 차이점은?
연결리스트 자료 구조 특성에 맞춰 연결, 삭제와 같은  후 처리를 고려!

비정렬 연결리스트에서 중복문자열을 제거하는 코드
임시버퍼가 허용되지 않는다면?
input: 1 -> 1 -> 2 -> 2 -> 3
output: 1 -> 2 -> 3

연결리스트 특성 상
head -> tail로 갈 때 포인터 필요

한 번에 2개 node를 검사하기 위해 2개 포인터 필요

근데 파이썬은 리스트 type이 원래 연결리스트 구조이기 때문에 나중에 공
'''

'''
행렬회전

1. 전치행렬
2. reverse
과정으로 구할 수 있다

1. 전치행렬은?
주 대각선을 기준으로 뒤집어서 얻을 수 있다


'''
N, M = 4, 5
matrix = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    for m in range(M):
        matrix[n][m] = n*M + m + 1
map_print(matrix)

# 왼쪽위-> 오른쪽아래 대각선을 기준으로 전치행렬 구하기
matrix2 = [[0 for _ in range(N)] for _ in range(M)]
'''
# 시계방향
for n in range(N):
    for m in range(M):
        matrix2[m][n] = matrix[n][m]
'''

# 반시계방향
for n in range(N):
    for m in range(M):
        matrix2[M-m-1][N-n-1] = matrix[n][m]
map_print(matrix2)

for i, m in enumerate(matrix2):
    matrix2[i] = m[-1::-1]
map_print(matrix2)    











