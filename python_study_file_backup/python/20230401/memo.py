
# 배열과 문자열
'''
https://www.youtube.com/watch?v=lsgokbcbWpE&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=1
중복이 없는가
'''
def isUnique(str):
    for i in ragne(len(str)):
        for j in range(i, len(str)):
            if str[i] == str[j]:
                return False
    return True

# hash map 사용
def isUniqye2(str):
    dic = {}
    
    for s in str:
        if s in dic:
            return False
        dic[s] = 1
        
    return True
#print(isUniqye2('abcd'))
#print(isUniqye2('abcda'))


'''
https://www.youtube.com/watch?v=noYGgJNCWvQ&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=2
순열확인
문자열 두 개가 주어졌을 때, 서로 순열관계에 있는지 확인
1. 길이가 같아야함
2. 구성하는 문자의 종류, 개수가 같아야함

문자열 정렬해서 두 문자열이 동일한지 확인
'''
def checkPermutation(a, b):
    
    if len(a) != len(b):
        return False
    
    if sorted(a) != sorted(b):
        return False
    
    return True

# hash map사용
# 문자열 출연 빈도를 저장
def checkPermutation2(a, b):
    dic = {}
    for aa in a:
        dic[aa] = dic.get(aa, 0) + 1
    #print(dic)
    
    for bb in b:
        if bb not in dic:
            return False
        if dic[bb] <= 0:
            return False
        dic[bb] -= 1
    #print(dic)
    '''
    for k, v in dic.items():
        if v != 0:
            return False
    print(dic)
    ''' 
    return True
'''
print(checkPermutation2('c', 'aac'))
print(checkPermutation2('hooh', 'oohh'))
print(checkPermutation2('aba', 'bba'))
print(checkPermutation2('aaabbbccc', 'abcabcabc'))
print(checkPermutation2('abaa', 'abba'))
'''

'''
https://www.youtube.com/watch?v=xm9Fuwn5Fyc&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=3
URL화
문자열 내 모든 공백을 %20으로 바꾸는 메서드 작성
문자열 끝에 추가로 필요한 문자들을 더할 수 있는 충분한 공간이 있다 가정
공백을 포함하는 문자열의 길이도 함께 주어짐
'''
def urlify(a):
    # 앞뒤 공백 제거. strip()
    #print(f'|{a}|')
    a = a.strip()
    #print(f'|{a}|')
    
    # 공백으로 split(), '%20'으로 join
    a = '%20'.join(a.split())
    #print(a)
    '''
    al = a.split()
    print(al)
    
    a = '%20'.join(al)
    print(a)
    '''
    return a
'''
# 내장함수 사용 안하고!
def urlify2(a, n):
    # 공백개수 구하기
    whitespace= len(a) - n
    
    # 문자열 앞에 있는 공백 개수
    
    # 문자열 뒤에 있는 공백 개수
    
    # 문자열 앞 공백 제거
    # 문자열 사이 공백 -> %20로 바꿔주기
    # 문자열 뒤 공백 제거
'''    
#print(urlify("Mr John    Smith    ")) # "Mr%20John%20Smith"
#print(urlify("  Coding  Moon    ")) # "Coding%20Moon"


'''
https://www.youtube.com/watch?v=OOIMJxwWdGM&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=4
회문 순열이 가능한지?
회문: 앞으로 읽으나, 뒤로 읽으나 같은 단어 or 구절
순열: 문자열을 재배치하는 것
(대소문자, 빈글자 무시)
'''
#hash map으로 해결 가능
def checkPalinPerm(a):
    dic = {}
    #print(a)
    a = a.lower()
    #print(a)
    for aa in a:
        if aa != ' ':
            dic[aa] = dic.get(aa, 0) + 1
    
    #print(dic)
    # 글자 구성 개수
    # 모두 짝수 or 1개만 홀수
    num = len(list( k for k in dic if dic[k]%2 != 0))
    #print(num)
    
    if num == 0 or num == 1:
        return True
    
    return False
'''
print(checkPalinPerm("Tact Coa"))
print(checkPalinPerm("Tact Boa"))
print(checkPalinPerm("aabbc"))
print(checkPalinPerm("aabc"))
'''

'''
https://www.youtube.com/watch?v=dcNv2V8k4RY&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=5
하나빼기
문자열을 편집: 문자삽입, 문자삭제, 문자교체
문자열 2개가 주어졌을 때 문자열을 같에 만들기 위한 편집횟수가 1회 이내인지 확인
'''
def checkEditReplace(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
        if cnt > 1:
            return False
    return True

def checkEditInsertORDelete(a,b): #b의 len이 더 길다
    ai = 0
    bi = 0
    while(ai < len(a) and bi < len(b)):
        if a[ai] != b[bi]:
            if ai != bi:
                # 앞에서 편집이 이미 이뤄졌다
                return False
            else:
                bi += 1
        else:
            ai += 1
            bi += 1
    return True

def oneAway(a, b):
    la = len(a)
    lb = len(b)
    # 교체: 두 문자열 길이가 같은 경우
    if la == lb:
        return checkEditReplace(a,b)
    
    # 삽입, 삭제: 두 문자열 길이 차이 1
    elif lb - la == 1: #삽입
        return checkEditInsertORDelete(a, b)
        
    elif la - lb == 1: #삭제
        return checkEditInsertORDelete(b, a)
    
    else:
        return False
    
    return True
'''
print(oneAway('apple','aple'))
print(oneAway('aple','apple'))
print(oneAway('more','core'))
print(oneAway('abc','ade'))
'''


'''
https://www.youtube.com/watch?v=5rNk9fZby_0&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=6
문자열 압축
압축된 문자열 길이가 기존 문자열 길이보다 길면 기존 문자열 반환
문자열은 알파벳으로만 구성됨
'''
def stringCompression(a):
    
    now_str = a[0]
    now_cnt = 0
    ca = a[0]
    for aa in a:
        if aa == now_str:
            now_cnt += 1
        else:
            ca += str(now_cnt)
            ca += aa
            now_cnt = 1
            now_str = aa
    ca += str(now_cnt)
    
    if len(ca) >= len(a):
        return a
    else:
        return ca
'''
print(stringCompression('aabcccccaaa'))
print(stringCompression('aa'))
print(stringCompression('aaaAAaa'))
print(stringCompression('aacbba'))
'''

'''
https://www.youtube.com/watch?v=SZzYrBv0aRU&list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM&index=7
행렬회전
1. transfer(전치행렬)
2. reverse
'''

def map_print(m):
    for mm in m:
        print(mm)
    print()

N = 4
matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        matrix[i][j] = i*N + j + 1

#map_print(matrix)
'''
# 시계방향 90도 돌리기
# transfer
for i in range(N):
    for j in range(N):
        if j < i:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        else:
            break
#map_print(matrix)
'''
# 반시계방향 90도 돌리기
for i in range(N):
    for j in range(N):
        if j+i < N-1:
            matrix[i][j], matrix[N-j-1][N-i-1] = matrix[N-j-1][N-i-1], matrix[i][j]
        else:
            break
#map_print(matrix)

# reverse
for mi, m in enumerate(matrix):
    matrix[mi] = m[-1::-1]
#map_print(matrix)


