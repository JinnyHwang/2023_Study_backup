
# k개 중 하나를 N번 선택하기
# curr_num번째 위치에 0 or 1 선택
n = 3
m = 2
answer = []

def print_answer():
    for ans in answer:
        print(ans,end=' ')
    print()

# 추가조건 : 1의 개수가 M개인 수 출력
# 이 방법은 for문을 n번 돌기 때문에 시간복잡도 O(2^n*n)
def Choose1(curr_num):
    if curr_num == n+1:
        cnt = 0
        for e in answer:
            if e == 1:
                cnt += 1
        if cnt == m:
            print_answer()
        return
    
    for i in range(2):
        answer.append(i)
        Choose1(curr_num+1)
        answer.pop()
    '''
    answer.append(0)
    Choose(curr_num+1)
    answer.pop()
    
    answer.append(1)
    Choose(curr_num+1)
    answer.pop()
    '''
#Choose1(1)




def Choose(curr_num, cnt):
    if curr_num == n+1:
        if cnt == m:
            print_answer()
        return
    

    answer.append(0)
    Choose(curr_num+1, cnt)
    answer.pop()
    
    answer.append(1)
    Choose(curr_num+1, cnt+1)
    answer.pop()
    
#Choose(1,0)



N, M = tuple(map(int, input().split()))
visited = [0 for _ in range(N+1)]
ans = []

def ans_print():
    for a in ans:
        print(a,end=' ')
    print()

'''
def Choose(cnt):

    if cnt == M+1:
        ans_print()
        return

    for n in range(1,N+1):
        if visited[n] == 0:
            visited[n] = 1
            ans.append(n)
            Choose(cnt+1)
            ans.pop()

Choose(1)
'''
# 탐색하는 번호, 몇 번 째 탐색인지 cnt에 기록
def find_combination(curr_num, cnt):
    # 범위는 벗어나는 숫자 탐색할 때 종료
    if curr_num == N+1:
        if cnt == M:
            ans_print()
        return
    
    # 현재 번호를 넣는 경우
    ans.append(curr_num)
    find_combination(curr_num+1,cnt+1)
    ans.pop()

    # 현재 번호를 넣지 않는 경우
    find_combination(curr_num+1,cnt)

#find_combination(1,0)


# 백트래킹으로 가능한 모든 조합을 탐색
# 오름차순으로 순서쌍이 만들어지려면?
# 마지막으로 선택한 숫자를 재귀함수의 last_num인자로 해결할 수 있음

# N개 중 M개의 숫자를 뽑아 서로 다른 조합을 만들면 증가수열이 됨
# 이후에 고르게 되는 숫자는 뽑았던 숫자보다 항상 커져야함
# 이전에 골라진 값을 기준으로 이후의 값만 순화하기 위해서는 재귀함수 인자에
# 마지막으로 뽑은 숫자를 알려주면 됨

# 뽑은 숫자 개수는 cnt로 표기
# 마지막으로 뽑은 숫자는 last_num으로 표기
# 남은 숫자 중 어떤 숫자를 뽑을지 선택
combi = []

def print_combi():
    for a in combi:
        print(a,end=' ')
    print()

# last_num 활용
# 시작을 정해주기
def FindCombination(cnt, last_num):
    
    if cnt == M:
        print_combi()
        return
    
    for i in range(last_num+1, N+1):
        combi.append(i)
        FindCombination(cnt+1,i)
        combi.pop()
        
'''    
for i in range(1,N+1):
    combi.append(i)
    FindCombination(1,i)
    combi.pop()
'''

def FindCombination2(cnt, last_num):
    
    if cnt == M:
        print_combi()
        return
    '''
    for i in range(last_num+1, N+1):
        if i not in combi:
            print('?', i)
            print('combi?', combi)
            combi.append(i)
            FindCombination2(cnt+1, i)
            combi.pop()
            print('??', i)
    '''
    
    for i in range(last_num+1, N+1):
        print('!', i)
        print('combi?', combi)
        combi.append(i)
        FindCombination2(cnt+1, i)
        combi.pop()
        print('!!', i)
    
    


print('FindCombination2')
FindCombination2(0,0)


